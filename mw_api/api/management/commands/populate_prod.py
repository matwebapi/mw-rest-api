from django.core.management.base import BaseCommand, CommandError

from api.management.json_loader.json_path import Json
from api.management.json_loader.middle_parser import MiddleParser


class Command(BaseCommand):
    help = 'Populate initial data for production API.'

    def handle(self, *args, **options):
        fga = 'DEPARTAMENTOS_FGA.json'
        data = Json.get_json_data(fga)
        jsons = Json.get_json_names()

        print('HANDLE[jsons] = {}'.format(jsons))
        print('\n' * 5)

        m = MiddleParser()
        for name in jsons:
            m.create_model_according_to_json_name(name)


