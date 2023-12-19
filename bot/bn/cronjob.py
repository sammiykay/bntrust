from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import MyModel

class Command(BaseCommand):
    help = 'Deletes data from MyModel that is older than 30 days'

    def handle(self, *args, **options):
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        MyModel.objects.filter(created_at__lt=thirty_days_ago).delete()

    def delete_data(self):
        self.handle()
