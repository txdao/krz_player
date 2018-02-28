import pygame
import time
import random
file_dir = 'F:/KRZ/files/'
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
            print('When you left me\nMy heart was broken in two\nBut I patched it up\nAnd promised I would wait for you\n')
        elif m == 2:
            print('I never should have left you\non that awful day.\nI was happy then, until you stole my heart.\nand disappeared again.\n')
        elif m == 3:
            print()
    elif n == 2:
        if m == 1:
            print()
        elif m == 2:
            print('I never thought I\'d miss you\nbut I sorely did.\nI kept my hopes up\nwhen I should\'ve run and hid.\n')
        elif m == 3:
            print('As long as you were gone\nI knew I that I was free\nFree from certainty\nThat other loves could never be\n')
    elif n == 3:
        if m == 1:
            print()
        elif m == 2:
            print('There were months I wished\nyou\'d come back every day.\nBut you waited too long,\ndarlin\' it\'s too late.\nIt\'s too late.')
        elif m == 3:
            print('After the years I know\nThat I’m bound to my fate\nBecause you waited too long\nDarling, it’s too late\nIt’s too late')
    return

def print_chorus():
    print('It’s too late\nto love you now\nIt’s too late\nI’ve made my vow\n')
    return

def print_outro_verse():
    print('Another love came by\nAnd stole my heart away\nI wish that I could take it back\nIt’s too late\n')

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
    
    play_intro()
    time_start = time.clock()
    print('...')
    wait(time_start, 10)
    print('...')
    wait(time_start, 20)
    print('...')
    wait(time_start, 30)
    number = input('[1] When you left me ...\n[2] I never should have met you ...\n[3] I wish we\'d met before ...\nChoose: ')
    print(' ')
    if not (number == '1' or number == '2' or number == '3'):
        number = str(random.randint(1, 3))
    wait(time_start, 61.8)

    play_verse('1', number)
    time_start = time.clock()
    wait(time_start, 2)
    print_verse(1, number)
    wait(time_start, 31.6)

    play_chorus()
    wait(time_start, .5)
    print_chorus()
    time_start = time.clock()
    wait(time_start, 31.7)

    play_hold()
    time_start = time.clock()
    number = input('[1] The hurt you left behind ...\n[2] I never thought I\'d miss you ...\n[3] as long as you were gone ...\nChoose: ')
    print(' ')
    if not (number == '1' or number == '2' or number == '3'):
        number = str(random.randint(1, 3))
    wait(time_start, 13.9)
    
    play_verse(2, number)
    print_verse(2, number)
    time_start = time.clock()
    wait(time_start, 31.7)

    play_chorus_with_jam()
    time_start = time.clock()
    print_chorus()
    wait(time_start, 32)
    number = input('[1] I thought that somehow love would find a way ...\n[2] There were months I wished you\'d come back every day ...\n[3] After years I know that I\'m bound to my fate ...\nChoose: ')
    print(' ')
    if not (number == '1' or number == '2' or number == '3'):
        number = str(random.randint(1, 3))
    wait(time_start, 62.7)

    play_verse(3, number)
    time_start = time.clock()
    print_verse(3, number)
    wait(time_start, 31.7)

    play_outro()
    time_start = time.clock()
    print_chorus()
    wait(time_start, 31)
    print_outro_verse()
    wait(time_start, 100)

