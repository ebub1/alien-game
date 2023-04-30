#!/usr/bin/env python3

from typing import Any
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Class representing one alien ship"""
    def __init__(self,ai_settings,screen):
        #Initiating alien ship and it's start position
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #Downloading the alien ship and initiating a rectangle
        self.image=pygame.image.load('alien.png')
        self.rect=self.image.get_rect()
        #Every new alien ship appears in on the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #Save exact alien position 
        self.x=float(self.rect.x)
    def check_edges(self):
        """Retern True if alien near edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """Move alien ship to the right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def blitme(self):
        '''Drawing the alien ship in current position'''
        self.screen.blit(self.image,self.rect)

