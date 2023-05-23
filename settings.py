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
        self.ship_limit = 3
        #bullet parameters
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 250, 250, 250
        self.bullets_allowed = 3
        #aliens parameters
        self.fleet_drop_speed = 50
        #temp speed up 
        self.speedup_scale = 1.2
        self.score_scale = 1.2
        self.initialize_dynamic_settings()
        self.alien_points = 1000
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        #fleet direction =1 moving to the right if -1 to the left
        self.fleet_direction = 1
       
    def increase_speed(self):
        """"Set speed up settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)