from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        return f'logging to file: {message}'

class ConsoleLogger(Logger):
    def log(self, message):
        return f'logging to console: {message}'

class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        else:
            raise ValueError('Unknown logger type')

logger = LoggerFactory.create_logger('file')

print(logger.log('File has been saved'))