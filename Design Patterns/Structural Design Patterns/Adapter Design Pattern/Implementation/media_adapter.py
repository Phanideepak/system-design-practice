from abc import abstractmethod, ABC

# Existing Code.
# Media Player
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type, file_name):
        pass


# VLC Player abstract class
# Target Interface
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, file_name):
        pass
    
    @abstractmethod
    def play_mp4(self, file_name):
        pass

class VLCPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        print(f'Playing VLC File: {file_name}')
    
    def play_mp4(self, file_name):
        pass

class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        pass
    
    def play_mp4(self, file_name):
        print(f'Playing Mp4 File: {file_name}')


# Media Adapter takes old media player and adds vlc, mp4 functionality to it.
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
       if audio_type == 'vlc':
           self.__advanced_media_player = VLCPlayer()
       else:
           self.__advanced_media_player = Mp4Player()
    
    def play(self, audio_type, file_name):
        if audio_type == 'vlc':
            self.__advanced_media_player.play_vlc(file_name)
        else:
            self.__advanced_media_player.play_mp4(file_name)


class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.__mediaAdapter = None 
    
    def play(self, audio_type, file_name):
        if audio_type == 'mp3':
            print(f'Playing mp3 file: {file_name}')
        elif audio_type in ['mp4', 'vlc']:
            self.__mediaAdapter = MediaAdapter(audio_type)
            self.__mediaAdapter.play(audio_type, file_name)
        else:
            print('Invalid media format')

audio_player = AudioPlayer()
audio_player.play('mp3', 'beyond.mp3')
audio_player.play('vlc', 'dookudu.vlc')
audio_player.play('mp4', 'bluebird.mp4')
audio_player.play('avi', 'cinema.avi')