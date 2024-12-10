from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def ls(self):
        pass

class File(FileSystem):
    def __init__(self, name):
        self.__file_name = name 
    
    def ls(self):
        print(f'file name: {self.__file_name}')


class Directory(FileSystem):
    def __init__(self, name):
        self.__directory_name = name
        self.__file_system_list = []

    def add(self, file_system_obj):
        self.__file_system_list.append(file_system_obj)
    
    def ls(self):
        print(f'Directory Name: {self.__directory_name}')

        for file_system_obj in self.__file_system_list:
            file_system_obj.ls()


# Client Code 

if __name__ == '__main__':
    movie_directory = Directory('movies')
    border_file = File('border')
    movie_file1 = File('Transformers')
    movie_file2 = File('Ultron')
    movie_file3 = File('Avengers')
    movie_directory.add(border_file)
    movie_directory.add(movie_file1)
    movie_directory.add(movie_file2)
    movie_directory.add(movie_file3)

    comedy_movie_directory = Directory('comedy')
    hulchul_file = File('hulchul')
    mrbean_file = File('Mr Bean')
    comedy_movie_directory.add(hulchul_file)
    comedy_movie_directory.add(mrbean_file)

    movie_directory.add(comedy_movie_directory)

    movie_directory.ls()
