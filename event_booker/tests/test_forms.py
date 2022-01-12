from django.test import TestCase
from ..forms import CustomerBookForm
from ..models import Customer


class EvenBookFormTest(TestCase):

    def setUp(self) -> None:
        self.form = CustomerBookForm()

    def test_field_name_label(self):
        self.assertTrue(self.form.fields['name'].label == 'Name')

    def test_field_surname_label(self):
        self.assertTrue(self.form.fields['surname'].label == 'Surname')

    def test_field_email_label(self):
        self.assertTrue(self.form.fields['email'].label == 'Email')

    def test_field_birth_year_label(self):
        self.assertTrue(self.form.fields['birth_year'].label == 'Birth year')

    def test_valid_form(self):
        c = Customer(name='Leszek',
                     surname='Grechowicz',
                     email='leszek@o2.pl',
                     birth_year='2000')
        data = {'name': c.name, 'surname': c.surname, 'email': c.email, 'birth_year': c.birth_year}
        form = CustomerBookForm(data=data)
        self.assertTrue(self.form.is_valid())
