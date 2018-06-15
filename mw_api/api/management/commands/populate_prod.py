from django.core.management.base import BaseCommand, CommandError

from api.management.json_loader.json_path import Json
from api.management.json_loader.middle_parser import MiddleParser


class Command(BaseCommand):
    help = 'Populate initial data for production API.'

    def handle(self, *args, **options):
        jsons = Json.get_json_names()
        m = MiddleParser()
        for name in jsons:
            m.create_model_according_to_json_name(name)


