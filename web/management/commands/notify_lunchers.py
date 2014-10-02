from django.core.management.base import BaseCommand
from web.scripts import notify_lunchers


class Command(BaseCommand):

    def handle(self, *args, **options):
        notify_lunchers()