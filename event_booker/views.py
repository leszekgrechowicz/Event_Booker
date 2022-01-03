import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
import uuid

from django.views.generic import FormView

from event_booker.forms import CustomerBookForm
from event_booker.models import Event, Customer
from event_booker.utils import list_divider

test = uuid.uuid4()


# # recommended, uuid guarantees uniqueness.
#
# >>> import uuid
# >>> print(uuid.uuid4().hex)
# '772d4c80-3668-4980-a014-aae59e34b9b9'
#
# # others way, some sort of salt combination
#
# >>> import secrets, hashlib
# >>> first_name = user.first_name  # pull user first name, a salt.
# >>> salt = secrets.token_hex(8) + first_name
# >>> hashlib.sha256(salt.encode('utf-8')).hexdigest()
# 'f8b2e14fe3496de336017687089fb3c49bcab889ac80545fc087289c5b1a3850'

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
                messages.warning(request, f'Unfortunately this event is for adults only !')
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
            # link = reverse('event_booker:confirm-booking', kwargs={'uuid': uuid_})
            send_mail(f' {event.name} booking  confirmation.',
                      f'Dear {name} {surname},\n \n\tPlease kindly confirm your attendance to an Event '
                      f'"{event.name}" \n at {event.date} by following the link below \n'
                      f'http://127.0.0.1:8000/booking-confirmation/{uuid_}/ .\n'
                      f'Kind Regards, \n'
                      f'Team - EvEnter',
                      'no-reply@eventer.com',
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
        except ValueError:
            raise Http404()
        event =

        return render(request, 'event_booker/booking-confirmation.html', {'customer': customer})
