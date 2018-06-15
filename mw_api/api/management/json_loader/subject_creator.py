from api.models import (Campus, Department, )
from api.management.json_loader.creator import ListsCreator
from api.management.json_loader.json_path import Json


class SubjectsCreator(ListsCreator):
    code = 'CODIGO_DISCIPLINA'
    name = 'MATERIA'

    def __init__(self, json_data):
        pass

    def __set_keys(self):
        self.keys = (SubjectsCreator.code, SubjectsCreator.name,
                     self.department_name)

    def __set_department_name(self):
        PREFIX = 'DISCIPLINAS_'
        assert(self.json_name.startswith(PREFIX))
        self.department_name = self.json_name[len(PREFIX):]

#    def create_departments(self):
#        self._init_lists()
#
#        for i in range(len(self.lists)):
#            self.__create_department_from_index(i)
#
#    def __create_department_from_index(self, i):
#        code, name, initials = self.lists[i]
#        campus = Campus.objects.get_or_create(name=self.campus_name)[0]
#
#        department, created = Department.objects.get_or_create(code=code, initials=initials,
#                                           name=name, campus=campus)
#        if created:
#            print('Created DEPARTMENT [{}] successfully'.format(department.name))
#        else:
#            print('DEPARTMENT [{}] already existed.'.format(department.name))
#        return department
