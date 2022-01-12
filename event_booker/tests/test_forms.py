from django.test import TestCase
from ..forms import CustomerBookForm
from ..models import Customer
import datetime


class EvenBookFormTest(TestCase):
    """Form Tests"""

    def setUp(self) -> None:
        self.form = CustomerBookForm()
        self.customer_data = {'name': 'Leszek', 'surname': 'Grechowicz', 'email': 'leszek@o2.pl', 'birth_year': 1978}

    def test_empty_form(self):
        self.assertIn('name', self.form.fields)
        self.assertIn('surname', self.form.fields)
        self.assertIn('email', self.form.fields)
        self.assertIn('birth_year', self.form.fields)
        self.assertNotIn('uuid', self.form.fields)

    def test_field_name_label(self):
        self.assertTrue(self.form.fields['name'].label == 'Name')

    def test_field_surname_label(self):
        self.assertTrue(self.form.fields['surname'].label == 'Surname')

    def test_field_email_label(self):
        self.assertTrue(self.form.fields['email'].label == 'Email')

    def test_field_birth_year_label(self):
        self.assertTrue(self.form.fields['birth_year'].label == 'Birth year')

    def test_valid_form(self):
        form = CustomerBookForm(data=self.customer_data)
        self.assertTrue(form.is_valid())

    def test_not_valid_form(self):
        self.customer_data['birth_year'] = datetime.datetime.now().year - 151
        form = CustomerBookForm(data=self.customer_data)
        self.assertFalse(form.is_valid())

    def test_not_valid_form_date_above_todays_date(self):
        self.customer_data['birth_year'] = datetime.datetime.now().year + 1
        form = CustomerBookForm(data=self.customer_data)
        self.assertFalse(form.is_valid())
