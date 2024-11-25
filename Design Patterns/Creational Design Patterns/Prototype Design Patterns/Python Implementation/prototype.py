import copy

class Prototype:
    def __init__(self, value):
        self.value = value
    
    def clone(self):
        return copy.copy(self) # Shallow Copy

original = Prototype([1, 2, 3, 4])

cloned = original.clone()

cloned.value += [5,6,7,8,9,10]

print(original.value)
print(cloned.value)
    
