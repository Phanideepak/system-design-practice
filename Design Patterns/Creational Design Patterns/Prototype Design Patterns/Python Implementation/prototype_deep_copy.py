import copy

class Prototype:
    def __init__(self, value):
        self.value = value
    
    def clone(self):
        return copy.deepcopy(self) # Deep Copy

original = Prototype([1, 2, 3, 4])

cloned = original.clone()

cloned.value += [9, 10, 11]


print(original.value)
print(cloned.value)
    
