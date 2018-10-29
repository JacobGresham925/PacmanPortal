
import pygame
from pygame.sprite import Sprite
import spritesheet
from button import Button


class Ghosts(Sprite):

    def __init__(self, ai_settings, screen, maze, pacman):
        """Initialize the ship and set its starting position."""
        super(Ghosts, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.maze = maze
        self.size = 30
        self.pacman = pacman
        # Get ship from sprite sheet and load its image and rect.
        self.bl = spritesheet.Spritesheet('images/blinky.png')
        self.cl = spritesheet.Spritesheet('images/clyde.png')
        self.pi = spritesheet.Spritesheet('images/pinky.png')
        self.ink = spritesheet.Spritesheet('images/inky.png')

        # Blinky setup
        self.blinky1a = self.bl.image_at((0, 0, 16, 16), -1)
        self.blinky1a = pygame.transform.scale(self.blinky1a, (self.size, self.size))
        self.blinky1b = self.bl.image_at((16, 0, 16, 16), -1)
        self.blinky1b = pygame.transform.scale(self.blinky1b, (self.size, self.size))
        self.blinky2a = self.bl.image_at((0, 16, 16, 16), -1)
        self.blinky2a = pygame.transform.scale(self.blinky2a, (self.size, self.size))
        self.blinky2b = self.bl.image_at((16, 16, 16, 16), -1)
        self.blinky2b = pygame.transform.scale(self.blinky2b, (self.size, self.size))
        self.blinky3a = self.bl.image_at((0, 32, 16, 16), -1)
        self.blinky3a = pygame.transform.scale(self.blinky3a, (self.size, self.size))
        self.blinky3b = self.bl.image_at((16, 32, 16, 16), -1)
        self.blinky3b = pygame.transform.scale(self.blinky3b, (self.size, self.size))
        self.blinky4a = self.bl.image_at((0, 48, 16, 16), -1)
        self.blinky4a = pygame.transform.scale(self.blinky4a, (self.size, self.size))
        self.blinky4b = self.bl.image_at((16, 48, 16, 16), -1)
        self.blinky4b = pygame.transform.scale(self.blinky4b, (self.size, self.size))

        # inky setup
        self.inky1a = self.ink.image_at((0, 0, 16, 16), -1)
        self.inky1a = pygame.transform.scale(self.inky1a, (self.size, self.size))
        self.inky1b = self.ink.image_at((16, 0, 16, 16), -1)
        self.inky1b = pygame.transform.scale(self.inky1b, (self.size, self.size))
        self.inky2a = self.ink.image_at((0, 16, 16, 16), -1)
        self.inky2a = pygame.transform.scale(self.inky2a, (self.size, self.size))
        self.inky2b = self.ink.image_at((16, 16, 16, 16), -1)
        self.inky2b = pygame.transform.scale(self.inky2b, (self.size, self.size))
        self.inky3a = self.ink.image_at((0, 32, 16, 16), -1)
        self.inky3a = pygame.transform.scale(self.inky3a, (self.size, self.size))
        self.inky3b = self.ink.image_at((16, 32, 16, 16), -1)
        self.inky3b = pygame.transform.scale(self.inky3b, (self.size, self.size))
        self.inky4a = self.ink.image_at((0, 48, 16, 16), -1)
        self.inky4a = pygame.transform.scale(self.inky4a, (self.size, self.size))
        self.inky4b = self.ink.image_at((16, 48, 16, 16), -1)
        self.inky4b = pygame.transform.scale(self.inky4b, (self.size, self.size))

        # pinky setup
        self.pinky1a = self.pi.image_at((0, 0, 16, 16), -1)
        self.pinky1a = pygame.transform.scale(self.pinky1a, (self.size, self.size))
        self.pinky1b = self.pi.image_at((16, 0, 16, 16), -1)
        self.pinky1b = pygame.transform.scale(self.pinky1b, (self.size, self.size))
        self.pinky2a = self.pi.image_at((0, 16, 16, 16), -1)
        self.pinky2a = pygame.transform.scale(self.pinky2a, (self.size, self.size))
        self.pinky2b = self.pi.image_at((16, 16, 16, 16), -1)
        self.pinky2b = pygame.transform.scale(self.pinky2b, (self.size, self.size))
        self.pinky3a = self.pi.image_at((0, 32, 16, 16), -1)
        self.pinky3a = pygame.transform.scale(self.pinky3a, (self.size, self.size))
        self.pinky3b = self.pi.image_at((16, 32, 16, 16), -1)
        self.pinky3b = pygame.transform.scale(self.pinky3b, (self.size, self.size))
        self.pinky4a = self.pi.image_at((0, 48, 16, 16), -1)
        self.pinky4a = pygame.transform.scale(self.pinky4a, (self.size, self.size))
        self.pinky4b = self.pi.image_at((16, 48, 16, 16), -1)
        self.pinky4b = pygame.transform.scale(self.pinky4b, (self.size, self.size))

        # clyde setup
        self.clyde1a = self.cl.image_at((0, 0, 16, 16), -1)
        self.clyde1a = pygame.transform.scale(self.clyde1a, (self.size, self.size))
        self.clyde1b = self.cl.image_at((16, 0, 16, 16), -1)
        self.clyde1b = pygame.transform.scale(self.clyde1b, (self.size, self.size))
        self.clyde2a = self.cl.image_at((0, 16, 16, 16), -1)
        self.clyde2a = pygame.transform.scale(self.clyde2a, (self.size, self.size))
        self.clyde2b = self.cl.image_at((16, 16, 16, 16), -1)
        self.clyde2b = pygame.transform.scale(self.clyde2b, (self.size, self.size))
        self.clyde3a = self.cl.image_at((0, 32, 16, 16), -1)
        self.clyde3a = pygame.transform.scale(self.clyde3a, (self.size, self.size))
        self.clyde3b = self.cl.image_at((16, 32, 16, 16), -1)
        self.clyde3b = pygame.transform.scale(self.clyde3b, (self.size, self.size))
        self.clyde4a = self.cl.image_at((0, 48, 16, 16), -1)
        self.clyde4a = pygame.transform.scale(self.clyde4a, (self.size, self.size))
        self.clyde4b = self.cl.image_at((16, 48, 16, 16), -1)
        self.clyde4b = pygame.transform.scale(self.clyde4b, (self.size, self.size))

        # Death setup
        self.eye = spritesheet.Spritesheet('images/eyes.png')
        self.eyes1 = self.eye.image_at((0, 0, 16, 16), -1)
        self.eyes1 = pygame.transform.scale(self.eyes1, (self.size, self.size))
        self.eyes2 = self.eye.image_at((0, 16, 16, 16), -1)
        self.eyes2 = pygame.transform.scale(self.eyes2, (self.size, self.size))
        self.eyes3 = self.eye.image_at((0, 32, 16, 16), -1)
        self.eyes3 = pygame.transform.scale(self.eyes3, (self.size, self.size))
        self.eyes4 = self.eye.image_at((0, 48, 16, 16), -1)
        self.eyes4 = pygame.transform.scale(self.eyes4, (self.size, self.size))

        self.blueghost = pygame.image.load('images/blueghost.png')
        self.blueghost = pygame.transform.scale(self.blueghost, (self.size, self.size))

        self.powerpill = pygame.image.load('images/powerpill.png')
        self.powerpill_rect = self.powerpill.get_rect()

        self.blimage = self.blinky1a
        self.inkimage = self.inky1a
        self.piimage = self.pinky1a
        self.climage = self.clyde1a
        self.blrect = self.blimage.get_rect()
        self.inkrect = self.inkimage.get_rect()
        self.pirect = self.piimage.get_rect()
        self.clrect = self.climage.get_rect()
        # Initilize all pacman assets

        self.screen = screen
        self.screen_rect = screen.get_rect()
        # self.rect.center = self.screen_rect.center
        self.blrect.center = (280, 312)
        self.inkrect.center = (250, 312)
        self.pirect.center = (310, 312)
        self.clrect.center = (340, 312)

        self.bldead = 0
        self.pidead = 0
        self.inkdead = 0
        self.cldead = 0
        # Load the ship image and get its rect.
        # self.image = pygame.image.load('images/ship.bmp')
        # self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.blcenterx = float(self.blrect.centerx)
        self.blcentery = float(self.blrect.centery)
        self.inkcenterx = float(self.inkrect.centerx)
        self.inkcentery = float(self.inkrect.centery)
        self.picenterx = float(self.pirect.centerx)
        self.picentery = float(self.pirect.centery)
        self.clcenterx = float(self.clrect.centerx)
        self.clcentery = float(self.clrect.centery)
        self.tick = 0
        self.blbutton = None

    def update(self):
        """Update the ghosts"""
        if not self.ai_settings.blueghost:
            if self.tick == 0:
                self.blimage = self.blinky1a
                self.inkimage = self.inky1a
                self.piimage = self.pinky1a
                self.climage = self.clyde1a
            elif self.tick == 60:
                self.blimage = self.blinky1b
                self.inkimage = self.inky1b
                self.piimage = self.pinky1b
                self.climage = self.clyde1b

            elif self.tick == 120:
                self.blimage = self.blinky2a
                self.inkimage = self.inky2a
                self.piimage = self.pinky2a
                self.climage = self.clyde2a
            elif self.tick == 180:
                self.blimage = self.blinky2b
                self.inkimage = self.inky2b
                self.piimage = self.pinky2b
                self.climage = self.clyde2b

            elif self.tick == 240:
                self.blimage = self.blinky3a
                self.inkimage = self.inky3a
                self.piimage = self.pinky3a
                self.climage = self.clyde3a
            elif self.tick == 300:
                self.blimage = self.blinky3b
                self.inkimage = self.inky3b
                self.piimage = self.pinky3b
                self.climage = self.clyde3b

            elif self.tick == 360:
                self.blimage = self.blinky4a
                self.inkimage = self.inky4a
                self.piimage = self.pinky4a
                self.climage = self.clyde4a
            elif self.tick == 420:
                self.blimage = self.blinky4b
                self.inkimage = self.inky4b
                self.piimage = self.pinky4b
                self.climage = self.clyde4b
            self.tick += 1
            if self.tick == 480:
                self.tick = 0
        if self.ai_settings.blueghost:
            self.blimage = self.blueghost
            self.piimage = self.blueghost
            self.inkimage = self.blueghost
            self.climage = self.blueghost
        if self.bldead:
            self.blimage = self.eyes1
        if self.pidead:
            self.blimage = self.eyes1
        if self.inkdead:
            self.inkimage = self.eyes1
        if self.cldead:
            self.climage = self.eyes1

    def reset(self):
        self.blrect.center = (280, 240)
        self.inkrect.center = (30, 60)
        self.pirect.center = (310, 312)
        self.clrect.center = (340, 312)

    def intro(self):
        self.blrect.center = (280, 312)
        self.inkrect.center = (250, 312)
        self.pirect.center = (310, 312)
        self.clrect.center = (340, 312)
        # self.pacman.center = (10, 312)
        self.blrect.right = self.screen_rect.left
        self.pirect.right = self.blrect.left
        self.inkrect.right = self.pirect.left
        self.clrect.right = self.inkrect.left
        self.powerpill_rect.center = (0, 312)
        self.powerpill_rect.right = self.screen_rect.right
        self.ai_settings.intro = True
        self.blcenterx = self.blrect.centerx
        self.picenterx = self.pirect.centerx
        self.inkcenterx = self.inkrect.centerx
        self.clcenterx = self.clrect.centerx

    def introupdate(self):
        if self.ai_settings.intro:
            if self.ai_settings.powerpill and self.ai_settings.introduction == 0:
                self.blcenterx += 1
                self.picenterx += 1
                self.inkcenterx += 1
                self.clcenterx += 1
            if not self.ai_settings.powerpill and self.ai_settings.introduction == 0:
                self.blcenterx -= 1
                self.picenterx -= 1
                self.inkcenterx -= 1
                self.clcenterx -= 1
                self.powerpill_rect.centerx = -50
            if self.ai_settings.introduction == 1:
                self.blcenterx = -10
                self.picenterx = -10
                self.inkcenterx = -10
                self.clcenterx = -10
                self.blcenterx = self.blrect.centerx
                self.picenterx = self.pirect.centerx
                self.inkcenterx = self.inkrect.centerx
                self.clcenterx = self.clrect.centerx
                self.ai_settings.introduction = 2
            if self.ai_settings.introduction == 2:
                self.blcenterx += 1
                self.blbutton = Button(self.screen, "BLiNKY")
                self.blbutton.rect.centerx = self.blrect.centerx
                self.blbutton.rect.centery = self.blrect.centery - 20
                self.blbutton.msg_image_rect.center = self.blbutton.rect.center
                self.blbutton.draw_button()
                if self.blcenterx > self.screen_rect.right:
                    self.ai_settings.introduction = 3
            if self.ai_settings.introduction == 3:
                self.picenterx += 1
                # self.blbutton.rect.centerx -= 400
                self.blbutton = Button(self.screen, "PiNKY")
                self.blbutton.rect.centerx = self.pirect.centerx
                self.blbutton.rect.centery = self.pirect.centery - 20
                self.blbutton.msg_image_rect.center = self.blbutton.rect.center
                self.blbutton.draw_button()
                if self.picenterx > self.screen_rect.right:
                    self.ai_settings.introduction = 4
            if self.ai_settings.introduction == 4:
                self.inkcenterx += 1
                # self.blbutton.rect.centerx = -100
                self.blbutton = Button(self.screen, "iNKY")
                self.blbutton.rect.centerx = self.inkrect.centerx
                self.blbutton.rect.centery = self.inkrect.centery - 20
                self.blbutton.msg_image_rect.center = self.blbutton.rect.center
                self.blbutton.draw_button()
                if self.inkcenterx > self.screen_rect.right:
                    self.ai_settings.introduction = 5
            if self.ai_settings.introduction == 5:
                self.clcenterx += 1
                # self.blbutton.rect.centerx = -100
                self.blbutton = Button(self.screen, "CLYDE")
                self.blbutton.rect.centerx = self.clrect.centerx
                self.blbutton.rect.centery = self.clrect.centery - 20
                self.blbutton.msg_image_rect.center = self.blbutton.rect.center
                self.blbutton.draw_button()
                if self.clcenterx > self.screen_rect.right:
                    self.ai_settings.introduction = 6

            self.blrect.centerx = self.blcenterx
            self.pirect.centerx = self.picenterx
            self.inkrect.centerx = self.inkcenterx
            self.clrect.centerx = self.clcenterx

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.blimage, self.blrect)
        self.screen.blit(self.inkimage, self.inkrect)
        self.screen.blit(self.piimage, self.pirect)
        self.screen.blit(self.climage, self.clrect)
        self.screen.blit(self.powerpill, self.powerpill_rect)

    def die(self):
        self.bldead = 1
        self.pidead = 1
        self.inkdead = 1
        self.cldead = 1
