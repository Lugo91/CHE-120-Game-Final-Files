#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:04:28 2023

@author: akshansha
"""


import pygame

pygame.init()

screen = pygame.display.set_mode((400,400)) # making a display screen & specifying size
clock = pygame.time.Clock()

carpet_surface = pygame.image.load('graphics/arcade/carpet.png').convert_alpha()

font = pygame.font.Font(None, 45) #this line describes a font("None") using pygame and sets the font size to 30 pixels and assigns this to the variable named "font
start_text = font.render('Welcome to the arcade!', True, "White")
start_rect = start_text.get_rect(midbottom = (200,100))#renders at position stated in arguments
#Code below initializes the screen and prints the text shown below
#At position stated in arguments
font_small = pygame.font.Font(None, 25)
info1_text = font_small.render('use arrow keys to move', True, "White")
info2_text = font_small.render('and press space bar to enter games', True, "White")
info1_rect = info1_text.get_rect(midbottom = (200,135))
info2_rect = info2_text.get_rect(midbottom = (200,160))

def start_hubworld(): #this is the function that runs when you first run the HubWorld2.py file
      screen = pygame.display.set_mode((400,400)) # making a display screen & specifying size
      clock = pygame.time.Clock() #allows us to chnage framerate of game
      
      while True:
          
          for event in pygame.event.get(): 
              # making game exitable (VERY IMPORTANT!)
              if event.type == pygame.QUIT: #when the player hits the close window button in the top right the code in the if statement will run
                  pygame.quit() #quits pygame
                  exit() #exits the window/ closes the application.
              
              if event.type == pygame.KEYDOWN:# test if a key on keyboard is being pressed
                   if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE: #if the key that is being pressed is one of these, the code within the if statement bellow will run
                       run_hubworld() #runs the arcade function that allows player to run arround and play games.
                       
          screen.blit(carpet_surface, (0,0)) #displaying background on screen 
          screen.blit(start_text, start_rect) #creates a string that displays a welcome message to the player 
          screen.blit(info1_text, info1_rect) # creates a string that displays a message on how to satrt the game 
          screen.blit(info2_text, info2_rect)# creates a string that displays a message on how to satrt the game 
          pygame.display.update() #updates the screen to show anything that is trying to be displayed on the main screen.

def run_hubworld():
    #importing the functions fom modules that run the games:
    from guitar_hero import run_guitar_hero
    from brick_breaker import run_brick_breaker
    from snake_game import run_snake_game
    from flappybird import run_flappybird
    from Wordle import run_wordle
    from RainyRaiders import run_rainy_raiders
    
    # initiating the pygame module (required in order to use pygame properly)
    pygame.init()
    screen = pygame.display.set_mode((400,400)) # making a display screen & specifying size
    clock = pygame.time.Clock()
    #This loads the image that will be used as the entrance to each game
    console_surface = pygame.image.load('graphics/arcade/small-console.png').convert_alpha()
    #When the play isn't moving this is the image that will be shown
    player_idle = pygame.image.load('graphics/player/player_d.png').convert_alpha()
    #This creates a rectangle for the player character and sets 
    # the top of the middle to the position stated in arguments
    player_rect = player_idle.get_rect(midbottom = (200,370)) 
    #renders a font
    test_font = pygame.font.Font(None, 20)
    #renders the text stated below, which shows to the user
    text_enter = test_font.render('Press SPACE to play.', True, 'White')
    #The 6 lines below set the top middle of each of the console images
    #to the positions stated in the arguments
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
    #creates an empty string for the game name
    game_name = ''
    #This creates the text for each console and displays the game name string
    #Which is empty at this point as a player isn't interacting with a console 
    text_console = test_font.render('['+ game_name +']', True, 'Green') #has to be checked while running since this text changing
    
    #defaulting movement to false
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    #on_console variable store the condition of whether player is interacting with console
    on_console = False
    #infinite loop
    while True:
        
        for event in pygame.event.get():
            # making game exitable (VERY IMPORTANT!)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    #=== movement of player ==============================================================        
            if event.type == pygame.KEYDOWN:
                #if the left arrow key is pressed
                #it loads the image corresponding to the character facing left
                #It sets the player variable to that image
                #move left variable set to true
                if event.key == pygame.K_LEFT:
                    player_idle = pygame.image.load('graphics/player/player_left.png').convert_alpha()
                    move_left = True 
                #if the right arrow key is pressed
                #it loads the image corresponding to the character facing right
                #It sets the player variable to that image
                #move right variable set to true
                if event.key == pygame.K_RIGHT:
                    player_idle = pygame.image.load('graphics/player/player_right.png').convert_alpha()
                    move_right = True
                #if the up arrow key is pressed
                #it loads the image corresponding to the character facing up
                #It sets the player variable to that image
                #move up variable set to true
                if event.key == pygame.K_UP:
                    player_idle = pygame.image.load('graphics/player/player_up.png').convert_alpha()
                    move_up = True
                #if the down arrow key is pressed
                #it loads the image corresponding to the character facing down
                #It sets the player variable to that image
                #move down variable set to true
                if event.key == pygame.K_DOWN:
                    player_idle = pygame.image.load('graphics/player/player_d.png').convert_alpha()
                    move_down = True
                #if console set to true
                if on_console:
                    #game_name variable is set when character rect collides with console
                    #if that is true the game name variable is changed to whichever
                    #console they collided with
                    #If space is clicked while they're interacting with the console
                    #the respective game is loaded
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
                #if the key is not pressed the character will not move
                move_left = False
                move_right = False
                move_up = False
                move_down = False
    
    #setting speed when arrow keys are held
        if move_left:
            #while move left is true change x coordinate by -5
            # this is only true when the key is pressed
            player_rect.x -=5
        if move_right:
            #while move left is true change x coordinate by 5
            # this is only true when the key is pressed
             player_rect.x +=5
        if move_up:
            #while move left is true change y coordinate by -5
            # this is only true when the key is pressed
             player_rect.y -=5
        if move_down:
            #while move left is true change y coordinate by 5
            # this is only true when the key is pressed
            player_rect.y +=5      
            
    #=== displaying stuff on screen ==============================================================
        #The below lines render the background images and consoles
        #as well as the player images
        screen.blit(carpet_surface, (0,0))
        screen.blit(console_surface, console1_rect)
        screen.blit(console_surface, console2_rect)
        screen.blit(console_surface, console3_rect)
        screen.blit(console_surface, console4_rect)
        screen.blit(console_surface, console5_rect)
        screen.blit(console_surface, console6_rect)
        screen.blit(player_idle, player_rect) #The player_idle variable changes 
        #based on what key is pressed
        
        # when player collision with any of the consoles in the list that was defined above
        if player_rect.collidelist(consoles) != -1:
            #onconsole is trye
            on_console = True 
            
            #defining text and position for game name display
            #Consol number is set to whatver console the player collided with
            consol_num = player_rect.collidelist(consoles)
            #the game_name list is indexed into and it set to whatever the index of 
            #the specific console number is
            game_name = games[consol_num]
            #The game name is rendered based on when the game_name is set to
            #The text on game name is changed based on the lines above
            text_console = test_font.render('['+ game_name +']', True, 'Green')
            #When the player is interacting with the console
            #The console changes its x and y coordinates to communicate with the
            #user that they are interacting with the console
            console_display_rect = text_console.get_rect(midbottom = (consoles[consol_num].x + 30,consoles[consol_num].y))
           
            #defining position for speech text
            speech_rect = player_rect.inflate(60, 30)
            highscore_rect= consoles[consol_num].inflate(10,30)
           
            #displaying text for entering the game
            screen.blit(text_enter, speech_rect)
            screen.blit(text_console, console_display_rect)
        
        else:
            #if the player is not interacting with the console
            #on console is false and the game name does not appear
            on_console = False
        #Display is updated every 60 ms
        pygame.display.update()
        clock.tick(60)
#Runs hubworld
start_hubworld()