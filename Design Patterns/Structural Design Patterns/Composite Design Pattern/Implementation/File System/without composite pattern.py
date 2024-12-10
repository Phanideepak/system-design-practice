# Parent Class
class Directory:
    def __init__(self, directory_name):
        self.__directory_name = directory_name
        self.__obj_list = []
    
    def add(self, object):
        self.__obj_list.append(object)
    
    def ls(self):
        print(f'Director name : {self.__directory_name}')
        for obj in self.__obj_list:
            obj.ls()

# Child Class
class File:
    def __init__(self, file_name):
        self.__file_name = file_name
    
    def ls(self):
        print(f'File Name: {self.__file_name}')