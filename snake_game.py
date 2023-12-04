#   SNAKE GAME
#   Author : Apaar Gupta (@apaar97)
#   Python 3.5.2 Pygame

import pygame
import sys
import time
import random

# Pygame Init
pygame.init()

#sending back to hubworld
def back_to_hub(): #Code added by LG
    import HubWorld2 #Code added by LG
    HubWorld2.run_hubworld() #Code added by LG
def run_snake_game():
    # Play Surface
    size = width, height = 640, 320
    playSurface = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake Game")
    
    # Colors
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    brown = pygame.Color(165, 42, 42)
    
    # FPS controller
    fpsController = pygame.time.Clock()
    
    # Game settings
    delta = 10
    snakePos = [100, 50]
    snakeBody = [[100, 50], [90, 50], [80, 50]]
    foodPos = [400, 50]
    foodSpawn = True
    direction = 'RIGHT'
    changeto = ''
    score = 0
    
    
    # Game Over
    def gameOver():
         while True:   
            myFont = pygame.font.SysFont('monaco', 72)
            GOsurf = myFont.render("Game Over", True, red)
            GOrect = GOsurf.get_rect()
            GOrect.midtop = (320, 25)
            playSurface.blit(GOsurf, GOrect)
    #==============================================================================        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    back_to_hub()
                    
                if event.type == pygame.MOUSEBUTTONUP:#Code added by LG
                    pos = pygame.mouse.get_pos()#Code added by LG
                    
                    if pos[0] in range(180, 435) and pos[1] in range(170, 230): #Code added by LG
                        back_to_hub() #Code added by LG     
                    #quit button    
            large_font = pygame.font.Font(None, 60) #Code added by LG
            text_quit = large_font.render('Quit to hub', True, 'White') #Code added by LG
            quit_rect = text_quit.get_rect(midtop = (305, 180)) #Code added by LG
            pygame.draw.rect(playSurface, 'Black', (180,170,255,60)) #Code added by LG
            playSurface.blit(text_quit, quit_rect) #Code added by LG
    #==============================================================================
            showScore(0)
            pygame.display.flip()
    
    # Show Score
    def showScore(choice=1):
        SFont = pygame.font.SysFont('monaco', 32)
        Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
        Srect = Ssurf.get_rect()
        if choice == 1:
            Srect.midtop = (80, 10)
        else:
            Srect.midtop = (320, 100)
        playSurface.blit(Ssurf, Srect)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                back_to_hub()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
    
        # Validate direction
        if changeto == 'RIGHT' and direction != 'LEFT':
            direction = changeto
        if changeto == 'LEFT' and direction != 'RIGHT':
            direction = changeto
        if changeto == 'UP' and direction != 'DOWN':
            direction = changeto
        if changeto == 'DOWN' and direction != 'UP':
            direction = changeto
    
        # Update snake position
        if direction == 'RIGHT':
            snakePos[0] += delta
        if direction == 'LEFT':
            snakePos[0] -= delta
        if direction == 'DOWN':
            snakePos[1] += delta
        if direction == 'UP':
            snakePos[1] -= delta
    
        # Snake body mechanism
        snakeBody.insert(0, list(snakePos))
        if snakePos == foodPos:
            foodSpawn = False
            score += 1
        else:
            snakeBody.pop()
        if foodSpawn == False:
            foodPos = [random.randrange(1, width // 10) * delta, random.randrange(1, height // 10) * delta]
            foodSpawn = True
    
        playSurface.fill(white)
        for pos in snakeBody:
            pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], delta, delta))
        pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))
    
        # Bounds
        if snakePos[0] >= width or snakePos[0] < 0:
            gameOver()
        if snakePos[1] >= height or snakePos[1] < 0:
            gameOver()
    
        # Self hit
        for block in snakeBody[1:]:
            if snakePos == block:
                gameOver()
        showScore()
        pygame.display.flip()
        fpsController.tick(20)
