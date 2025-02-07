from django import forms

from credit.models import Loan


class LoanCreationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = 'title', 'amount', 'rate', 'term'