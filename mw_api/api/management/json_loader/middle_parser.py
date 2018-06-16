from api.management.json_loader.json_path import Json
from api.management.json_loader .department_creator import DepartmentsCreator
from api.management.json_loader .subject_creator import SubjectsCreator
from api.management.json_loader import utils


class MiddleParser:
    DEPARTAMENTOS = 'DEPARTAMENTOS_'
    DISCIPLINAS = 'DISCIPLINAS_'

    def __init__(self):
        pass

    def create_model_according_to_json_name(self, name):
        assert(name.endswith(Json.EXTENSION))

        department_names = []
        subject_names = []

        if name.startswith(MiddleParser.DEPARTAMENTOS):
            department_names.append(name)
        elif name.startswith(MiddleParser.DISCIPLINAS):
            subject_names.append(name)
        else:
            raise Exception('File name not supported')

        for name in department_names:
            data = Json.get_json_data(name)
            dc = DepartmentsCreator(data)
            d = dc.create_departments()

        for name in subject_names:
            data = Json.get_json_data(name)

            sc = SubjectsCreator(data)
            s = sc.create_subjects()
