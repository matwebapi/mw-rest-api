import json
import os

from django.conf import settings

from api.management.json_loader.path import Path


class Json:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    FIXTURES_DIR = Path.child_dir(settings.BASE_DIR, 'fixtures')
    JSON_DIR = Path.child_dir(FIXTURES_DIR, 'JSONS')
    EXTENSION = '.json'

    @staticmethod
    def get_json_data(file_name):
        file_path = Path.get_file_path(Json.JSON_DIR, file_name)
        with open(file_path, 'r') as read_file:
            data = json.load(read_file)
            return data

    @staticmethod
    def get_json_names():
        jsons = Path.get_file_names_in_dir(Json.JSON_DIR + os.sep,
                                          extension=Json.EXTENSION)
        return jsons

