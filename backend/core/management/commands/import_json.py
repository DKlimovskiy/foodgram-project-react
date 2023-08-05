import json
from django.conf import settings
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "".join([os.linesep, settings.HPI_JSON_MSG])

    def handle(self, *args, **kwargs):
        json_path = settings.HPI_JSON_PATH

        with open(json_path, 'rb') as file:
            data = json.load(file)
            self._perform_import(data)

        success_message = "".join([settings.SUCC_IMP_MSG, os.linesep])
        self.stdout.write(self.style.SUCCESS(success_message))

    def _perform_import(self, data):
        from core.utils import load_ingredients_data
        load_ingredients_data(data)
