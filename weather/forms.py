from django import forms
from .models import *


class SearchForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)
