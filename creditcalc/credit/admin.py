from django.contrib import admin

from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'amount', 'rate', 'start_date', 'term']
