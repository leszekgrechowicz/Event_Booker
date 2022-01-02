import datetime
from django import forms
from . import models


class CustomerBookForm(forms.ModelForm):
    class Meta:

        ATTRS = {

        }

        model = models.Customer
        fields = ['name', 'surname', 'email', 'birth_year']

        widgets = {
            'name': forms.TextInput(),
            'surname': forms.TextInput(),
            'email': forms.TextInput(),
            'birth_year': forms.NumberInput(),
        }

    # def clean_birth_year(self):
    #     birth_year = self.cleaned_data['birth_year']
    #     print(birth_year)
    #     restriction_set = self.cleaned_data['age_restriction']
    #     print(restriction_set)
    #
    #     if restriction_set:
    #
    #         year_now = datetime.date.today().year
    #         if (year_now - birth_year) < 18:
    #             raise forms.ValidationError(f"Unfortunately you are too young for this event")
    #         return birth_year
    #
    #     return birth_year



