class Settings:
    """Class for storage all settings"""
    def __init__(self):
        """INITIAL game settings"""
        #screen setting
        self.screen_width=1200
        self.screen_height=750
        self.bg_colour=(0,0,70)
        self.ship_speed_factor=1.5
        #bullet parameters
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

    