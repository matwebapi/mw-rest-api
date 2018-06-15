import os


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
