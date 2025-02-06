from django.core.management import BaseCommand
from credit.models import Loan
class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Create loan')
        loan_title = 'car'
        loan_body = 110000.00
        loan_percent = 3
        loan, created = Loan.objects.get_or_create(title=loan_title, body=loan_body,percent=loan_percent)
        print(created)
        self.stdout.write(self.style.SUCCESS('Loan object was created'))
        # except(ModuleNotFoundError):
        #     self.stdout.write((self.style.WARNING('No module named')))


