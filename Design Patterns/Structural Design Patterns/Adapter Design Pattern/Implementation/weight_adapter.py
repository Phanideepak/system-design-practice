from abc import ABC, abstractmethod

# Adaptee Interface
class WeightMachine(ABC):
    @abstractmethod
    def get_weight_in_pound(self):
        pass 

# Adaptee Class
class WeightMachineForBabies(WeightMachine):
    def get_weight_in_pound(self):
        return 28


# Adapter Class
class WeightMachineAdapter(ABC):
    @abstractmethod
    def get_weight_in_kg(self):
        pass


# Concrete Adapter Class implements interface
class WeightMachineAdapterImpl(WeightMachineAdapter):
    def __init__(self, weight_machine):
        self.__weight_machine = weight_machine
    
    def get_weight_in_kg(self):
        weight_in_pounds = self.__weight_machine.get_weight_in_pound()

        return weight_in_pounds * 0.45


# Client Code
weight_machine_adapter = WeightMachineAdapterImpl(WeightMachineForBabies())

print(weight_machine_adapter.get_weight_in_kg())
