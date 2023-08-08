from django.forms import ModelForm
from .models import Count


class CountForm(ModelForm):
    class Meta:
        model = Count
        fields = '__all__'

from django import forms


class ConverterForm(forms.Form):
    system = forms.IntegerField()
    number = forms.IntegerField()