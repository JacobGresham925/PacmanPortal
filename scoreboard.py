import pygame.font
from pygame.sprite import Group
from pacman import Pacman


class Scoreboard:

    def __init__(self, ai_settings, screen, maze, pacman):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.pacman = pacman
        self.maze = maze
        # self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.score_image = None
        self.score_rect = None
        self.high_score_image = None
        self.high_score_rect = None
        self.level_image = None
        self.level_rect = None
        self.ships = None
        self.pacmans = Group()

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_pacmans()

    def prep_score(self):
        rounded_score = int(round(self.ai_settings.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.pacmans.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.ai_settings.hs, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # Cetner the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.ai_settings.level), True,
                                            self.text_color, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_pacmans(self):
        """SHow how many ships are left."""
        self.pacmans = Group()
        for pacman_number in range(self.ai_settings.lives_left):
            pacman = Pacman(self.ai_settings, self.screen, self.maze)
            pacman.rect.x = 10 + pacman_number * pacman.rect.width
            pacman.rect.y = 10
            self.pacmans.add(pacman)
