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




