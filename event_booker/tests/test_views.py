from django.test import TestCase, Client
from django.urls import reverse

from ..models import Event


class TestEventView(TestCase):
    """Test Show Events View"""

    def setUp(self) -> None:
        self.client = Client()

    def test_event_view(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_event_view_accessible_by_name(self):
        response = self.client.get(reverse('event_booker:main-show-events'))
        self.assertEquals(response.status_code, 200)
