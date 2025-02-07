import datetime as dt
from datetime import datetime
from calendar import monthrange

from django.db import models


def convert_to_timedalta(date_as_string):
    dur = datetime.strptime(date_as_string, "%H:%M:%S")
    tot_seconds = dt.timedelta(days=dur.day, hours=dur.hour, minutes=dur.minute, seconds=dur.second).total_seconds()
    dur = dt.timedelta(seconds=tot_seconds)
    return dur


class Loan(models.Model):
    title = models.CharField(max_length=100, null=False, blank=True)
    # purpose = models.CharField(max_length=100)
    # description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=False)
    rate = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    start_date = models.DateField(auto_now_add=True)
    dur = convert_to_timedalta('00:00:00')
    term = models.DurationField(default=dur)
    num_of_payments = models.IntegerField(default=0)
    payment_per_month = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, null=True)


class Loan_details(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE)
    num_of_payments = models.IntegerField(default=0)
