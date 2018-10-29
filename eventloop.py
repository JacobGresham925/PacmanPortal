
import sys
import pygame
from time import sleep


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(ai_settings, pacman, maze, play_button, highscore_button, back,
                     ghosts, blues, sb):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, pacman)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, pacman)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, play_button, mouse_x, mouse_y, ghosts, pacman)
                check_highscorebutton(ai_settings, highscore_button, mouse_x, mouse_y)
                check_backbutton(ai_settings, back, mouse_x, mouse_y)
        if not ai_settings.intro:
            hit_block(ai_settings, pacman, maze, blues, ghosts, sb)


def check_backbutton(ai_settings, back, mouse_x, mouse_y):
    button_clicked3 = back.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked3 and not ai_settings.game_active:
        ai_settings.shs = False


def check_play_button(ai_settings, play_button, mouse_x, mouse_y, ghosts, pacman):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not ai_settings.game_active:
        pygame.mouse.set_visible(False)
        ai_settings.game_active = True
        ghosts.reset()
        pacman.reset()
        pacman.intromus.play()
        ghosts.powerpill_rect.centerx = -10
        ai_settings.intro = False


def check_highscorebutton(ai_settings, highscore_button, mouse_x, mouse_y):
    button2_clicked = highscore_button.rect.collidepoint(mouse_x, mouse_y)
    if button2_clicked and not ai_settings.game_active:
        ai_settings.shs = True


def check_keydown_events(event, pacman):
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = True
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
        pacman.moving_up = False
        pacman.moving_down = False
        pacman.moving_right = False
    elif event.key == pygame.K_UP:
        pacman.moving_left = False
        pacman.moving_up = True
        pacman.moving_down = False
        pacman.moving_right = False
    elif event.key == pygame.K_DOWN:
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = True
        pacman.moving_right = False
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, pacman):
    if event.key == pygame.K_RIGHT:
        # pacman.moving_right = False
        pacman.tick = 0
    elif event.key == pygame.K_LEFT:
        # pacman.moving_left = False
        pacman.tick = 0
    elif event.key == pygame.K_UP:
        # pacman.moving_up = False
        pacman.tick = 0
    elif event.key == pygame.K_DOWN:
        # pacman.moving_down = False
        pacman.tick = 0


def hit_block(ai_settings, pacman, maze, blues, ghosts, sb):
    # i = 0
    # temp = False
    # j = 0
    k = len(maze.dots)
    for j in range(k):
        if pygame.Rect.colliderect(pacman.rect, maze.dots[j]):
            print(str(j) + 'deleted')
            del(maze.dots[j])
            pacman.waka.play()
            ai_settings.score += 50 * ai_settings.level
            if ai_settings.score > ai_settings.hs:
                ai_settings.hs = ai_settings.score
            break
    for l in range(len(maze.powerpills)):
        if pygame.Rect.colliderect(pacman.rect, maze.powerpills[l]):
            del(maze.powerpills[l])
            blues.play()
            ai_settings.blueghost = True
            ai_settings.bluetick = 0
            break
    ai_settings.bluetick += 1

    if ai_settings.blueghost:
        if pygame.Rect.colliderect(pacman.rect, ghosts.blrect):
            if ghosts.bldead == 0:
                pacman.esound.play()
            ghosts.bldead = 1
        if pygame.Rect.colliderect(pacman.rect, ghosts.pirect):
            if ghosts.pidead == 0:
                pacman.esound.play()
            ghosts.pidead = 1
        if pygame.Rect.colliderect(pacman.rect, ghosts.inkrect):
            if ghosts.inkdead == 0:
                pacman.esound.play()
            ghosts.inkdead = 1
        if pygame.Rect.colliderect(pacman.rect, ghosts.clrect):
            if ghosts.cldead == 0:
                pacman.esound.play()
            ghosts.cldead = 1
    else:
        if pygame.Rect.colliderect(pacman.rect, ghosts.blrect):
            pacman.dead = 1
            if ai_settings.lives_left > 0:
                ai_settings.lives_left -= 1
                sb.prep_pacmans()
                ghosts.reset()
                sleep(0.5)
            else:
                ai_settings.game_active = False
                hs_file = open("score.txt", "r")
                score = int(hs_file.read())
                if score < ai_settings.hs:
                    hs_file.close()
                    hs_file = open("score.txt", "w")
                    hs_file.write(str(ai_settings.hs))
                hs_file.close()
                pacman.intro()
                ghosts.intro()

        if pygame.Rect.colliderect(pacman.rect, ghosts.pirect):
            pacman.dead = 1
            ai_settings.lives_left -= 1
        if pygame.Rect.colliderect(pacman.rect, ghosts.inkrect):
            pacman.dead = 1
            ai_settings.lives_left -= 1
        if pygame.Rect.colliderect(pacman.rect, ghosts.clrect):
            pacman.dead = 1
            ai_settings.lives_left -= 1

    if ai_settings.bluetick == 602:
        ai_settings.blueghost = False
        # ******Temp*****
        ghosts.pidead = 0
        ghosts.bldead = 0
        ghosts.inkdead = 0
        ghosts.cldead = 0
    # i = 0
    for i in range(len(maze.bricks)):
        for rect in maze.barriers:
            if pygame.Rect.colliderect(pacman.rect, maze.bricks[i]) or pygame.Rect.colliderect(pacman.rect, rect):
                # possible fix ---- find if it collides with top bottom left or right of the pacman
                if pacman.moving_right:
                    pacman.centerx -= ai_settings.pac_speed_factor
                    pacman.moving_right = False
                    pacman.moving_left = True
                    return
                    # pacman.moving_right = False
                if pacman.moving_left:
                    pacman.centerx += ai_settings.pac_speed_factor
                    pacman.moving_left = False
                    pacman.moving_right = True
                    return
                    # pacman.moving_left = False

    # i = 0
    for i in range(len(maze.bricks)):
        for rect in maze.barriers:
            if pygame.Rect.colliderect(pacman.rect, maze.bricks[i]) or pygame.Rect.colliderect(pacman.rect, rect):
                if pacman.moving_up:
                    pacman.centery += ai_settings.pac_speed_factor
                    pacman.moving_up = False
                    pacman.moving_down = True
                    return
                    # pacman.moving_up = False
                if pacman.moving_down:
                    pacman.centery -= ai_settings.pac_speed_factor
                    pacman.moving_down = False
                    pacman.moving_up = True
                    return
                    # pacman.moving_down = False


def mapreader(): pass
