import sys
import pygame
from settings import Settings
from ship import Ship
from naruto import Naruto 
import game_function as gf
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship=Ship(ai_settings,screen)
    naruto=Naruto(screen)
    pygame.display.set_caption("Alien invasion")
    while True:
        gf.check_ivents(ship)
        gf.update_screen(ai_settings,screen,ship,naruto)
        ship.update()
        
run_game()

