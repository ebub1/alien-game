#!/usr/bin/env python3

class GameStat():
    """Counting of statiscic for Aliens game"""
    def __init__(self, ai_settings):
        """Initializing statistic"""
        self.ai_settings = ai_settings
        self.reset_stat()
        #Game starts when flag is active
        self.game_active = False
        #Record must not reset
        self.high_score = 0
    def reset_stat(self):
        """Initializing statistic which change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1