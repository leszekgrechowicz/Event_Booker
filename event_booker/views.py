import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
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
            # 'events': list_divider(Event.objects.all().order_by('date'), 3),
            'events': list_divider(Event.objects.all().order_by('date'), 3),

        })


class BookEventView(FormView):
    """Book event view"""

    def get(self, request, id):
        form = CustomerBookForm()
        return render(request, 'event_booker/book-event.html', {'event': Event.objects.get(id=id),
                                                                'form': form})

    def post(self, request, id):
        form = CustomerBookForm(request.POST)
        event = Event.objects.get(id=id)
        if form.is_valid():
            year_now = datetime.date.today().year
            birth_year = form.cleaned_data['birth_year']
            email = form.cleaned_data['email']
            if event.age_restriction is True and (year_now - birth_year) < 18:
                messages.warning(request, f'Unfortunately this event is for adults only !')
                return redirect('event_booker:main-show-events')
            Customer.objects.create(name=form.cleaned_data['name'],
                                    surname=form.cleaned_data['surname'],
                                    email=email,
                                    birth_year=birth_year,
                                    invited=True,
                                    event=event,
                                    uuid=uuid.uuid4())

            event.no_of_reservations += 1
            event.save()
            messages.success(request, f'An Email confirmation has been send to "{email}"')

            return redirect('event_booker:main-show-events')

        return render(request, 'event_booker/book-event.html', {'event': event,
                                                                'form': form})
