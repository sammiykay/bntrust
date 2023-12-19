
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from myapp.models import MohammedUsers

class Command(BaseCommand):
    help = 'Deletes data from MyModel that is older than 2 days'

    def handle(self, *args, **options):
        thirty_days_ago = datetime.now() - timedelta(days=2)
        MohammedUsers.objects.filter(created_at__lt=thirty_days_ago).delete()