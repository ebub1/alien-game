#!/usr/bin/env python3

import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien 
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStat
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #creating a ship
    ship=Ship(ai_settings,screen)
    #creating a group to store bullets
    bullets = Group()
    #creating star group
    stars = Group()
    gf.create_sky(ai_settings, screen, stars)
    #Creating fleet
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship, aliens)
    pygame.display.set_caption("Alien invasion")
    #Creating examle to storage statistic
    stats = GameStat(ai_settings)
    #Start main cycle of the game
    while True:
        gf.check_events(ai_settings,screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings,stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stars, ship, aliens, bullets)
            
run_game()