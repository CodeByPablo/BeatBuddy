import os
from Config.Singleton import Singleton
    
class Folder(Singleton):
    def __init__(self) -> None:
        if not self.created:
            file_path = os.path.dirname(__file__)
            self.root_folder = self.__get_root_folder(file_path)

    def __get_root_folder(self, current: str) -> str:
        last_sep_index = -1
        for x in range(len(current) - 1, -1, -1):
            if current[x] == os.sep:
                last_sep_index = x
                break

        path = current[:last_sep_index] + os.sep
        return path

