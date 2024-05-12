#Setting and config file

class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """initialize the game setting"""
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Ship setting
        self.ship_speed_factor = 1.5
