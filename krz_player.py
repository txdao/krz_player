import pygame
import time
import random
file_dir = 'F:/KRZ/files/'
pygame.mixer.init()

def play(file):
    song = pygame.mixer.Sound(file)
    song.set_volume(1)
    song.play()
    print('playing ' + file)
    return song

def loop():
    pass

def wait_for_input():
    pass

def play_intro():
    play(file_dir + 'JunebugIntro_v2.ogg')

def play_chorus():
    play(file_dir + 'JUNEBUG Chorus 1.ogg')

def play_chorus_with_jam():
    play(file_dir + 'JUNEBUG Chorus 2 with jam section.ogg')

def play_verse(n, m):
    play(file_dir + 'JUNEBUG Verse {} Option {}.ogg'.format(n, m))

def play_outro():
    play(file_dir + 'JUNEBUG Last Chorus and outro.ogg')

def play_vamp():
    pass

def play_hold():
    hold = random.randint(1, 3)
    play(file_dir + 'JUNEBUG Hold loop {}.ogg'.format(hold))
    pass

def display_text():
    pass

def elapsed_time(start_time):
    return time.clock() - start_time

def wait(start_time, length):
    while elapsed_time(time_start) < length:
        continue


if __name__ == "__main__":
    
    # play_intro()
    # time_start = time.clock()
    # number = input('1, 2, 3? ')
    # wait(time_start, 61.8)

    # play_verse('1', number)
    # time_start = time.clock()
    # wait(time_start, 31.6)

    # play_chorus()
    # time_start = time.clock()
    # wait(time_start, 31.7)

    # play_hold()
    # time_start = time.clock()
    # number = input('1, 2, 3? ')
    # wait(time_start, 13.9)
    
    # play_verse(2, number)
    # time_start = time.clock()
    # wait(time_start, 31.7)

    # play_chorus_with_jam()
    # time_start = time.clock()
    number = input('1, 2, 3? ')
    # wait(time_start, 61.7)

    play_verse(3, number)
    time_start = time.clock()
    wait(time_start, 31.7)

    play_outro()
    time_start = time.clock()
    wait(time_start, 100)

