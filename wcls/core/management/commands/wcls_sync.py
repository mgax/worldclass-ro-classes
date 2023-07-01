from django.core.management.base import BaseCommand

from ...scraping import sync


class Command(BaseCommand):
    def handle(self, *args, **options):
        sync()
