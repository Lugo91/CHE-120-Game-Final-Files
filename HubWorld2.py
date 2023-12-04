#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:04:28 2023

@author: akshansha
"""


import pygame
import os # to be able to search the right directory when finding images

pygame.init()

screen = pygame.display.set_mode((400,400)) # making a display screen & specifying size
clock = pygame.time.Clock()

carpet_surface = pygame.image.load('graphics/arcade/carpet.png').convert_alpha()

font = pygame.font.Font(None, 45) #this line describes a font("None") using pygame and sets the font size to 30 pixels and assigns this to the variable named "font
start_text = font.render('Welcome to the arcade!', True, "White")
start_rect = start_text.get_rect(midbottom = (200,100))

font_small = pygame.font.Font(None, 25)
info1_text = font_small.render('use arrow keys to move', True, "White")
info2_text = font_small.render('and press space bar to enter games', True, "White")
info1_rect = info1_text.get_rect(midbottom = (200,135))
info2_rect = info2_text.get_rect(midbottom = (200,160))

def start_hubworld():
      screen = pygame.display.set_mode((400,400)) # making a display screen & specifying size
      clock = pygame.time.Clock()
      
      while True:
          
          for event in pygame.event.get():
              # making game exitable (VERY IMPORTANT!)
              if event.type == pygame.QUIT:
                  pygame.quit()
                  exit()
              
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                       run_hubworld()
                       
          screen.blit(carpet_surface, (0,0))
          screen.blit(start_text, start_rect)
          screen.blit(info1_text, info1_rect)
          screen.blit(info2_text, info2_rect)
          pygame.display.update()

def run_hubworld():
    #importing the functions fom modules that run the games:
    from guiter_hero import run_guitar_hero
    from brick_breaker import run_brick_breaker
    from snake_game import run_snake_game
    from flappybird import run_flappybird
    from Wordle import run_wordle
    from RainyRaiders import run_rainy_raiders
    
    # initiating the pygame module (required in order to use pygame properly)
    pygame.init()
    #os.chdir('N:\CHE 120\Assignments\Game')
    screen = pygame.display.set_mode((400,400)) # making a display screen & specifying size
    clock = pygame.time.Clock()
    
    console_surface = pygame.image.load('graphics/arcade/small-console.png').convert_alpha()
    
    player_idle = pygame.image.load('graphics/player/player_d.png').convert_alpha()
    player_rect = player_idle.get_rect(midbottom = (200,370))

    test_font = pygame.font.Font(None, 20)
    text_enter = test_font.render('Press SPACE to play.', True, 'White')

    console1_rect = console_surface.get_rect(midtop = (80,100))
    console2_rect = console_surface.get_rect(midtop = (320,100))
    console3_rect = console_surface.get_rect(midtop = (320,200))
    console4_rect = console_surface.get_rect(midtop = (245,50))
    console5_rect = console_surface.get_rect(midtop = (80,200))
    console6_rect = console_surface.get_rect(midtop = (155,50))
    
    #list of games corresponding to each console
    games=["Guitar Hero (LG)", "Brick Breaker", "Snake", "Flappybird", "Wordle (AA)", "Rainy Raiders (LR)"] #change strings to actual game names 

    #list of consoles
    consoles = [console1_rect, console2_rect, console3_rect, console4_rect, console5_rect, console6_rect ]
    
    game_name = ''
    text_console = test_font.render('['+ game_name +']', True, 'Green') #has to be checked while running since this text changing
    
    #defaulting movement to none
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    on_console = False
    
    while True:
        
        for event in pygame.event.get():
            # making game exitable (VERY IMPORTANT!)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    #=== movement of player ==============================================================        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_idle = pygame.image.load('graphics/player/player_left.png').convert_alpha()
                    move_left = True 
                if event.key == pygame.K_RIGHT:
                    player_idle = pygame.image.load('graphics/player/player_right.png').convert_alpha()
                    move_right = True
                if event.key == pygame.K_UP:
                    player_idle = pygame.image.load('graphics/player/player_up.png').convert_alpha()
                    move_up = True
                if event.key == pygame.K_DOWN:
                    player_idle = pygame.image.load('graphics/player/player_d.png').convert_alpha()
                    move_down = True
                if on_console:
                    if game_name=="Guitar Hero (LG)":
                        if event.key == pygame.K_SPACE: #AKSHANSH TYPE HERE
                            run_guitar_hero()
                    elif game_name=="Brick Breaker":
                        if event.key == pygame.K_SPACE:
                            run_brick_breaker()
                    elif game_name=="Snake":
                        if event.key == pygame.K_SPACE:
                            run_snake_game()
                    elif game_name=="Flappybird":
                        if event.key == pygame.K_SPACE:
                            run_flappybird()
                    elif game_name=="Rainy Raiders (LR)":
                        if event.key == pygame.K_SPACE:
                            run_rainy_raiders()
                    elif game_name=="Wordle (AA)":
                        if event.key == pygame.K_SPACE:
                            run_wordle()       
                    
            else:
                move_left = False
                move_right = False
                move_up = False
                move_down = False
    
    #setting speed when arrow keys are held
        if move_left:
            player_rect.x -=5
        if move_right:
             player_rect.x +=5
        if move_up:
             player_rect.y -=5
        if move_down:
            player_rect.y +=5      
            
    #=== displaying stuff on screen ==============================================================
    
        screen.blit(carpet_surface, (0,0))
        screen.blit(console_surface, console1_rect)
        screen.blit(console_surface, console2_rect)
        screen.blit(console_surface, console3_rect)
        screen.blit(console_surface, console4_rect)
        screen.blit(console_surface, console5_rect)
        screen.blit(console_surface, console6_rect)
        screen.blit(player_idle, player_rect)
        
        # collision with console
        if player_rect.collidelist(consoles) != -1:
            on_console = True 
            
            #defining text and position for game name display
            consol_num = player_rect.collidelist(consoles)
            game_name = games[consol_num]
            text_console = test_font.render('['+ game_name +']', True, 'Green')
            console_display_rect = text_console.get_rect(midbottom = (consoles[consol_num].x + 30,consoles[consol_num].y))
           
            #defining position for speech text
            speech_rect = player_rect.inflate(60, 30)
            highscore_rect= consoles[consol_num].inflate(10,30)
           
            #displaying text
            screen.blit(text_enter, speech_rect)
            screen.blit(text_console, console_display_rect)
        
        else:
            on_console = False
    
        pygame.display.update()
        clock.tick(60)

start_hubworld()