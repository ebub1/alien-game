#!/usr/bin/env python3

import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #Set button's size and parameters
        self.width, self.height = 200, 50
        self.button_color =(0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #Build object button's rect and put it on center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #Create message only one time
        self.prep_msg(msg)
    def prep_msg(self, msg):
        """Prepare msg to rect and put it on center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        """Draw an empty button and show the msg"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)