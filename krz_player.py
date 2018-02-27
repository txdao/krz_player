import pygame
import time
file_dir = 'F:/KRZ/files/'
pygame.mixer.init()

def play(file):
    song = pygame.mixer.Sound(file)
    song.set_volume(1)
    song.play()
    print(file)
    return song

def loop():
    pass

def wait_for_input():
    pass

def play_intro():
    return play(file_dir + 'JunebugIntro_v2.ogg')

def play_chorus():
    pass

def play_verse(n, m):
    return play(file_dir + 'JUNEBUG Verse {} Option {}.ogg'.format(n, m))

def play_outro():
    pass

def play_vamp():
    pass

def play_hold():
    pass

def display_text():
    pass



if __name__ == "__main__":
    intro = play_intro()
    number = input('1, 2, 3? ')
    play_verse('1', number)