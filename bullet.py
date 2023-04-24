import pygame
from pygame import Sprite
class Bullet(Sprite):
    """Class for bullets control"""
    def __init__(self,ai_settings, screen,ship):
        """Create bullet object and set right position"""
        super(Bullet,self).__init__()
        self.screen = screen
        """Create bullet in  position(0,0) and apply right position"""
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Bullet position saving in real format
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

