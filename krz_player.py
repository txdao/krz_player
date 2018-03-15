#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import time
import random
file_dir = ''
pygame.mixer.init()

def play(file):
    song = pygame.mixer.Sound(file)
    song.set_volume(1)
    song.play()
    # print('playing ' + file)
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

def print_verse(n, m_string):
    m = int(m_string)
    if n == 1:
        if m == 1:
            print('When you left me,\nmy heart was broken in two.\nBut I patched it up,\nand promised I would wait for you\n')
        elif m == 2:
            print('I never should have left you\non that awful day.\nI was happy then, until you stole my heart.\nand disappeared again.\n')
        elif m == 3:
            print('I wish we\'d met\nbefore I ever learned to cry.\nWhen someone loved me briefly,\nand the said goodbye.\n')
    elif n == 2:
        if m == 1:
            print('The hurt you left behind\nwould truly never heal.\nA hole where my heart knew\nthere should be something real.\n')
        elif m == 2:
            print('I never thought I\'d miss you\nbut I sorely did.\nI kept my hopes up\nwhen I should\'ve run and hid.\n')
        elif m == 3:
            print('As long as you were gone\nI knew I that I was free\nFree from certainty\nthat other loves could never be\n')
    elif n == 3:
        if m == 1:
            print('In time I thought that\nsomehow love would find a way.\nBut you waited too long,\ndarlin\' it\'s too late.\nIt\'s too late.\n')
        elif m == 2:
            print('There were months I wished\nyou\'d come back every day.\nBut you waited too long,\ndarlin\' it\'s too late.\nIt\'s too late.\n')
        elif m == 3:
            print('After the years I know\nThat I’m bound to my fate\nBecause you waited too long\nDarling, it’s too late\nIt’s too late\n')
    return

def print_chorus():
    print('It’s too late\nto love you now.\nIt’s too late.\nI’ve made my vow.\n')
    return

def print_outro_verse():
    print('Another love came by,\nAnd stole my heart away.\nI wish that I could take it back,\nIt’s too late.\n')

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
    return time.time() - start_time

def wait(start_time, length):
    while elapsed_time(time_start) < length:
        continue


if __name__ == "__main__":
    
    play_intro()
    time_start = time.time()
    print('...')
    wait(time_start, 10)
    print('...')
    wait(time_start, 20)
    print('...')
    wait(time_start, 30)
    number = input('\n[1] When you left me ...\n[2] I never should have met you ...\n[3] I wish we\'d met before ...\nChoose: ')
    print(' ')
    if not (number == '1' or number == '2' or number == '3'):
        number = str(random.randint(1, 3))
    wait(time_start, 61.7355)

    play_verse('1', number)
    time_start = time.time()
    wait(time_start, 2)
    print_verse(1, number)
    wait(time_start, 31.75)

    play_chorus()
    time_start = time.time()
    wait(time_start, .5)
    print_chorus()
    wait(time_start, 31.89)

    play_hold()
    time_start = time.time()
    number = input('[1] The hurt you left behind ...\n[2] I never thought I\'d miss you ...\n[3] As long as you were gone ...\nChoose: ')
    print(' ')
    if not (number == '1' or number == '2' or number == '3'):
        number = str(random.randint(1, 3))
    wait(time_start, 15.785)
    
    play_verse(2, number)
    print_verse(2, number)
    time_start = time.time()
    wait(time_start, 31.727)

    play_chorus_with_jam()
    time_start = time.time()
    print_chorus()
    wait(time_start, 32.5)
    number = input('[1] I thought that somehow love would find a way ...\n[2] There were months I wished you\'d come back every day ...\n[3] After years I know that I\'m bound to my fate ...\nChoose: ')
    print(' ')
    if not (number == '1' or number == '2' or number == '3'):
        number = str(random.randint(1, 3))
    wait(time_start, 63.685)

    play_verse(3, number)
    time_start = time.time()
    print_verse(3, number)
    wait(time_start, 31.62)

    play_outro()
    time_start = time.time()
    print_chorus()
    wait(time_start, 31)
    print_outro_verse()
    wait(time_start, 60)
    print('END')
    wait(time_start, 101)
    

