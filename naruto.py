import pygame
class Naruto:
    def __init__(self,screen):
        #initiating naruto and it's start position
        self.screen=screen
        #downloading the image and initiating a rectangle
        self.image=pygame.image.load('naruto2.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #every new ship appears in on the rigt of screenbottom
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
    def blitme(self):
        '''Drawing the naruto in current position'''
        self.screen.blit(self.image,self.rect)

