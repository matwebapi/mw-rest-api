from api.management.json_loader.utils import debug

class ListsCreator:
    def __init__(self, keys, data):
        assert(isinstance(keys, tuple))
        assert(isinstance(data, dict))
        assert(set(keys) == set(data.keys()))

        self.keys = keys
        self.data = data
        self._init_lists()

    def _init_lists(self):
        lists = []
        for key in self.keys:
            value = self.data[key]
            if not isinstance(value, list):
                value = [value]
            lists.append(value)

        lists = list(zip(*lists))
        self.lists = lists
