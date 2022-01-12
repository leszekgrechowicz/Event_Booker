from django.test import TestCase
from ..models import Event, Customer, EventImage


class TestEventModel(TestCase):
    """Test the Event Model"""

    def setUp(self) -> None:
        self.e = Event(name="Django Test",
                       date="2022/01/30",
                       start_date="2022/01/10",
                       end_date="2022/01/29",
                       places=30,
                       description='Test Description')

    def test_create_event(self):
        self.assertIsInstance(self.e, Event)

    def test_str_representation(self):
        self.assertEquals(str(self.e), "Django Test")

    def test_name_label(self):
        field_label = self.e._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_event_name_max_length(self):
        max_length = self.e._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_description_max_length(self):
        max_length = self.e._meta.get_field('description').max_length
        self.assertEquals(max_length, 200)


class TestCustomerModel(TestCase):
    """Test the Customer Model"""

    def setUp(self) -> None:
        self.c = Customer(name='Leszek',
                          surname='Grechowicz',
                          email='leszek@o2.pl',
                          birth_year="1978/01/08")

    def test_create_customer(self):
        self.assertIsInstance(self.c, Customer)

    def test_str_representation(self):
        self.assertEquals(str(self.c), "Leszek Grechowicz")


class TestImageModel(TestCase):
    """Test the Image Model"""

    def setUp(self) -> None:
        self.e = Event(name="Django Test",
                       date="2022/01/30",
                       start_date="2022/01/10",
                       end_date="2022/01/29",
                       places=30,
                       description='Test Description')

        self.i = EventImage(scr="./images/test/image.jpg",
                            event=self.e)

    def test_create_image_model(self):
        self.assertIsInstance(self.i, EventImage)

    def test_str_representation(self):
        self.assertEquals(str(self.i), "./images/test/image.jpg")
