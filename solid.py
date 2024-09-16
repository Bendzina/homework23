# დავალება 1.

# შექმენით მედია ფლეიერის აპლიკაცია. განსაზღვრეთ 
# ინტერფეისები დაკვრის, პაუზის, გაჩერების, გადახვევის 
# და სწრაფი წინსვლის ფუნქციებისთვის. განახორციელეთ 
# კლასები აუდიო პლეერისთვის, ვიდეო პლეერისთვის და 
# სტრიმინგის პლეერისთვის. დარწმუნდით, რომ თითოეული 
# მოთამაშე ახორციელებს მხოლოდ მის ფუნქციონალურ 
# ინტერფეისებს. მაქსიმალურად გამოიყენეთ SOLID პრინციპები!!!

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Pauseble(ABC):
    @abstractmethod
    def pause(self):
        pass
class Rewindable(ABC):
    @abstractmethod
    def rewind(self):
        pass

class FastForwardable(ABC):
    @abstractmethod
    def fast_forward(self):
        pass

#audioplayer
class AudioPlayer(MediaPlayer, Pauseble, Rewindable, FastForwardable):
    def play(self):
        print("Audio playing...")

    def stop(self):
        print("Audio stopped...")

    def pause(self):
        print("Audio paused...")
    def rewind(self):
        print("Audio rewinded...")
    def fast_forward(self):
        print("Audio fast forwarded...")


    # video player


class VideoPlayer(MediaPlayer, Pauseble, Rewindable, FastForwardable):

    def play(self):
        print("Video playing...")
    def stop(self):
        print("Video stopped...")
    def pause(self):
        print("Video paused...")
    def rewind(self):
        print("Video rewinded...")
    def fast_forward(self):
        print("Video fast forwarded...")


#streaming player

class StreamingPlayer(MediaPlayer, Pauseble):
    def play(self):
        print("Streaming playing...")
    def stop(self):
        print("Streaming stopped...")
    def pause(self):
        print("Streaming paused...")

#გამოვიყენოთ პლეიერი
def play_media(player: MediaPlayer):
    player.play()
    player.stop()

def constor_media(player):
    if isinstance(player, Pauseble):
        player.pause()
    if isinstance(player, Rewindable):
        player.rewind()
    if isinstance(player, FastForwardable):
        player.fast_forward()
audio_player = AudioPlayer()
video_player = VideoPlayer()
streaming_player = StreamingPlayer()

print ("\n --Audio Player")
play_media(audio_player)
constor_media(audio_player)

print ("\n --Video Player")
play_media(video_player)
constor_media(video_player)

print ("\n --Streaming Player")
play_media(streaming_player)
constor_media(streaming_player)