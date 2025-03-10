from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import SpeechBubble, Rainbow
from termcolor import colored
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
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)
    

Screen.wrapper(thank_you)