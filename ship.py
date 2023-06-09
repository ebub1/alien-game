#!/usr/bin/env python3
import pygame
from pygame.sprite import Sprite

class Ship():
    def __init__(self,ai_settings,screen):
        self.ai_settings=ai_settings
        #initiating ship and it's start position
        self.screen=screen
        #downloading the ship and initiating a rectangle
        self.image=pygame.image.load('ship2.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #every new ship appears in on the rigt of screenbottom
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        #flags for movings
        self.moving_right=False
        self.moving_left=False
    def center_ship(self):
        """Put ship in the center"""
        self.center = self.screen_rect.centerx
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
    def blitme(self):
        '''Drawing the ship in current position'''
        self.screen.blit(self.image,self.rect)

class Ship_live(Sprite):
    def __init__(self,screen):
        super(Ship_live, self).__init__()
        self.screen=screen
        #downloading the ship live image and initiating a rectangle
        self.image = pygame.image.load('ship_live.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    def blitme(self):
        '''Drawing the ship live in current position'''
        self.screen.blit(self.ship_live_image, self.rect)
