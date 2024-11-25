class Resource:
    def __init__(self):
        print('Creating a resource')

class ObjectPool:
    def __init__(self, create_instance, max_size = 10):
        self._create_instance = create_instance
        self._max_size = max_size
        self._available = []
        self._in_use = set()

    def acquire(self):
        if self._available:
            print('Picking object from available pool')
            obj = self._available.pop()
        elif len(self._in_use) < self._max_size:
            obj = self._create_instance()
        else:
            raise Exception('No objects available in the pool')
        
        self._in_use.add(obj)
        
        return obj
    
    def release(self, obj):
        if obj in self._in_use:
            print('releasing resource')
            self._in_use.remove(obj)
            self._available.append(obj)
    

pool = ObjectPool(Resource, max_size = 3)

 
resource1 = pool.acquire()
resource2 = pool.acquire()

pool.release(resource1)

resource3 = pool.acquire()
resource4 = pool.acquire()




        