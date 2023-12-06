# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:30:11 2023

@author: lucgo
"""
#Code written and commented by Luc Gorbet #21088307

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
g_active = False #boolean value of wheather the green note(F key) is being played/pressed by the user
r_active = False #boolean value of wheather the red note(G key) is being played/pressed by the user
y_active = False #boolean value of wheather the yellow note(H key) is being played/pressed by the user
b_active = False #boolean value of wheather the blue note(J key) is being played/pressed by the user

#score and lives
font = pygame.font.Font(None, 30) #this line describes a font("None") using pygame and sets the font size to 30 pixels and assigns this to the variable named "font"
#this will make it easier to display text in the future as the font variable has all the information and the font type and size will not need to be specified everytime

#modes/states (start menu, playing, game lost) and text display
mode = 'start' #the mode variable is checked later in the code to test the part of the game the player is in. The start mode is the  home screen, "play" is the name of the mode in which the code will run the plable game. And "lost" is the mode when the player has lost all their lives.
large_font = pygame.font.Font(None, 60) #describes another font using the same pygame function but this font is larger and assigned to the variable "large_font". This font will be used for things like title screens.
text_start = large_font.render('Press space to start', True, 'White') #creating text to display to the user. the first argument string is the text that i want displayed, the second argument is whether i want antialias, and the third is the colour i want the text to be displayed as.
start_rect = text_start.get_rect(midbottom = (250, 155)) #assigns a position to the text_start text by seeing how big the string is pixel wize and assigns the bottom middle the the point (250, 155) 
text_instructions = font.render('Use F, G, H, and J to play the right notes', True, 'White')
instructions_rect = text_instructions.get_rect(midbottom = (250, 180))
text_try_again = font.render('Press space to play again', True, 'Red')

text_quit = large_font.render('Quit to hub', True, 'White')
quit_rect = text_quit.get_rect(midtop = (250, 280))

#=== note movement when generated ==================================================================================

#green notes
gnote_img = [] #this is a list that will contain all the images of the green note that will be displayed on the game screen. Everytime a new green note is generated, a new copy of the green note image will be added to this list with it's own index.
gnote_rect = [] #this will be the list of the rectangles that correspond to each green note image iin the gnote_img list above. The first rectangle in the list (index 0) will be assigned to the first image (index 0) in the list above of note images.
gnoteX_change = -1 #this is the x velocity that will be assigned to the green note rectangles in the list above. this will make the rectangles move 1 pixel to the left every frame.
gnoteY_change = +5 #this is the y velocity that will be assigned to the green note rectangles in the list above. this will make the rectangles move 5 pixel down every frame.
#the combination of the x and y velocity will make it appear as if the green notes are following the green note string that is displayed on the screen.

#this function will be run whenever a new green note is wanted to be generated.
def spawn_green():
    gnote_img.append(g_note) #this appends a new instance of the g_note image to the gnote_img list. 
    gnote_rect.append(g_note.get_rect(midbottom = (228,199))) #this line creates a rectangle for the new image that was just generated and assigns its original position to be (228,199). This position is at the top of the green string on the screen. 
    #By appending this rectangle into the gnote_rect list at the same time as the image is appended, it means that the rectangle coresponding to the image at index 0 in the image list will be in the rectangle list in index 0 (the indexs will always matchup).

#the following lines of code from 86 to 115 are using the same proses for creating and tracking the note images and their rectangles but it is for the remaining coloured notes(red, yellow, blue). 
    #the one thing that varried from colour to colour, is the x and y velocity as well as the rectangle positions as those define where the notes spawn and how they move once generated later on. The velocity and position for each colour are set to spawn at the top of that colours string and move in a way so that it someone follows the string.

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
# this function is called to send the user back to the Hub/arcade screen.
def back_to_hub():
    import HubWorld2 # imports the HubWorld2 code which is the arcade screen
    HubWorld2.run_hubworld() #this is the name of the function within HubWorld2.py that actually runs the code and starts the game.
#==========================================================================

#this is a general function that will allow the came to be run from the hub/arcade by using this run_guitar_hero function
def run_guitar_hero():
    screen = pygame.display.set_mode((500,560)) #making a display screen & specifying size (pixel width, pixel height)
    clock = pygame.time.Clock() #helps track time and allows us to controll framerate
    
    #setting key effects to be off when game starts... these boolean variables will be used to determine when a note is being pressed (setting them to False at the start)
    g_active = False #boolean value of wheather the green note is being played/pressed by the user
    r_active = False #boolean value of wheather the red note is being played/pressed by the user
    y_active = False #boolean value of wheather the yellow note is being played/pressed by the user
    b_active = False #boolean value of wheather the blue note is being played/pressed by the user
    
    #score and lives
    score = 0 #this variable tracks the player's score, starting at zero and increases by one when the player hits a note at the right time
    score_list = [0] #this is a list of all the guitar hero scores while the game is running. Used to calculate the player's total score across multiple guitar hero games
    lives = 5 #variable is the number of lives the player has (initially set to 5). as the player misses notes, they will lose lives and this variable will decrease. this value will be checked and if it is 0 or lower then it is determined that the player has lost.

    #modes/states (start menu, playing, game lost) and text display
    mode = 'start' #the mode variable is checked later in the code to test the part of the game the player is in. The start mode is the  home screen, "play" is the name of the mode in which the code will run the plable game. And "lost" is the mode when the player has lost all their lives.

    while True: #this while loop makes everything within it repeat every frame. thus variables such as lives can repeatidly be checked to know when the player loses
        if mode == 'start': #mode is set to start when the run_guitar_hero function is run so anthing is the if statement is what will happen when the run_guitar_hero function is called.
            for event in pygame.event.get(): #this is a pygame function that allows you to check multiple events such as: if a key is pressed, if the game is exited, if the mouse is being clicked, etc.

                if event.type == pygame.QUIT:# this if statement is True when you hit the x botton in the top right of the window. 
                    back_to_hub() #runs the function that imports and runs the hub/arcade. Makes it so whenever the game is quit using the exit x botton in the top right of the window, it sends the user back to the hub world/arcade.
                
                if event.type == pygame.KEYDOWN: # pygame function that checks if any key on the keyboard is being press and returns true if one is pressed.
                    if event.key == pygame.K_SPACE: #when the spar bar is pressed, the mode will turn to 'play' and the actual gameplay will start. 
                        mode = 'play' # mode 'play' is when the user actually plays the game, so when the player is in the start screen and they press space, it will start the game.
            screen.blit(bg_surface, (0,0)) #displays the background image for guitar hero on the screen, setting the top left of the image to be in the top left of the display screen (0,0)
            screen.blit(text_start, start_rect) #displays the strat text onto the screen in the start_rect position. this text is what tells the player that they have to press teh space bar to start the game.
            screen.blit(text_instructions, instructions_rect) # displays the instruction text onto the screen. This text tells the player to use the 'F', 'G', 'H', and 'J' keys to play the notes/strings at the right time.
            pygame.display.update() #this function updates the screen so that anything that is set to be displayed will now be displayed.
    
        if mode == 'lost': #code that runs when the player loses. mode will be changed to equal 'lost' when the player loses later in the code whihc would make this if statement run.
            total_score = sum(score_list) #this calculates the players total score over the course of however many times they've played
            text_lose = large_font.render('Your score was ' + str(score), False, 'White') #text that concatenates a string and the score variable to display to the player what their score was at the end of the game.
            lose_rect = text_lose.get_rect(midbottom = (250, 190)) #rectangle that marks the position in pixels where the text_lose text will want to be displayed 
            text_total_score = font.render('Your overall score is ' + str(int(total_score)), True, 'Red') #displays the player's total score over the course of howevermany games they play. Note these strings wont show up on the screen till the string is drawn onto the screen or blitted.
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #this is the same check as above in lines 147-148 which just checks to see if the game is being exited and if it is to send the player back to the hub/arcade
                    back_to_hub()
                
                if event.type == pygame.KEYDOWN: #checks if keys are being pressed.
                    if event.key == pygame.K_SPACE: #if the spacebar is pressed the following code in the if statement will run.
                        mode = 'play' #sets the mode to 'play' making the game start as the game is played when mode is equal to 'play'
                        score = 0 #this reassigns the variable score to 0 to make sure the player starts the new game with no points 
                        lives = 5 #this reassigns the number of lives of the player to 5 before the game starts.
                        
                if event.type == pygame.MOUSEBUTTONUP: #chekcs if the mouse button was released. this will only be true when the main mouse button is released not when pressed
                    pos = pygame.mouse.get_pos() #returns a tuple of the coordinates of the mouse of the screen in pixels.
                    if pos[0] in range(110, 380) and pos[1] in range(270, 330): #checks if the mouse position when the mouse button was released is within the x and y ranges inidcated. A quit to hub/arcade button is placed in this pixel location. 
                        back_to_hub() #when the player hits the button, it will send them back to the hub by running this function 
            
            #quit button
            pygame.draw.rect(screen, 'White', (100,260,300,80)) #draws a white rectangle that's bottom left is 100 pixels from the left of the screen, has a width of 260,is lowest point is at y = 300, and that has a hieght of 60 pixels
            pygame.draw.rect(screen, 'Black', (110,270,280,60)) #draws black rectangle ontop of white one
            screen.blit(text_quit, quit_rect) # displays the exit button text at the quit_rect position which is on the button.
            
            pygame.draw.rect(screen, 'White', (55,135,400,115))
            pygame.draw.rect(screen, 'Black', (65,145,380,95))
            screen.blit(text_lose, lose_rect) #draws/shows/prints/blits the text that shows up when you lose the game. this strings tells you what your score was before you lost
            screen.blit(text_total_score, (130, 190)) #shows the text on the screen that displayes the players total score. this text will be in the position (130, 190)
            screen.blit(text_try_again, (120,210)) #shows the text on the screen that informs the player on how to play again.
            pygame.display.update() #updates the screen so that any text or images that have been placed on the display actually show up
            
    #=== code running while playing game ==========================================
        if mode == 'play': #checks if the mode is equal to 'play' which indicates that the player wants to start playing the game.
            screen.blit(bg_surface, (0,0)) # displays background onto the screen 
            pygame.display.update() #updates the screen so that the background is vissible right away.
        #=== lose sequence =================================================================================================
            
            if int(lives) <= 0:#checks whether the player has lost the game by seeing if their numbe of lives is 0 or lower
                mode = 'lost' #if they have lost it sets the mode to lose so that on the next loop it will run the if statement for when the player has lost
                score_list.append(score) #adds the players game score to the list of all their scores so that their total score can be calculated 
                gnote_img.clear() #the following few lines is clearing the lists that are used to store the displayed images and their positions. This will also make them no longer be displayed after the player loses 
                gnote_rect.clear()
                rnote_img.clear()
                rnote_rect.clear()
                ynote_img.clear()
                ynote_rect.clear()
                bnote_img.clear()
                bnote_rect.clear()
                
            for event in pygame.event.get():
                # making game exitable while playing the game (when mode == 'play')
                if event.type == pygame.QUIT:
                    back_to_hub()
        
        #=== key colour effects ============================================================================================
        
                if event.type == pygame.KEYDOWN: #when a key is pressed check the following in the if statement:
                    
                    if event.key == pygame.K_f: #checks if the key pressed was the 'F' key, this key corresponds to the green string in the game. 
                        time_i_g = pygame.time.get_ticks() #this gets the time that the F key was pressed and assigns it to a varriable. the variable is the initial time that the green string was played.
                        time_f_g = time_i_g + 100 #adds 100 milliseconds to the time that the butten was initially pressed and assigns that new time to a varribale. the variable is the final time that the green string was played till. meaning the code will test if the curent time has reached this point.
                        g_active = True #stes g_active to be True when the f button is pressed.
                        screen.blit(g_key, g_key_rect) #displays the green key effect that happens when you play a note. this allows the player to see what note their playing and it immerses them into the game.
                        pygame.display.update() #make the sttuff that has been added to the screen get displayed.
                        
                    if event.key == pygame.K_g: #checks if the key pressed was the 'G' key, this key corresponds to the red string in the game. 
                        time_i_r = pygame.time.get_ticks()
                        time_f_r = time_i_r + 100 
                        r_active = True
                        screen.blit(r_key, r_key_rect)
                        pygame.display.update()
                        
                    if event.key == pygame.K_h: #checks if the key pressed was the 'H' key, this key corresponds to the yellow string in the game. 
                        time_i_y = pygame.time.get_ticks()
                        time_f_y = time_i_y + 100 
                        y_active = True
                        screen.blit(y_key, y_key_rect)
                        pygame.display.update()
                        
                    if event.key == pygame.K_j: #checks if the key pressed was the 'J' key, this key corresponds to the blue string in the game. 
                        time_i_b = pygame.time.get_ticks() 
                        time_f_b = time_i_b + 100
                        b_active = True
                        screen.blit(b_key, b_key_rect)
                        pygame.display.update()
        
        #this next part of the code runs when a note button (F, G, H, or J) has been pressed.
            if g_active: #this is true when the corresponding green note key (F) has been pressed.
                if pygame.time.get_ticks() < time_f_g: #checks whether the curent time is smaller than the final time that the key effect should last till(time_f_g)
                    screen.blit(g_key, g_key_rect) #if the time is smaller, then it displays the key effect on the screen. 
                    pygame.display.update()
                    
                elif pygame.time.get_ticks() >= time_f_g: #checks whether the current time is past or is equal to the duration of the time that the key effect should last.
                    screen.blit(g_idle, (0,0)) #if the key effect should be over (aka the current time is greater than time_f_g), this makes the key on the game screen back to normal and not light up.
                    pygame.display.update()
                    g_active = False #this is telling the code that the player is not longer pressing the key corresponding to the green note and that the effects that are related to the pressing of the green note should stop (aka go back to normal).
        
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
        
            if pygame.time.get_ticks()%20 == 0: #this line checks the time/fram and if it is divisible by 20 then it does what is in the if statement. This is just a method that i came up with to randomly decide when the game should generate notes. 
                 note = random.randint(0,3) #using the random module, i create a random integer that is one of four posible values (0,1,2,3) and assign it to the variable 'note'. These four values will each correspond to a different colour note that should be generated.
                 if note == 0: #if the random number is a zero, the spawn_green function will run which will create a green note. the same goes for the rest of the notes but for the other random integer values.
                     spawn_green()
                 if note == 1:
                     spawn_red()
                 if note == 2:
                     spawn_yellow()
                 if note == 3:
                     spawn_blue()
            
        #=== displaying notes on screen and colision system ================================================================
            #this section of the code, takes the already astablished imgaes of the notes and their rectangles and chnages their rectangle position to make the notes move. This is also where the notes get displayed on the screen.
            #it also checks whether the coloured notes and it's respective key are coliding if the player clicks the button.
        
            #green notes
            for g in range(len(gnote_rect)-1): #for loop that is in the range of the number of green notes that have been addded to the gnote_rect & gnote_img lists. only checks the length of one since the two will always have the same length. The reasoning for the "len() -1" is because there could be x number of elements in the list but the position of the last one would be x-1.
                gnote_rect[g].x += gnoteX_change #for every rectangle in the list, this line changes its x position by the preset variable that corresponds to its x velocity (noteX_change) and reasigns that x value to the rect making it move.
                gnote_rect[g].y += gnoteY_change #does the same thing as the code above but changing the y position of the rectangle.
                screen.blit(gnote_img[g], gnote_rect[g]) #takes the image 
                
                #detecting colisions (i.e. when player plays note at right time)
                if g_key_rect.colliderect(gnote_rect[g]) and g_active:
                    gnote_rect.remove(gnote_rect[g])
                    gnote_img.remove(gnote_img[g])
                    score += 1
                
                if gnote_rect[g].y > 560: #this is checking whether any of the green notes have gone out of frame this way they can be revomed from the list of images that get displayed (gnote_img) and so that I can track how many notes the player misses to remove a life. 
                    gnote_rect.remove(gnote_rect[g]) #if a green note is no longer on the screen, remove it's rectangle form the green note rectangle list (gnote_rect) as that note and it's rectangle has no use anymore since it's off screen.
                    gnote_img.remove(gnote_img[g]) #removes the image of the green note that has gone past the screen from the list of green notes images to display on the screen. 
                    lives -= 1 #takes away a life from the player for having missed a note. simply done by using augmented assignment to subtract one from the current lives value and reassign the new number to the lives variable.
                
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
            
            text_score = font.render('Score: ' + str(int(score)) , False, 'White') #creates text that will dispay the players curent score 
            score_rect = text_score.get_rect(midbottom = (250, 180)) #rectangle that defines a position. will be used to position the string above on the screen
            text_lives = font.render('Lives: ' + str(int(lives)), False, 'Red') #creates text that will dispay the player's curent number of lives so that they can track however many notees they have missed and make sure to not miss any more.
            lives_rect = text_lives.get_rect(midbottom = (250,155)) #rectangle that defines a position. will be used to position the string above on the screen
            
            screen.blit(text_score, score_rect) 
            screen.blit(text_lives, lives_rect)
            pygame.display.update()
            clock.tick(40) #setting the frames per second to 40. meaning this code will try and run 40 times per second