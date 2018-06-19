from api.management.json_loader.json_path import Json
from api.management.json_loader .department_creator import DepartmentsCreator
from api.management.json_loader .subject_creator import SubjectsCreator
from api.management.json_loader.utils import debug


class MiddleParser:
    DEPARTAMENTOS = 'DEPARTAMENTOS_'
    DISCIPLINAS = 'DISCIPLINAS_'

    def __init__(self, json_names):
        self.__init_models_lists(json_names)
        pass

    def __init_models_lists(self, json_names):
        self.department_names = []
        self.subject_names = []

        for name in json_names:
            assert(name.endswith(Json.EXTENSION))
            if name.startswith(MiddleParser.DEPARTAMENTOS):
                self.department_names.append(name)
            elif name.startswith(MiddleParser.DISCIPLINAS):
                self.subject_names.append(name)
            else:
                raise Exception('File name not supported')

    def create_all_models(self):
        for name in self.department_names:
            data = Json.get_json_data(name)
            dc = DepartmentsCreator(data)
            d = dc.create_departments()

            if name == 'DEPARTAMENTOS_FUP.json':
                debug('name', name)
                debug('data', data)

        for name in self.subject_names:
            data = Json.get_json_data(name)

            sc = SubjectsCreator(data)
            s = sc.create_subjects()
