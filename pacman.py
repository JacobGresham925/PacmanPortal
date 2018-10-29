
import pygame
from pygame.sprite import Sprite
import spritesheet
from ghosts import Ghosts
from time import sleep


class Pacman(Sprite):

    def __init__(self, ai_settings, screen, maze):
        """Initialize the ship and set its starting position."""
        super(Pacman, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.maze = maze
        self.size = 30
        self.ghosts = Ghosts(self.ai_settings, self.screen, self.maze, self)
        # Get ship from sprite sheet and load its image and rect.
        self.ss = spritesheet.Spritesheet('images/pacman.png')
        self.s1 = spritesheet.Spritesheet('images/pacmandeath.png')
        self.image = self.ss.image_at((0, 0, 16, 16), -1)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        # Initilize all pacman assets
        self.image4 = self.s1.image_at((0, 0, 16, 16), -1)
        self.image4 = pygame.transform.scale(self.image4, (self.size, self.size))
        self.image5 = self.s1.image_at((16, 0, 16, 16), -1)
        self.image5 = pygame.transform.scale(self.image5, (self.size, self.size))
        self.imageright1 = self.ss.image_at((0, 0, 16, 16), -1)
        self.imageright1 = pygame.transform.scale(self.imageright1, (self.size, self.size))
        self.imageright2 = self.ss.image_at((16, 0, 16, 16), -1)
        self.imageright2 = pygame.transform.scale(self.imageright2, (self.size, self.size))
        self.imageleft1 = self.ss.image_at((0, 16, 16, 16), -1)
        self.imageleft1 = pygame.transform.scale(self.imageleft1, (self.size, self.size))
        self.imageleft2 = self.ss.image_at((16, 16, 16, 16), -1)
        self.imageleft2 = pygame.transform.scale(self.imageleft2, (self.size, self.size))
        self.imageup1 = self.ss.image_at((0, 32, 16, 16), -1)
        self.imageup1 = pygame.transform.scale(self.imageup1, (self.size, self.size))
        self.imageup2 = self.ss.image_at((16, 32, 16, 16), -1)
        self.imageup2 = pygame.transform.scale(self.imageup2, (self.size, self.size))
        self.imagedown1 = self.ss.image_at((0, 48, 16, 16), -1)
        self.imagedown1 = pygame.transform.scale(self.imagedown1, (self.size, self.size))
        self.imagedown2 = self.ss.image_at((16, 48, 16, 16), -1)
        self.imagedown2 = pygame.transform.scale(self.imagedown2, (self.size, self.size))

        self.image3 = self.ss.image_at((32, 0, 16, 16), -1)
        self.image3 = pygame.transform.scale(self.image3, (self.size, self.size))
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.waka = pygame.mixer.Sound('sounds/waka.wav')
        self.intromus = pygame.mixer.Sound('sounds/intro.wav')
        self.dsound = pygame.mixer.Sound('sounds/death.wav')
        self.esound = pygame.mixer.Sound('sounds/eatghost.wav')
        self.dead = 0
        # Load the ship image and get its rect.
        # self.image = pygame.image.load('images/ship.bmp')
        # self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.tick = 0
        self.i = 0

    def update(self):
        """Update the ship's posisiton based on the movement flags."""
        # Update the ship's center value, not the rect.
        # Update rect object from self.center.
        if self.dead:
            self.dsound.play()
            self.image = self.image3
            self.screen.fill(self.ai_settings.bg_color)
            self.blitme()
            self.maze.blitme()
            pygame.display.flip()
            sleep(.1)
            self.image = self.imageright2
            self.screen.fill(self.ai_settings.bg_color)
            self.blitme()
            self.maze.blitme()
            pygame.display.flip()
            sleep(.1)
            self.image = self.image3
            self.screen.fill(self.ai_settings.bg_color)
            self.blitme()
            self.maze.blitme()
            pygame.display.flip()
            sleep(.1)
            self.image = self.image4
            self.screen.fill(self.ai_settings.bg_color)
            self.blitme()
            self.maze.blitme()
            pygame.display.flip()
            sleep(.1)
            self.image = self.image5
            self.screen.fill(self.ai_settings.bg_color)
            self.blitme()
            self.maze.blitme()
            pygame.display.flip()
            sleep(.1)
            self.dead = 0
            self.reset()
            self.ghosts.reset()
        else:
            if self.moving_right:
                if self.tick == 0:
                    self.image = self.imageright1
                if self.tick == 20:
                    self.image = self.imageright2
                if self.tick == 40:
                    self.image = self.image3
                self.tick += 1
                if self.tick == 60:
                    self.tick = 0
                self.centerx += self.ai_settings.pac_speed_factor
                # self.mr()

            if self.moving_left:
                if self.tick == 0:
                    self.image = self.imageleft1
                if self.tick == 20:
                    self.image = self.imageleft2
                if self.tick == 40:
                    self.image = self.image3
                self.tick += 1
                if self.tick == 60:
                    self.tick = 0
                self.centerx -= self.ai_settings.pac_speed_factor

            if self.moving_up:
                if self.tick == 0:
                    self.image = self.imageup1
                if self.tick == 20:
                    self.image = self.imageup2
                if self.tick == 40:
                    self.image = self.image3
                self.tick += 1
                if self.tick == 60:
                    self.tick = 0
                self.centery -= self.ai_settings.pac_speed_factor

            if self.moving_down:
                if self.tick == 0:
                    self.image = self.imagedown1
                if self.tick == 20:
                    self.image = self.imagedown2
                if self.tick == 40:
                    self.image = self.image3
                self.tick += 1
                if self.tick == 60:
                    self.tick = 0
                self.centery += self.ai_settings.pac_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def reset(self):
        self.rect.center = self.screen_rect.center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def intro(self):
        self.centerx = 40
        self.centery = 312
        # self.rect.left = self.screen_rect.right

    def introupdate(self):
        if self.ai_settings.intro:
            if self.ai_settings.powerpill:
                self.moving_right = True
                self.centerx += 0.5
                if pygame.Rect.colliderect(self.rect, self.ghosts.powerpill_rect) or self.rect.centerx > 680:
                    self.ghosts.powerpill_rect.centerx = -100
                    self.ai_settings.powerpill = False
            if not self.ai_settings.powerpill:
                self.moving_left = True
                self.moving_right = False
                self.centerx -= 0.5
                if self.rect.centerx < 0:
                    self.ai_settings.introduction = 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def mr(self):
        self.centerx += self.ai_settings.pac_speed_factor

    def ml(self):
        self.centerx -= self.ai_settings.pac_speed_factor

    def mu(self):
        self.centery -= self.ai_settings.pac_speed_factor

    def md(self):
        self.centery += self.ai_settings.pac_speed_factor

    def die(self): pass
