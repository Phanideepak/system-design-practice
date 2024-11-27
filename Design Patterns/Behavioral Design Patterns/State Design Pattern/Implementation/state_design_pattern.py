from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def handle_request(self, context):
        pass

# Concrete State
class GreenLight(TrafficLightState):
    def handle_request(self, context):
        print('Green Light: Go')
        context.set_state(YellowLight())

# Concrete State
class YellowLight(TrafficLightState):
    def handle_request(self, context):
        print('Yellow Light: Prepare to Stop.')
        context.set_state(RedLight())


# Concrete State
class RedLight(TrafficLightState):
    def handle_request(self, context):
        print('Red Light: Stop')
        context.set_state(GreenLight())


# Context
class TrafficLight:
    def __init__(self):
        self._state = RedLight()
    
    def set_state(self, state):
        self._state = state
    
    def request(self):
        self._state.handle_request(self)


# Client Code
traffic_light = TrafficLight()

for i in range(6):
    traffic_light.request()
