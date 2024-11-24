import javax.print.attribute.standard.Media;

interface MediaPlayer{
    void play(String audioType, String fileName);
}

interface AdvancedMediaPlayer{
    void playVLC(String fileName);
    void playMp4(String fileName);
}

class VLCPlayer implements AdvancedMediaPlayer{
    @Override
    public void playVLC(String fileName) {
        System.out.println("Playing VLC File "+ fileName);
    }

    @Override
    public void playMp4(String fileName) {
    }
}

class Mp4Player implements AdvancedMediaPlayer{

    @Override
    public void playVLC(String fileName) {
    }

    @Override
    public void playMp4(String fileName) {
        System.out.println("Playing Mp4 File "+ fileName);
    }
}

class MediaAdapter implements MediaPlayer{
    private AdvancedMediaPlayer advancedMediaPlayer;
    public MediaAdapter(String audioType){
        if(audioType.equalsIgnoreCase("vlc")){
            advancedMediaPlayer = new VLCPlayer();
        }
        else if(audioType.equalsIgnoreCase("mp4")){
            advancedMediaPlayer = new Mp4Player();
        }
    }
    @Override
    public void play(String audioType, String fileName) {
        if(audioType.equalsIgnoreCase("vlc")){
            advancedMediaPlayer.playVLC(fileName);
        }
        else if(audioType.equalsIgnoreCase("mp4")){
            advancedMediaPlayer.playMp4(fileName);
        }
    }
}

class AudioPlayer implements MediaPlayer{

    MediaAdapter mediaAdapter;

    @Override
    public void play(String audioType, String fileName) {
        if(audioType.equalsIgnoreCase("mp3")){
            System.out.println("Playing mp3 file "+ fileName);
        } else if(audioType.equalsIgnoreCase("mp4") || audioType.equalsIgnoreCase("vlc")){
            mediaAdapter = new MediaAdapter(audioType);
            mediaAdapter.play(audioType, fileName);
        } else {
            System.out.println("Invalid media format");
        }
    }
}

public class AdapterDesignDemo {
    public static void main(String[] args) {
        AudioPlayer audioPlayer = new AudioPlayer();
        audioPlayer.play("mp3", "beyond the horizon.mp3");
        audioPlayer.play("mp4", "alone.mp4");
        audioPlayer.play("vlc", "far far away.vlc");
        audioPlayer.play("avi", "mind me.avi");
    }
}
