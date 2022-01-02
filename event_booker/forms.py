from django import forms
from . import models


class CustomerBookForm(forms.ModelForm):
    class Meta:

        ATTRS = {
            'class': 'form-control mt-1',
        }

        model = models.Customer
        fields = ['name', 'surname', 'email', 'birth_year']

        widgets = {
            'name': forms.TextInput(attrs=ATTRS),
            'surname': forms.TextInput(attrs=ATTRS),
            'email': forms.TextInput(attrs=ATTRS),
            'birth_year': forms.NumberInput(attrs=ATTRS),
        }



