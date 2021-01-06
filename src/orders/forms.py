from django import forms

from .models import Order
from django_countries.widgets import CountrySelectWidget

class OrderCreateForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address',
              'postal_code', 'city', 'country']
    widgets = {'country': CountrySelectWidget()}
