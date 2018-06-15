from api.models import (Campus, Department, )


class ListsCreator:
    def __init__(self, key_map, json_data):
        self.json_name = list(json_data.keys())[0]
        self.data = json_data[self.json_name]
        self.key_map = key_map

        for value in self.key_map.values():
            assert(value in self.data.keys())

    def _init_lists(self):
        tuples = []
        lists = []
        for item in self.key_map.items():
            key, key_json = item
            value = self.data[key_json]
            if not isinstance(value, list):
                value = [value]

            tuples.append((key, value))
            lists.append(value)

        lists = list(zip(*lists))
        self.lists = lists



class DepartmentCreator(ListsCreator):
    key_map = {
        'code': 'CODIGO',
        'name': 'DENOMINACAO',
        'initials': 'SIGLA'
    }

    def __init__(self, json_data):
        super().__init__(key_map=DepartmentCreator.key_map, json_data=json_data)
        self.__set_campus_name()

    def __set_campus_name(self):
        PREFIX = 'DEPARTAMENTOS_'
        assert(self.json_name.startswith(PREFIX))
        self.campus_name = self.json_name[len(PREFIX):]

    def create_departments(self):
        self._init_lists()

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
