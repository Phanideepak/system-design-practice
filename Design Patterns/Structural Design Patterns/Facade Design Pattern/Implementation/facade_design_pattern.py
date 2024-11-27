### Example in Code (Python):
'''
Imagine a scenario where we have a home theater system with several components, like a DVD player, projector, and sound system. Interacting with each component separately can be complex. A **Facade** can simplify this
 by providing a unified interface to start the whole system.
'''

class DVDPlayer:
    def on(self):
        print('DVD Player is now on')
    
    def play(self):
        print('DVD Player is playing movie')

    def stop(self):
        print('DVD Player has stopped')
    
    def off(self):
        print('DVD Player is now off')

class Projector:
    def on(self):
        print('Projector is now on')
    
    def set_input(self):
        print('Project input is now set to dvd')
    
    def off(self):
        print('Projector is now off')

class SoundSystem:
    def on(self):
        print('Sound system is now on')
    
    def set_volume(self):
        print('Sound system volume set')
    
    def off(self):
        print('Sound system is now off')


class HomeTheatreFacade:
    def __init__(self, dvd_player, projector, sound_system):
        self.__dvd_player : DVDPlayer = dvd_player
        self.__projector : Projector = projector
        self.__sound_system : SoundSystem = sound_system

    def watch_movie(self):
        print('Get ready to watch the movie')
        self.__projector.on()
        self.__projector.set_input()
        self.__sound_system.on()
        self.__sound_system.set_volume()
        self.__dvd_player.on()
        self.__dvd_player.play()
    
    def end_movie(self):
        print('Shutting down home theatre')
        self.__dvd_player.stop()
        self.__dvd_player.off()
        self.__sound_system.off()
        self.__projector.off()


dvd_player = DVDPlayer()
projector = Projector()
sound_system = SoundSystem()

home_theatre = HomeTheatreFacade(dvd_player, projector, sound_system)

home_theatre.watch_movie()

home_theatre.end_movie()