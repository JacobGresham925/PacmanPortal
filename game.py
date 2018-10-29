import pygame
from eventloop import EventLoop
from maze import Maze
from pacman import Pacman
from ghosts import Ghosts
from settings import Settings
from button import Button
from scoreboard import Scoreboard


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 740))
        self.ai_settings = Settings()
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile='map.txt', brickfile='square',
                         portalfile='square', shieldfile='shield', pointfile='point',
                         dotfile='dot', powerpillfile='powerpill')

        self.pacman = Pacman(self.ai_settings, self.screen, self.maze)
        self.ghosts = Ghosts(self.ai_settings, self.screen, self.maze, self.pacman)
        self.displayname = Button(self.screen, "PacmanPortal")
        self.play_button = Button(self.screen, "PLAY GAME")
        self.highscore_button = Button(self.screen, "HIGH SCORES")
        self.blinkyname = Button(self.screen, "BLiNKY")
        self.pinkyname = Button(self.screen, "PiNKY")
        self.clydename = Button(self.screen, "CLYDE")
        self.inkeyname = Button(self.screen, "iNKEY")
        self.back = Button(self.screen, "Back")
        self.sb = Scoreboard(self.ai_settings, self.screen, self.maze, self.pacman)
        self.score = Button(self.screen, "hello")
        self.blues = 0

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        # self.displayname = Button(self.screen, "Portal Pacman")
        self.displayname.rect.centery -= 300
        self.displayname.msg_image_rect.center = self.displayname.rect.center
        # self.highscore_button = Button(self.screen, "Portal Pacman")
        self.highscore_button.rect.centery += 330
        self.highscore_button.msg_image_rect.center = self.highscore_button.rect.center
        # self.play_button = Button(self.screen, "Portal Pacman")
        self.play_button.rect.centery += 280
        self.play_button.msg_image_rect.center = self.play_button.rect.center

        hs_file = open("score.txt", "r")
        self.ai_settings.hs = int(hs_file.read())
        hs_file.close()
        msgg = 'The high score is ' + str(self.ai_settings.hs)
        self.score = Button(self.screen, msgg)
        self.score.rect.centery -= 150
        self.score.msg_image_rect.center = self.score.rect.center
        self.ghosts.intro()
        self.pacman.intro()
        self.blues = pygame.mixer.Sound('sounds/blueghosts.wav')

        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.pacman, self.maze, self.play_button,
                               self.highscore_button, self.back, self.ghosts, self.blues, self.sb)
            if self.ai_settings.score > self.ai_settings.hs and self.ai_settings.game_active:
                self.ai_settings.hs = self.ai_settings.score
                msgg = 'The high score is ' + str(self.ai_settings.hs)
                score = Button(self.screen, msgg)
                score.rect.centery += 150
                score.msg_image_rect.center = score.rect.center
            if len(self.maze.dots) == 1:
                self.maze = Maze(self.screen, mazefile='map.txt', brickfile='square',
                                 portalfile='square', shieldfile='shield', pointfile='point',
                                 dotfile='dot', powerpillfile='powerpill')
                self.pacman.reset()
                self.ghosts.reset()
                self.ai_settings.level += 1
            if not self.ai_settings.game_active:
                pygame.mouse.set_visible(True)
            self.update_screen()

    def update_screen(self):
        self.pacman.update()
        self.ghosts.update()
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.blitme()
        self.ghosts.blitme()
        self.sb.prep_score()
        self.sb.prep_high_score()
        # self.sb.prep_pacmans()
        self.sb.show_score()

        if not self.ai_settings.game_active:
            self.screen.fill(self.ai_settings.bg_color)
            self.displayname.draw_button()
            self.highscore_button.draw_button()
            self.play_button.draw_button()
            self.ghosts.introupdate()
            self.ghosts.blitme()
            self.pacman.introupdate()
            self.pacman.blitme()

        if self.ai_settings.shs:
            self.screen.fill(self.ai_settings.bg_color)
            self.back.draw_button()
            self.score.draw_button()

        pygame.display.flip()


game = Game()
game.play()
