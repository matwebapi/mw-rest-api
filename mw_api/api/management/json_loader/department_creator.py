from api.models import (Campus, Department, )
from api.management.json_loader.creator import ListsCreator
from api.management.json_loader.json_path import Json
from api.management.json_loader.utils import debug


class DepartmentsCreator(ListsCreator):
    keys = ('CODIGO', 'DENOMINACAO', 'SIGLA')

    def __init__(self, json_data):
        self.json_name, self.data = Json.get_root_data(json_data)
        self.__set_campus_name()

        super().__init__(keys=DepartmentsCreator.keys, data=self.data)

    def __set_campus_name(self):
        PREFIX = 'DEPARTAMENTOS_'
        assert(self.json_name.startswith(PREFIX))
        self.campus_name = self.json_name[len(PREFIX):]

    def create_departments(self):
        self._init_lists()

        for i in range(len(self.lists)):
            self.__create_department_from_index(i)

    def try_get_department(self, code, initials, name, campus):
        try:
            department = Department.objects.get(code=code)
            print('DEPARTMENT [{}] already existed.'.format(department.name))
        except Department.DoesNotExist:
            department = Department.objects.create(code=code, initials=initials,
                                                name=name, campus=campus)
            print('Created DEPARTMENT [{}] successfully'.format(department.name))
        return department

    def try_get_campus(self, name):
        try:
            campus = Campus.objects.get(name=name)
        except Campus.DoesNotExist:
            campus = Campus.objects.create(name=name)
        return campus

    def __create_department_from_index(self, i):
        code, name, initials = self.lists[i]

        campus = self.try_get_campus(name=self.campus_name)

        department = self.try_get_department(code, name, initials, campus)
        return department
