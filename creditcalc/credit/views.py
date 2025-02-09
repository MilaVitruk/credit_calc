from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from credit.models import Loan, Loan_details
from django.urls import reverse

from .forms import LoanCreationForm

# import credit.urls.urlpatterns as urls
# def count_num_of_payments(object) -> int:
#     years_full = object.term.days // 365
#     days_left = object.term.days - years_full * 365
#     months_amount = years_full * 12 + days_left // 30
#     days_left -= (months_amount % 12) * 30.5
#     # Использовала грубоватый расчет, без учета високосных годов и февраля. Возможно вернусь к этому
#     if days_left != 0:
#         months_amount += 1
#     return months_amount
#
# def count_payment_every_month(object):
#     # расчет месячной процентной ставки
#     if object.num_of_payments and object.num_of_payments != 0:
#         monthly_rate = object.rate / (12 * 100)
#         k_ann = (monthly_rate*(1+monthly_rate) ** object.num_of_payments)/(((1 + monthly_rate) ** object.num_of_payments) - 1)
#         payment_per_month = object.amount * k_ann
#         return round(payment_per_month, 2)
#     else:
#         return 0
#
def count_total_amount(object):
    return object.payment_per_month * object.num_of_payments

def credit_homepage(request: HttpRequest):
    # Добавлю перечень ссылок сюда
    # context = {'links': urls}
    # print(urls)
    return render(request, 'credit/homepage.html')

def loans_list(request: HttpRequest) -> HttpResponse:
    context = {
        'loans': Loan.objects.all(),
    }
    for loan in context['loans']:
        loan.total_amount = count_total_amount(loan)
        loan.overpay = loan.total_amount - loan.amount

    return render(request, 'credit/loans-list.html', context=context)

def create_loan(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoanCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            url = reverse('credit:loans_list')
            return redirect(url)
    else:
        form = LoanCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'credit/loan-creation-form.html', context=context)
