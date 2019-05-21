import random

import pygame
import sys
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((800, 600))
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
scorefont = pygame.font.Font('freesansbold.ttf', 28)
list_velocityx = [-10,10]
list_velocityy = [-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,5,6,7,8,9,10,11,12,13,14,15]


class Paddles():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.rect = pygame.Rect(self.posx, self.posy, 20, 150)
        self.paddle = pygame.draw.rect(screen, black,self.rect )

    def update(self, posy):

        if (self.posy + posy >= 0) and (self.posy + posy <= 450):
            self.rect = pygame.Rect(self.posx, self.posy + posy, 20, 150)
            pygame.draw.rect(screen, black, self.rect)
            self.posy += posy


        else:
            pygame.draw.rect(screen, black, self.rect)


class Ball():
    def __init__(self):
        self.velocityx = random.choice(list_velocityx)
        self.velocityy = random.choice(list_velocityy)
        self.posx = 400
        self.posy = 300
        self.ball = pygame.Rect(self.posx,self.posy,20,20)
        pygame.draw.ellipse(screen,black,self.ball)





    def updateX(self):
        self.velocityx = self.velocityx * -1
        self.ball  = pygame.Rect(self.posx + self.velocityx,self.posy + self.velocityy,20,20)
        pygame.draw.ellipse(screen,black,self.ball)
        self.posy = self.posy + self.velocityy
        self.posx = self.posx + self.velocityx


    def updateY(self):
        self.velocityy = self.velocityy * -1
        self.ball = pygame.Rect(self.posx + self.velocityx,self.posy + self.velocityy,20,20)
        pygame.draw.ellipse(screen,black,self.ball)
        self.posy = self.posy + self.velocityy
        self.posx = self.posx + self.velocityx
        print(self.posy)


    def update(self):
        self.ball = pygame.Rect(self.posx + self.velocityx, self.posy + self.velocityy, 20, 20)
        pygame.draw.ellipse(screen, black,self.ball)
        self.posy = self.posy + self.velocityy
        self.posx = self.posx + self.velocityx


    def reset(self):
        self.posx = 400
        self.posy = 300
        self.velocityy = random.choice(list_velocityy)
        self.velocityx = random.choice(list_velocityx)
        self.ball = pygame.Rect(self.posx,self.posy,20,20)
        pygame.draw.ellipse(screen,black,self.ball)



def menutext():
    text = font.render('Welcome to Pong By Jordi', 20, white)
    text1 = font.render('Press 1 for Single player 2 for Multiplayer', 20, white)
    text1rect = text1.get_rect()
    text1rect.center = (400, 400)
    textrect = text.get_rect()
    textrect.center = (400, 300)
    screen.blit(text, textrect)
    screen.blit(text1, text1rect)
    pygame.display.flip()


def scoretext(playerscore, aiscore):
    playertext = scorefont.render(str(playerscore), 20, black)
    aitext = scorefont.render(str(aiscore), 20, black)
    playertextrect = playertext.get_rect()
    aitextrect = aitext.get_rect()
    playertextrect.center = (150, 30)
    aitextrect.center = (650, 30)
    screen.blit(playertext, playertextrect)
    screen.blit(aitext, aitextrect)


def multiplayer():
    playerscore = 0
    player2score = 0
    player2paddle = Paddles(775, 200)
    playerpaddle = Paddles(10, 200)

    playerpaddle.update(0)
    player2paddle.update(0)
    clock = pygame.time.Clock()
    ball = Ball()


    running = True
    # Our main loop!
    while running:
        # for loop through the event queue
        key = None
        for event in pygame.event.get():
            # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(55)
        pygame.event.pump()
        pressed = pygame.key.get_pressed()


        screen.fill(white)


        if pressed[pygame.K_ESCAPE]:
            print("yeye")
            running = False

        if pressed[pygame.K_w]:


            playerpaddle.update(-10)
            player2paddle.update(0)

        if pressed[pygame.K_s]:


            playerpaddle.update(10)
            player2paddle.update(0)

        if pressed[pygame.K_UP]:


            playerpaddle.update(0)
            player2paddle.update(-10)

        if pressed[pygame.K_DOWN]:

            playerpaddle.update(0)
            player2paddle.update(10)




        if ball.posy <=0 or ball.posy >= 600:
            ball.updateY()


        if ball.ball.colliderect(playerpaddle.rect) or ball.ball.colliderect(player2paddle.rect):
            ball.updateX()

        if ball.posx <= 0:
            player2score +=1
            ball.reset()

        if ball.posx >= 800:
            playerscore += 1
            ball.reset()

        if player2score == 5 or playerscore == 5:
            running = False
        else:
            ball.update()
            scoretext(playerscore,player2score)
            player2paddle.update(0)
            playerpaddle.update(0)


        pygame.display.update()


def game():
    running = True
    menutext()
    # Our main loop!
    while running:
        # for loop through the event queue

        for event in pygame.event.get():
            # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
            if event.type == KEYDOWN:
                # If the Esc key has been pressed set running to false to exit the main loop
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_1:
                    screen.fill(white)
                    pygame.display.update()
                    multiplayer()
                if event.key == K_2:
                    screen.fill(white)
                    pygame.display.update()
            # Check for QUIT event; if QUIT, set running to false
            elif event.type == QUIT:
                running = False


if __name__ == '__main__':
    game()
