from asciimatics.screen import Screen
import pygame
import time
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import SpeechBubble, Rainbow
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, PalmFirework
from termcolor import colored

pygame.mixer.init()
pygame.mixer.music.load("Fireworks with Sound Effects.mp3")
pygame.mixer.music.play()

from random import randint, choice
def thank_you(screen):
    ascii_art=r"""
                          _____     _   _       _        _   _        _  __        __   __    U  ___ u    _   _  
                         |_ " _|   |'| |'|  U  /"\  u   | \ |"|      |"|/ /        \ \ / /     \/"_ \/ U |"|u| | 
                           | |    /| |_| |\  \/ _ \/   <|  \| |>     | ' /          \ V /      | | | |  \| |\| | 
                          /| |\   U|  _  |u  / ___ \   U| |\  |u   U/| . \\u       U_|"|_u .-,_| |_| |   | |_| | 
                         u |_|U    |_| |_|  /_/   \_\   |_| \_|      |_|\_\          |_|    \_)-\___/   <<\___/  
                         _// \\_   //   \\   \\    >>   ||   \\,-. ,-,>> \\,-.   .-,//|(_        \\    (__) )(   
                        (__) (__) (_") ("_) (__)  (__)  (_")  (_/   \.)   (_/     \_) (__)      (__)       (__)  
  ____            _       _  __        _____     U  ___ u    _         _         U  ___ u               U _____ u    ____       ____     
 |___"\          /"|     |"|/ /       |" ___|     \/"_ \/   |"|       |"|         \/"_ \/  __        __ \| ___"|/ U |  _"\ u   / __"| u  
 U __) |       u | |u    | ' /       U| |_  u     | | | | U | | u   U | | u       | | | |  \"\      /"/  |  _|"    \| |_) |/  <\___ \/   
 \/ __/ \       \| |/  U/| . \\u     \|  _|/  .-,_| |_| |  \| |/__   \| |/__  .-,_| |_| |  /\ \ /\ / /\  | |___     |  _ <     u___) |   
 |_____|u  _     |_|     |_|\_\       |_|      \_)-\___/    |_____|   |_____|  \_)-\___/  U  \ V  V /  U |_____|    |_| \_\    |____/>>  
 <<  //   (")  _//<,-, ,-,>> \\,-.    )(\\,-        \\      //  \\    //  \\        \\    .-,_\ /\ /_,-. <<   >>    //   \\_    )(  (__) 
(__)(__)   "  (__)(_/   \.)   (_/    (__)(_/       (__)    (_")("_)  (_")("_)      (__)    \_)-'  '-(_/ (__) (__)  (__)  (__)  (__)      

"""
    colored_ascii_art= colored(ascii_art, 'red')
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              Rainbow(screen,SpeechBubble(colored_ascii_art)),
              y=screen.height - 30)
    ]
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)
    

Screen.wrapper(thank_you)