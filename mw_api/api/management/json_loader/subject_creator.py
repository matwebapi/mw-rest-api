from api.models import Department, Subject

from api.management.json_loader.creator import ListsCreator
from api.management.json_loader.json_path import Json
from api.management.json_loader.utils import debug


class SubjectsCreator(ListsCreator):

    def __init__(self, json_data):
        self.json_name, self.data = Json.get_root_data(json_data)
        self.__set_department_name()
        self.__set_keys()
        self.__set_department()

        del self.data[self.department_key_name]
        super().__init__(keys=self.keys, data=self.data)

    def __set_department_name(self):
        PREFIX = 'DISCIPLINAS_'
        assert(self.json_name.startswith(PREFIX))
        self.department_name = self.json_name[len(PREFIX):]

    def __set_department(self):
        self.department_code = self.data[self.department_key_name]
        self.department = Department.objects.get_or_create(code=self.department_code)[0]

    def __set_keys(self):
        self.department_key_name = 'CODIGO_DEPARTAMENTO_' + \
                                        self.department_name + ':'
        self.codes_key = 'CODIGO_DISCIPLINA'
        self.names_key = 'MATERIA'

        self.keys = (self.codes_key, self.names_key)

    def create_subjects(self):
        self._init_lists()
        debug('subject_lists', self.lists)

        for i in range(len(self.lists)):
            self.__create_subject_from_index(i)

    def __create_subject_from_index(self, i):
        subject_code, subject_name = self.lists[i]
        subject_code = int(subject_code)


        try:
            subject = Subject.objects.get(code=subject_code)
            print('SUBJECT [{}] already existed.'.format(subject.name))
        except Subject.DoesNotExist:
            subject = Subject.objects.create(code=subject_code,
            name=subject_name, department=self.department)
            print('Created SUBJECT [{}] successfully'.format(subject.name))
        return subject
