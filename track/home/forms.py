import datetime

from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TrackSearchForm(forms.Form):
    shipped_from = forms.DateField(
        label='Shipped from, date',
        widget=DateInput(attrs={'class': 'delivery-form__input',
                                'value': (datetime.date.today() - datetime.timedelta(days=1))})
    )
    shipped_to = forms.DateField(
        initial=datetime.date.today,
        label='Shipped to, date',
        widget=DateInput(attrs={'class': 'delivery-form__input',
                                'value': datetime.date.today()})
    )
    state = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'delivery-form__input'})
    )
    senders_zip = forms.IntegerField(
        label="Sender's ZIP",
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'delivery-form__input'})
    )
