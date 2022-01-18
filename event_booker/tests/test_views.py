import uuid
import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail

from ..models import Event, Customer


class MyTestSettings(TestCase):
    """Main test settings"""

    def setUp(self) -> None:
        self.client = Client()
        self.event1 = Event.objects.create(name="event1",
                                           date="2022-01-30",
                                           start_date="2022-01-10",
                                           end_date="2022-01-29",
                                           places=30,
                                           description='Test Description',
                                           age_restriction=True)
        self.event_view_url = reverse('event_booker:main-show-events')
        self.book_event_url = reverse('event_booker:book-event', kwargs={'id': self.event1.id})
        self.uuid_ = uuid.uuid4()
        self.correct_customer_data = {'name': 'Leszek',
                                      'surname': 'Grechowicz',
                                      'email': 'Leszek@o2.pl',
                                      'birth_year': '1978',
                                      }


class TestEventView(MyTestSettings):
    """Test Show Events View"""

    def setUp(self) -> None:
        super(TestEventView, self).setUp()

    def test_event_view(self):
        response = self.client.get(self.event_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_booker/index.html')


class TestBookEventView(MyTestSettings):
    """Test Customer Book Event"""

    def setUp(self):
        super(TestBookEventView, self).setUp()

    def test_book_event_view_GET(self):
        response = self.client.get(self.book_event_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_booker/book-event.html')


class TestProcessingBooking(MyTestSettings):

    def setUp(self, datatime=None) -> None:
        super(TestProcessingBooking, self).setUp()
        self.customer_count = Customer.objects.count()
        self.age_restriction_customer_data = self.correct_customer_data.copy()
        self.age_restriction_customer_data['birth_year'] = f'{datetime.datetime.now().year - 1}'

    def test_form_submit_view(self):
        response = self.client.post(self.book_event_url, self.correct_customer_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Customer.objects.count(), self.customer_count + 1)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, f'{self.event1.name} booking confirmation.')

    def test_form_submit_age_restriction(self):
        response = self.client.post(self.book_event_url, self.age_restriction_customer_data)
        print('******************888')
        print(self.age_restriction_customer_data)
        self.assertEqual(response.status_code, 302)

