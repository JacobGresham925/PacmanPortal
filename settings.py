class Settings:
    """Class to sore all settings for game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Placeholder
        self.ph = 0

        # speed of pacman
        self.pac_speed_factor = 0.5
        self.game_active = False
        self.hs = 0
        self.shs = False
        self.intro = True
        self.powerpill = True
        self.blueghost = False
        self.introduction = 0
        self.bluetick = 0
        self.score = 0
        self.lives_left = 3
        self.level = 1
