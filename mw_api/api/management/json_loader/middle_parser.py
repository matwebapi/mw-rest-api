from api.management.json_loader.json_path import Json
from api.management.json_loader .department_creator import DepartmentsCreator
from api.management.json_loader import utils


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
            utils.debug('data', data)
            print('Creating DEPARTMENTS: {}'.format(root))
            dc = DepartmentsCreator(data)
            d = dc.create_departments()
        elif name.startswith(MiddleParser.DISCIPLINAS):
            pass
        else:
            raise Exception('File name not supported')
