from django.urls import path
from .views import credit_homepage, loans_list, create_loan

app_name = 'credit'
urlpatterns = [
    path('', credit_homepage, name='homepage'),
    path('loans/', loans_list, name='loans_list'),
    path('add-loan/', create_loan, name='add_loan'),

]