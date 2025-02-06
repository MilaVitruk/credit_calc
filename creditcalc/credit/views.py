from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from credit.models import Loan, Loan_details

# import credit.urls.urlpatterns as urls
def count_num_of_payments(object) -> int:
    years_full = object.term.days // 365
    days_left = object.term.days - years_full * 365
    months_amount = years_full * 12 + days_left // 30
    days_left -= (months_amount % 12) * 30.5
    # Использовала грубоватый расчет, без учета високосных годов и февраля. Возможно вернусь к этому
    if days_left != 0:
        months_amount += 1
    return months_amount


def credit_homepage(request: HttpRequest):
    # context = {'links': urls}
    # print(urls)
    return render(request, 'credit/homepage.html')

def loans_list(request: HttpRequest):
    context = {
        'loans': Loan.objects.all(),
    }
    for loan in context['loans']:
        loan.num_of_payments = count_num_of_payments(loan)

    return render(request, 'credit/loans-list.html', context=context)
