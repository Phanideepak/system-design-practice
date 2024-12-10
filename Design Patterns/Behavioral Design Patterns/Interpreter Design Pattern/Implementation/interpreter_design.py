from abc import abstractmethod, ABC

class Context:    
    def __init__(self):
        self.__context_map = dict()

    def put(self, str_val, int_val):
       self.__context_map[str_val] = int_val

    def get(self, str_val):
        return self.__context_map[str_val]

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(context):
        pass


class NumberTerminalExpression(AbstractExpression):
    def __init__(self, string_val):
        self.string_val = string_val
    
    def interpret(self, context):
        return context.get(self.string_val)

class MultiplyNonTerminalExpression(AbstractExpression):
    def __init__(self, leftExpression, rightExpression):
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression
    
    def interpret(self, context):
        return self.leftExpression.interpret(context) * self.rightExpression.interpret(context)



# Client Code
context = Context()
context.put('a', 2)
context.put('b', 10)

expression1 = MultiplyNonTerminalExpression(NumberTerminalExpression('a'), NumberTerminalExpression('b'))

print(expression1.interpret(context))