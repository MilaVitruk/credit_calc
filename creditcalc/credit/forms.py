from django import forms

from credit.models import Loan
from django.forms import HiddenInput


class LoanCreationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        widgets = {
            'num_of_payments': HiddenInput(),
            'payment_per_month': HiddenInput(),
            'total_amount': HiddenInput(),
        }