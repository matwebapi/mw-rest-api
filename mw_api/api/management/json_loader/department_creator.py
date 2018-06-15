from api.models import (Campus, Department, )


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
