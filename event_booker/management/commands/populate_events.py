from django.core.management.base import BaseCommand
from ._private import create_events


class Command(BaseCommand):
    help = 'Populate Events with dummy events'

    def handle(self, *args, **options):
        create_events()
        self.stdout.write(self.style.SUCCESS("Successfully populated Events table with dummy Events"))


