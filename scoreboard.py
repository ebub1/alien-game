#!/usr/bin/env python3

import pygame.font

class Scoreboard():
    """Class to show game score"""
    def __init__(self,ai_settings, screen, stats):
        """Initialize attributes for counting score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #font settings
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)
        #preparing source image
        self.prep_score()

    def prep_score(self):
        """Preparing current score into image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        """Input score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)