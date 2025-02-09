from django.http import HttpRequest

from credit.models import Loan




def count_num_of_payments(object) -> int:
    years_full = object.term.days // 365
    days_left = object.term.days - years_full * 365
    months_amount = years_full * 12 + days_left // 30
    days_left -= (months_amount % 12) * 30.5
    # Использовала грубоватый расчет, без учета високосных годов и февраля. Возможно вернусь к этому
    if days_left != 0:
        months_amount += 1
    return months_amount

def count_payment_every_month(object):
    # расчет месячной процентной ставки
    if object.num_of_payments and object.num_of_payments != 0:
        monthly_rate = object.rate / (12 * 100)
        k_ann = (monthly_rate*(1+monthly_rate) ** object.num_of_payments)/(((1 + monthly_rate) ** object.num_of_payments) - 1)
        payment_per_month = object.amount * k_ann
        return round(payment_per_month, 2)
    else:
        return 0

def count_total_amount(object):
    return object.payment_per_month * object.num_of_payments



def count_ant_set_fields_middleware(get_response):
    print('Before middleware')
    def middleware(request: HttpRequest):
        print('Before get_response')
        response = get_response(request)
        print('you can correct the answer here')
        print(Loan.objects.all())
        for loan in Loan.objects.all():
            loan.num_of_payments = count_num_of_payments(loan)
            loan.payment_per_month = count_payment_every_month(loan)
            loan.total_amount = count_total_amount(loan)
            loan.overpay = loan.total_amount - loan.amount
        for loan in Loan.objects.all():
            print(loan.title)
            print(loan.num_of_payments)
            print(loan.payment_per_month)
            print(loan.total_amount)

        return response


    return middleware