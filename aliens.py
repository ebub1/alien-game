#!/usr/bin/env python3

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
        #Delete bullets when they out of the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
            print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
            
run_game()

