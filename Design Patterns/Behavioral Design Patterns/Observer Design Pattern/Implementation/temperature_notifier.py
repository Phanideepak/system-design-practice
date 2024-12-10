from abc import abstractmethod, ABC


# Observer abstract class
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass



# Subject abstract class
class Subject(ABC):
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, temperature):
        for observer in self._observers:
            observer.update(temperature)


# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
    
    def set_temperature(self, temperature):
        print(f'Weather Station: New Temperature is {temperature}°C')
        self._temperature = temperature
        self.notify(temperature)


# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f'Phone Display : Temperature updated to {temperature}°C')

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f'Window Display : Temperature updated to {temperature}°C')


# Client Code
if __name__ == '__main__':
    # Create subject
    weather_station= WeatherStation()

    # Create Observers
    phone_display = PhoneDisplay()
    window_display = WindowDisplay()

    # Attach observers to subject
    weather_station.attach(phone_display)
    weather_station.attach(window_display)

    # Change temperature and notify observers
    weather_station.set_temperature(29)
    weather_station.set_temperature(30)

    # Detach an observer and update again
    weather_station.detach(phone_display)
    weather_station.set_temperature(32)
