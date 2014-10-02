from django.core.management.base import BaseCommand
from web.scripts import check_quorum


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_quorum()