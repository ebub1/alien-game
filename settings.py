#!/usr/bin/env python3

class Settings:
    """Class for storage all settings"""
    def __init__(self):
        """INITIAL game settings"""
        #screen setting
        self.screen_width=1200
        self.screen_height=750
        self.bg_colour=(5,19,38)
        #ship parametrs
        self.ship_speed_factor=1.5
        self.ship_limit = 3
        #bullet parameters
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 250, 250
        self.bullets_allowed = 3
        #aliens parameters
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction =1 moving to the right if -1 to the left
        self.fleet_direction = 1

    