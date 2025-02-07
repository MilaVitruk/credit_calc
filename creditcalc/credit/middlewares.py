from django.http import HttpRequest

# def set_
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
    monthly_rate = object.rate / (12 * 100)
    k_ann = (monthly_rate*(1+monthly_rate) ** object.num_of_payments)/(((1 + monthly_rate) ** object.num_of_payments) - 1)
    payment_per_month = object.amount * k_ann
    return round(payment_per_month, 2)

def count_total_amount(object):
    return object.payment_per_month * object.num_of_payments