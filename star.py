#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite
class Star(Sprite):
    """Class representing one star"""
    def __init__(self,ai_settings,screen):
        #Initiating alien ship and it's start position
        super(Star, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #Downloading the star and initiating a rectangle
        self.image=pygame.image.load('star.png')
        self.rect=self.image.get_rect()
        #Every new alien ship appears in on the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #Save exact alien position 
        self.x=float(self.rect.x)
        
    def blitme(self):
        '''Drawing the alien ship in current position'''
        self.screen.blit(self.image,self.rect)

