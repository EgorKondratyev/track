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
