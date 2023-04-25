import sys
import pygame
from settings import Settings
from ship import Ship
from naruto import Naruto 
import game_function as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #creating a ship
    ship=Ship(ai_settings,screen)
    #creating a group to store bullets
    bullets = Group()
    naruto=Naruto(screen)
    pygame.display.set_caption("Alien invasion")
    #Start main cycle of the game
    while True:
        gf.check_events(ai_settings,screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()

