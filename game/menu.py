import pygame
import time

from game.soundplayer import *


class GameMenu:
    def __init__(self, title, screen, fps = 50):
        self.running = True
        self.title = title
        self.screen = screen
        self.FPS = fps
        self.CLOCK = None
        self.bg = None
        self.logo = None
        self.button_play = False
        self.button_records = False
        self.button_quit = False
        playBackgroundMusic()


    def button(self, title, x, y, w, h, i, a, color, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, a, (x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "1":
                    self.button_play = True
                elif action == "2":
                    self.button_records = True
                elif action == "3":
                    self.button_quit = True
        else:
            pygame.draw.rect(self.screen, i, (x,y,w,h))

        smallText = pygame.font.Font('freesansbold.ttf', 19)
        TextSurf, TextRect = self.text_objects(title, smallText, color)
        TextRect.center = ((x+(w/2)),(y+(h/2)))
        self.screen.blit(TextSurf, TextRect)

    def text_objects(self, text, font, color):
    	textSurface = font.render(text, True, color)
    	return textSurface, textSurface.get_rect()

    def run(self):
    	self.CLOCK = pygame.time.Clock()
    	self.bg = pygame.image.load('data/backgrounds/1.png').convert_alpha()
    	self.screen.blit(self.bg, (0, 0))
        self.logo = pygame.image.load('data/backgrounds/logo.png').convert_alpha()
        self.screen.blit(self.logo, (160, 45))
    	while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            banner = (95,0,0)
            options = (240,240,240)
            rect_activate = (60,60,60)
            rect = (30, 30, 30)	

            self.button("Start", 257, 230, 130, 40, rect, rect_activate, options, "1")
            self.button("Records", 257, 280, 130, 40, rect, rect_activate, options, "2")
            self.button("Quit", 257, 330, 130, 40, rect, rect_activate, options, "3")
            
            if self.button_play == True:
                playSoundClick()
                return 1
            elif self.button_records == True:
                playSoundClick()
                return 2
            elif self.button_quit == True:
                pygame.quit()
                quit()
            pygame.display.update()
            self.CLOCK.tick(self.FPS)
