# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:30:11 2023

@author: lucgo
"""

import pygame #importing pygame module
import random #importing random module to be able to randomly generate game components

pygame.init() #pygame function used to initialize all imported pygame modules. This is required when working with pygame

screen = pygame.display.set_mode((500,560)) #making a display screen & specifying size (pixel width, pixel height)
clock = pygame.time.Clock() #helps track time and allows us to controll framerate

#background
bg_surface = pygame.image.load('graphics/games/guitar hero/guitar_hero_bg.png').convert_alpha() #importing the image that will be used for the background 

#green string images and objects
g_idle = pygame.image.load('graphics/games/guitar hero/idles/green_idle_key.png').convert_alpha() #importing photo of the green key(green circle) from a specified folder that will be dispayed when the note/key isn't pressed
g_key = pygame.image.load('graphics/games/guitar hero/green_key2.png').convert_alpha() #importing photo of green key that will be displayed when the note is being played ("F" key is being pressed)
g_key_rect = g_key.get_rect(midtop = (162,532)) #this determines the size (width, height) of the "g_key" photo in pixels and sets the top middle of the photo to the position (162,532). 
#Pygame rectangles also make detecting for collisions between two objects easier
g_note = pygame.image.load('graphics/games/guitar hero/green_note.png').convert_alpha() #imports photo of the green note.
g_top_rect = g_note.get_rect(midbottom = (225,199)) #makes a rectangle that is the size of the "g_note" to be able to latter detect when the note is colliding with the key(we'll be able to test if the rectangles are colliding)

#red string images and objects
r_idle = pygame.image.load('graphics/games/guitar hero/idles/red_idle_key.png').convert_alpha() #importing photo of red key(red circle) that will be dispayed when the note/key isn't pressed(the string tells pyhton where to finnd the photo and what it's called)
r_key = pygame.image.load('graphics/games/guitar hero/red_key2.png').convert_alpha()
r_key_rect = r_key.get_rect(midtop = (224,532))
r_note = pygame.image.load('graphics/games/guitar hero/red_note.png').convert_alpha()
r_top_rect = r_note.get_rect(midbottom = (245,199))

#yellow string images and objects
y_idle = pygame.image.load('graphics/games/guitar hero/idles/yellow_idle_key.png').convert_alpha()
y_key = pygame.image.load('graphics/games/guitar hero/yellow_key2.png').convert_alpha()
y_key_rect = y_key.get_rect(midtop = (286,530))
y_note = pygame.image.load('graphics/games/guitar hero/yellow_note.png').convert_alpha()
y_top_rect = y_note.get_rect(midbottom = (260,199))

#blue string images and objects
b_idle = pygame.image.load('graphics/games/guitar hero/idles/blue_idle_key.png').convert_alpha()
b_key = pygame.image.load('graphics/games/guitar hero/blue_key2.png').convert_alpha()
b_key_rect = b_key.get_rect(midtop = (347,530))
b_note = pygame.image.load('graphics/games/guitar hero/blue_note.png').convert_alpha()
b_top_rect = b_note.get_rect(midbottom = (280,199))

#setting key effects to be off when game starts... these boolean variables will be used to determine when a note is being pressed (setting them to False at the start)
g_active = False #boolean value of wheather the green note is being played/pressed by the user
r_active = False #boolean value of wheather the red note is being played/pressed by the user
y_active = False #boolean value of wheather the yellow note is being played/pressed by the user
b_active = False #boolean value of wheather the blue note is being played/pressed by the user

#score and lives
font = pygame.font.Font(None, 30) #this line describes a font("None") using pygame and sets the font size to 30 pixels and assigns this to the variable named "font"
#this will make it easier to display text in the future as the font variable has all the information and the font type and size will not need to be specified everytime

#modes/states (start menu, playing, game lost) and text display
mode = 'start' #the mode variable is checked later in the code to test the part of the game the player is in. The start mode is the  home screen, "play" is the name of the mode in which the code will run the plable game. And "lost" is the mode when the player has lost all their lives.
large_font = pygame.font.Font(None, 60) #describes another font using the same pygame function but this font is larger and assigned to the variable "large_font". This font will be used for things like title screens.
text_start = large_font.render('Press space to start', True, 'White') #creating text to display to the user. the first argument string is the text that i want displayed, the second argument is whether i want antialias, and the third is the colour i want the text to be displayed as.
start_rect = text_start.get_rect(midbottom = (250, 155))
text_instructions = font.render('Use F, G, H, and J to play the right notes', True, 'White')
instructions_rect = text_instructions.get_rect(midbottom = (250, 180))
text_try_again = font.render('Press space to play again', True, 'Red')

text_quit = large_font.render('Quit to hub', True, 'White')
quit_rect = text_quit.get_rect(midtop = (250, 280))

#=== note movement when generated ==================================================================================

#green notes
gnote_img = [] #this is a list that will contain all the images of the green note that will be displayed on the game screen. Everytime a new green note is generated, a new copy of the green note image will be added to this list with it's own index.
gnote_rect = [] #this will be the list of the rectangles that correspond to each green note image iin the gnote_img list above. The first rectangle in the list will be 
gnoteX_change = -1 #
gnoteY_change = +5 #

def spawn_green():
    gnote_img.append(g_note)
    gnote_rect.append(g_note.get_rect(midbottom = (228,199)))

#red notes
rnote_img = []
rnote_rect = []
rnoteX_change = 0
rnoteY_change = +5

def spawn_red():
    rnote_img.append(r_note)
    rnote_rect.append(r_note.get_rect(midbottom = (235,199)))
    
#yellow notes
ynote_img = []
ynote_rect = []
ynoteX_change = 0
ynoteY_change = +5

def spawn_yellow():
    ynote_img.append(y_note)
    ynote_rect.append(y_note.get_rect(midbottom = (278,199)))
    
#blue notes
bnote_img = []
bnote_rect = []
bnoteX_change = +1
bnoteY_change = +5

def spawn_blue():
    bnote_img.append(b_note)
    bnote_rect.append(b_note.get_rect(midbottom = (280,199)))
#==========================================================================
def back_to_hub():
    import HubWorld2
    HubWorld2.run_hubworld()
#==========================================================================
def run_guitar_hero():
    screen = pygame.display.set_mode((500,560)) #making a display screen & specifying size (pixel width, pixel height)
    clock = pygame.time.Clock() #helps track time and allows us to controll framerate
    
    #setting key effects to be off when game starts... these boolean variables will be used to determine when a note is being pressed (setting them to False at the start)
    g_active = False #boolean value of wheather the green note is being played/pressed by the user
    r_active = False #boolean value of wheather the red note is being played/pressed by the user
    y_active = False #boolean value of wheather the yellow note is being played/pressed by the user
    b_active = False #boolean value of wheather the blue note is being played/pressed by the user
    
    #score and lives
    score = 0 #this variable tracks the players score, starting at zero and increases when the player hits a note at the right time
    score_list = [0]
    lives = 5 #variable is the number of lives the player has (initially set to 5). as the player misses notes, they will lose lives and this variable will decrease

    #modes/states (start menu, playing, game lost) and text display
    mode = 'start' #the mode variable is checked later in the code to test the part of the game the player is in. The start mode is the  home screen, "play" is the name of the mode in which the code will run the plable game. And "lost" is the mode when the player has lost all their lives.

    while True:
        if mode == 'start':
            for event in pygame.event.get():
                # making game exitable (VERY IMPORTANT!)
                if event.type == pygame.QUIT:
                    back_to_hub()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        mode = 'play'
            screen.blit(bg_surface, (0,0))
            screen.blit(text_start, start_rect)         
            screen.blit(text_instructions, instructions_rect)
            pygame.display.update()
    
        if mode == 'lost':
            total_score = sum(score_list) #this calculates the players total score over the course of however many times they've played
            text_lose = large_font.render('Your score was ' + str(score), False, 'White')
            lose_rect = text_lose.get_rect(midbottom = (250, 190))
            text_total_score = font.render('Your overall score is ' + str(int(total_score)), True, 'Red')
            
            for event in pygame.event.get():
                # making game exitable (VERY IMPORTANT!)
                if event.type == pygame.QUIT:
                    back_to_hub()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        mode = 'play'
                        score = 0
                        lives = 5
                        
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] in range(110, 380) and pos[1] in range(270, 330):
                        back_to_hub()
            
            #quit button
            pygame.draw.rect(screen, 'White', (100,260,300,80))
            pygame.draw.rect(screen, 'Black', (110,270,280,60))
            screen.blit(text_quit, quit_rect)
            
            pygame.draw.rect(screen, 'White', (55,135,400,115))
            pygame.draw.rect(screen, 'Black', (65,145,380,95))
            screen.blit(text_lose, lose_rect)
            screen.blit(text_total_score, (130, 190))
            screen.blit(text_try_again, (120,210))
            pygame.display.update()
            
    #=== code running while playing game ==========================================
        if mode == 'play':  
            screen.blit(bg_surface, (0,0))
            pygame.display.update()
        #=== quit sequence =================================================================================================
            
            if int(lives) <= 0:
                mode = 'lost'
                score_list.append(score)
                gnote_img.clear()
                gnote_rect.clear()
                rnote_img.clear()
                rnote_rect.clear()
                ynote_img.clear()
                ynote_rect.clear()
                bnote_img.clear()
                bnote_rect.clear()
        
            for event in pygame.event.get():
                # making game exitable (VERY IMPORTANT!)
                if event.type == pygame.QUIT:
                    back_to_hub()
        
        #=== key colour effects ============================================================================================
        
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_f:
                        time_i_g = pygame.time.get_ticks()
                        time_f_g = time_i_g + 100
                        g_active = True
                        screen.blit(g_key, g_key_rect)
                        pygame.display.update()    
                        
                    if event.key == pygame.K_g:
                        time_i_r = pygame.time.get_ticks()
                        time_f_r = time_i_r + 100 
                        r_active = True
                        screen.blit(r_key, r_key_rect)
                        pygame.display.update()
                        
                    if event.key == pygame.K_h:
                        time_i_y = pygame.time.get_ticks()
                        time_f_y = time_i_y + 100 
                        y_active = True
                        screen.blit(y_key, y_key_rect)
                        pygame.display.update()
                        
                    if event.key == pygame.K_j:
                        time_i_b = pygame.time.get_ticks()
                        time_f_b = time_i_b + 100
                        b_active = True
                        screen.blit(b_key, b_key_rect)
                        pygame.display.update()
        
            if g_active:
                if pygame.time.get_ticks() < time_f_g:
                    screen.blit(g_key, g_key_rect)
                    pygame.display.update()
                    
                elif pygame.time.get_ticks() >= time_f_g:
                    screen.blit(g_idle, (0,0))
                    pygame.display.update()
                    g_active = False
        
            if r_active:
                if pygame.time.get_ticks() < time_f_r:
                    screen.blit(r_key, r_key_rect)
                    pygame.display.update()
                    
                elif pygame.time.get_ticks() >= time_f_r:
                    screen.blit(r_idle, (0,0))
                    pygame.display.update()
                    r_active = False
        
            if y_active:
                if pygame.time.get_ticks() < time_f_y:
                    screen.blit(y_key, y_key_rect)
                    pygame.display.update()
                    
                elif pygame.time.get_ticks() >= time_f_y:
                    screen.blit(y_idle, (0,0))
                    pygame.display.update()
                    y_active = False
        
            if b_active:
                if pygame.time.get_ticks() < time_f_b:
                    screen.blit(b_key, b_key_rect)
                    pygame.display.update()
                    
                elif pygame.time.get_ticks() >= time_f_b:
                    screen.blit(b_idle, (0,0))
                    pygame.display.update()
                    b_active = False
        
        #=== Creating notes as objects =====================================================================================
        
            if pygame.time.get_ticks()%20 == 0:  
                 note = random.randint(0,3)
                 if note == 0:
                     spawn_green()
                 if note == 1:
                     spawn_red()
                 if note == 2:
                     spawn_yellow()
                 if note == 3:
                     spawn_blue()
            
        #=== displaying notes on screen and colision system ================================================================
            
            #green notes
            for g in range(len(gnote_rect)-1):
                gnote_rect[g].x += gnoteX_change
                gnote_rect[g].y += gnoteY_change
                screen.blit(gnote_img[g], gnote_rect[g])
                
                #detecting colisions (i.e. when player plays note at right time)
                if g_key_rect.colliderect(gnote_rect[g]) and g_active:
                    gnote_rect.remove(gnote_rect[g])
                    gnote_img.remove(gnote_img[g])
                    score += 1
                
                if gnote_rect[g].y > 560:
                    gnote_rect.remove(gnote_rect[g])
                    gnote_img.remove(gnote_img[g])
                    lives -= 1
                
            #red notes
            for r in range(len(rnote_rect)-1):
                rnote_rect[r].x += rnoteX_change
                rnote_rect[r].y += rnoteY_change
                screen.blit(rnote_img[r], rnote_rect[r])
                
                #detecting colisions (i.e. when player plays note at right time)
                if r_key_rect.colliderect(rnote_rect[r]) and r_active:
                    rnote_rect.remove(rnote_rect[r])
                    rnote_img.remove(rnote_img[r])
                    score += 1
                
                if rnote_rect[r].y > 560:
                    rnote_rect.remove(rnote_rect[r])
                    rnote_img.remove(rnote_img[r])
                    lives -= 1
                
            #yellow notes
            for y in range(len(ynote_rect)-1):
                ynote_rect[y].x += ynoteX_change
                ynote_rect[y].y += ynoteY_change
                screen.blit(ynote_img[y], ynote_rect[y])
                
                #detecting colisions (i.e. when player plays note at right time)
                if y_key_rect.colliderect(ynote_rect[y]) and y_active:
                    ynote_rect.remove(ynote_rect[y])
                    ynote_img.remove(ynote_img[y])
                    score += 1
                    
                if ynote_rect[y].y > 560:
                    ynote_rect.remove(ynote_rect[y])
                    ynote_img.remove(ynote_img[y])
                    lives -= 1
                
            #blue notes
            for b in range(len(bnote_rect)-1):
                bnote_rect[b].x += bnoteX_change
                bnote_rect[b].y += bnoteY_change
                screen.blit(bnote_img[b], bnote_rect[b])
                
                #detecting colisions (i.e. when player plays note at right time)
                if b_key_rect.colliderect(bnote_rect[b]) and b_active:
                    bnote_rect.remove(bnote_rect[b])
                    bnote_img.remove(bnote_img[b])
                    score += 1
                    
                if bnote_rect[b].y > 560:
                    bnote_rect.remove(bnote_rect[b])
                    bnote_img.remove(bnote_img[b])
                    lives -= 1
            
            text_score = font.render('Score: ' + str(int(score)) , False, 'White')
            score_rect = text_score.get_rect(midbottom = (250, 180))
            text_lives = font.render('Lives: ' + str(int(lives)), False, 'Red')
            lives_rect = text_lives.get_rect(midbottom = (250,155))
            
            screen.blit(text_score, score_rect)
            screen.blit(text_lives, lives_rect)
            pygame.display.update()
            clock.tick(40)