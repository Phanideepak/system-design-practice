class Singleton:
    _instance = None

    def __init__(self):
        if not hasattr(self, 'initialized'):
            print('Initializing Singleton instance')
            self.initalized = True
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()

        return cls._instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 is s2)
