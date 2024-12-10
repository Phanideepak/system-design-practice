import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock: # Ensure thready safety access
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Usage

def test_singleton():
    s = Singleton()
    print(f"Instance: {id(s)}")


threads = [threading.Thread(target = test_singleton) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()