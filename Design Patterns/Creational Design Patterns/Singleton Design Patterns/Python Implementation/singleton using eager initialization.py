class Singleton:
    __instance = None 

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

if __name__ == '__main__':
    s1 = Singleton()

    s2 = Singleton()
    
    print(id(s1)) # id of the object 
    print(id(s2)) # id of the object

    print(s1 is s2)