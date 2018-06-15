import json
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import (Campus, Department, )

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


def debug(a, b):
    print('\n' * 5)
    print('DEBUG')
    print('{} = {}'.format(a, b))
    print('type({}) = {}'.format(a, type(b)))

class DepartmentCreator:
    key_map = {
        'code': 'CODIGO',
        'name': 'DENOMINACAO',
        'initials': 'SIGLA'
    }

    def __init__(self, json_data):
        self.json_name = list(json_data.keys())[0]
        self.data = json_data[self.json_name]
        self.__set_campus_name()

        for value in DepartmentCreator.key_map.values():
            assert(value in self.data.keys())


    def __set_campus_name(self):
        PREFIX = 'DEPARTAMENTOS_'
        assert(self.json_name.startswith(PREFIX))
        self.campus_name = self.json_name[len(PREFIX):]

    def __init_lists(self):
        tuples = []
        lists = []
        for item in DepartmentCreator.key_map.items():
            key, key_json = item
            value = self.data[key_json]
            if not isinstance(value, list):
                value = [value]

            tuples.append((key, value))
            lists.append(value)

        lists = list(zip(*lists))
        self.lists = lists

    def create_departments(self):
        self.__init_lists()

        for i in range(len(self.lists)):
            self.__create_department_from_index(i)

    def __create_department_from_index(self, i):
        code, name, initials = self.lists[i]
        campus = Campus.objects.get_or_create(name=self.campus_name)[0]

        department, created = Department.objects.get_or_create(code=code, initials=initials,
                                           name=name, campus=campus)
        if created:
            print('Created DEPARTMENT [{}] successfully'.format(department.name))
        else:
            print('DEPARTMENT [{}] already existed.'.format(department.name))
        return department

class MiddleParser:
    DEPARTAMENTOS = 'DEPARTAMENTOS_'
    DISCIPLINAS = 'DISCIPLINAS_'

    def __init__(self):
        pass

    def create_model_according_to_json_name(self, name):
        assert(name.endswith(Json.EXTENSION))
        data = Json.get_json_data(name)
        root = list(data.keys())[0]

        if name.startswith(MiddleParser.DEPARTAMENTOS):
            debug('data', data)
            print('Creating DEPARTMENTS: {}'.format(root))
            dc = DepartmentCreator(data)
            d = dc.create_departments()
            if name != 'DEPARTAMENTOS_FGA.json':
                return
            else:
                debug('FGA.data', data)
        elif name.startswith(MiddleParser.DISCIPLINAS):
            pass
  #          print('Creating SUBJECT')
        else:
            raise Exception('File name not supported')
