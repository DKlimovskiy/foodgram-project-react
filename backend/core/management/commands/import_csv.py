import csv
from django.conf import settings
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "".join([os.linesep, settings.HPI_CMSG])

    def handle(self, *args, **kwargs):
        csv_path = settings.HPI_CSV_PATH

        with open(csv_path, 'r') as file:
            data = csv.DictReader(file)
            self._perform_import(data)

        success_message = "".join([settings.SUCC_IMP_MSG, os.linesep])
        self.stdout.write(self.style.SUCCESS(success_message))

    def _perform_import(self, data):
        from core.utils import load_ingredients_data
        load_ingredients_data(data)
