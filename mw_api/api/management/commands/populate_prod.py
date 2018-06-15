import json
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import (Department, )

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

class Path:

    @staticmethod
    def parent_dir(dir):
        parent = os.path.realpath(os.path.join(dir, os.pardir))
        return parent

    @staticmethod
    def child_dir(parent, child):
        dir = os.path.realpath(os.path.join(parent, child))
        return dir

    @staticmethod
    def get_file_path(dir, file):
        path = os.path.realpath(os.path.join(dir, file))
        return path

    @staticmethod
    def get_kth_parent(dir, k):
        for i in range(k + 1):
            dir = Path.parent_dir(dir)
        return dir

    @staticmethod
    def get_file_names_in_dir(dir, extension=''):
        all_files = os.listdir(dir)
        files = [file for file in all_files if file.endswith(extension)]
        return files


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

class DepartmentCreator:
    key_map = {
        'code': 'CODIGO',
        'name': 'DENOMINACAO',
        'initials': 'SIGLA'
    }

    def __init__(self, json_data):
        for value in DepartmentCreator.key_map.values():
            assert(value in json_data.keys())
        self.data = json_data

    def create_department(self):
        tuples = []
        for item in DepartmentCreator.key_map.items():
            key, key_json = item
            value = self.data[key_json]
            tuples.append((key, value))
        kwargs = dict(tuples)
        department, created = Department.objects.get_or_create(**kwargs)[0]
        if created:
            print('Creating department: {}'.format(department.name))
        else:
            print('Cant create department: {}'.format(department.name))

class MiddleParser:
    DEPARTAMENTOS = 'DEPARTAMENTOS_'
    DISCIPLINAS = 'DISCIPLINAS_'

    def __init__(self):
        pass

    def create_model_according_to_json_name(self, name):
        assert(name.endswith(Json.EXTENSION))
        data = Json.get_json_data(name)
        root_name = list(data.keys())[0]
        data = data[root_name]

        if name.startswith(MiddleParser.DEPARTAMENTOS):
            dc = DepartmentCreator(data)
            d = dc.create_department()
            return
        elif name.startswith(MiddleParser.DISCIPLINAS):
            print('Creating SUBJECT')
        else:
            raise Exception('File name not supported')
