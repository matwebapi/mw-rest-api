from django.core.management.base import BaseCommand, CommandError

from api.management.json_loader.json_path import Json
from api.management.json_loader.middle_parser import MiddleParser


class Command(BaseCommand):
    help = 'Populate initial data for production API.'

    def handle(self, *args, **options):
        jsons = Json.get_json_names()

        middle_parser = MiddleParser(jsons)
        middle_parser.create_all_models()


