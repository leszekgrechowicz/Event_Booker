import datetime
import uuid

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from event_booker.forms import CustomerBookForm
from event_booker.models import Event, Customer
from event_booker.utils import list_divider


class ShowEventsView(View):
    """Show list of all events"""

    def get(self, request):
        return render(request, 'event_booker/index.html', {
            'title': 'Home',
            'events': list_divider(Event.objects.all().order_by('date'), 3),

        })


class BookEventView(FormView):
    """Customer book event view"""

    def get(self, request, id):
        form = CustomerBookForm()
        return render(request, 'event_booker/book-event.html', {'event': Event.objects.get(id=id),
                                                                'form': form})

    def post(self, request, id):
        form = CustomerBookForm(request.POST)
        event = Event.objects.get(id=id)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            year_now = datetime.date.today().year
            birth_year = form.cleaned_data['birth_year']
            email = form.cleaned_data['email']
            uuid_ = uuid.uuid4()

            if event.age_restriction is True and (year_now - birth_year) < 18:
                messages.warning(request, f'{name.capitalize()} ! Unfortunately this event is for adults only ! '
                                          f'An ID would be checked at the entrance.')
                return redirect('event_booker:main-show-events')
            Customer.objects.create(name=name,
                                    surname=surname,
                                    email=email,
                                    birth_year=birth_year,
                                    invited=True,
                                    event=event,
                                    uuid=uuid_)

            event.no_of_reservations += 1
            event.save()

            domain = get_current_site(request).domain
            link = reverse('event_booker:confirm-booking', kwargs={'uuid_': uuid_})
            link = 'http://' + domain + link
            email_subject = f'{event.name} booking confirmation.'
            email_send_from = 'no-reply@eventer.com'
            email_body = f'Dear {name} {surname},\n \n\tPlease kindly confirm your attendance to an Event ' \
                         f'"{event.name}" \non {event.date} by following the link below: \n' \
                         f'{link} .\n\n' \
                         f'Kind Regards, \n' \
                         f'Team - EvEnter'

            send_mail(email_subject,
                      email_body,
                      email_send_from,
                      [email],
                      fail_silently=False)

            messages.success(request, f'An Email confirmation has been sent to "{email}"')
            return redirect('event_booker:main-show-events')

        return render(request, 'event_booker/book-event.html', {'event': event,
                                                                'form': form})


class ConfirmBooking(View):

    def get(self, request, uuid_):

        try:
            customer = Customer.objects.get(uuid=uuid_)

        except (ValueError, Customer.DoesNotExist):
            raise Http404()

        event = Event.objects.get(id=customer.event.id)

        already_confirmed = False

        if customer.approved is True:
            already_confirmed = True
        else:
            customer.is_checked = True
            customer.approved = True
            customer.save()
            event.confirmed_reservations += 1
            event.save()

        return render(request, 'event_booker/booking-confirmation.html', {'customer': customer,
                                                                          'event': event,
                                                                          'confirmed': already_confirmed})
