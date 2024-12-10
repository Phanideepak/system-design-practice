def singleton(cls):
    # Lifecycle of identifier depends on lifecycle of decorator.
    instances = {} # Key-value : class - It's instance

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Logger:
    def info(self, message):
        print(f'Logger info : {message}')
    
    def error(self, error_stack):
        print(f'Logger error: {error_stack}')

log1 = Logger()

log2 = Logger()

print(id(log1))
print(id(log2))

print(log1 is log2)

