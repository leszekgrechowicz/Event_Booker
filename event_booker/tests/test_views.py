from django.test import TestCase, Client
from django.urls import reverse

from ..models import Event


class TestEventView(TestCase):
    """Test Show Events View"""

    def setUp(self) -> None:
        self.client = Client()
        self.event_view_url = reverse('event_booker:main-show-events')

    def test_event_view(self):
        response = self.client.get(self.event_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_booker/index.html')


class TestBookEventView(TestCase):
    """Test Customer Book Event"""

    def setUp(self):
        self.event1 = Event.objects.create(name="event1",
                                           date="2022-01-30",
                                           start_date="2022-01-10",
                                           end_date="2022-01-29",
                                           places=30,
                                           description='Test Description')
        self.book_event_url = reverse('event_booker:book-event', kwargs={'id': self.event1.id})

    def test_book_event_view_GET(self):
        response = self.client.get(self.book_event_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_booker/book-event.html')
