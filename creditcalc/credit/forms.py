from django import forms

from credit.models import Loan
from django.forms import HiddenInput, TextInput, NumberInput, DateInput


class LoanCreationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Title'}),
            'amount': NumberInput(attrs={'placeholder': 'Amount'}),
            'rate': NumberInput(attrs={'placeholder': 'Rate, %'}),
            'term': DateInput(attrs={'placeholder': 'Terms, days'}),
            'num_of_payments': HiddenInput(),
            'payment_per_month': HiddenInput(),
            'total_amount': HiddenInput(),
        }
# '1 00:00:00'
        labels = {'title': '',
                  'amount': '',
                  'rate': '',
                  'term': '',
                  }