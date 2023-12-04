#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:12:07 2023

@author: akshansha
"""
#this function which runs hubworld again runs when game is over or user quits
def back_to_hub():
    import HubWorld2
    HubWorld2.run_hubworld()

#This function which has the entire game is run from hubworld
def run_wordle():
    import pygame #Import the pygame module
    import time
    import random
    import sys
    from sys import exit
    from pygame import mixer
    #Word list below
    word_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']
    word1=word_list[random.randrange(0,499)] #Selects a random word from the list
    answer=list(word1) #turns that word into a list of characters
    print(word1)
    pygame.init() #initializes pygame
      
    clock = pygame.time.Clock() 
    font=pygame.font.SysFont("Helvitca", 60, False, False) #defines a font
    # it will display on screen 
    screen = pygame.display.set_mode([540, 500]) #defines the screen and its size
    screen.fill((0, 0, 0)) #sets the colour of the screen to blakc
    output_rect1= pygame.Rect(200,235, 28,32) #The rectangles below are the color rectangles
    output_rect2=pygame.Rect(228,235, 28,32)#these rectangles let us know whether the letter
    output_rect3=pygame.Rect(256,235, 28,32)#is in the right spot/in the word
    output_rect4=pygame.Rect(284,235, 28,32)#They are basically the letter guesses
    output_rect5=pygame.Rect(312,235, 28,32)
    # basic font for user typed 
    base_font = pygame.font.Font(None, 32) 
    user_text = '' #defines the users guess and the text that they type in as an empty string
    guessed=False #defines the variable guessed and sets it to false
    # create rectangle 
    input_rect = pygame.Rect(200, 200, 140, 32) #Creates the rectangle where user can input guess
    Wordle_logo=pygame.image.load('Wordle.png')#Defines an image of the wordle logo
    screen.blit(Wordle_logo, (151,100))#Places an image of the wordle logo
    mixer.init()#Initializes the mixer function
    mixer.music.load("jeopardy.mp3")#Loads the jeopardy theme
    mixer.music.set_volume(0.7)#Sets volume of song
    mixer.music.play() #Plays jeopardy theme in the background

    # color_over stores color black which 
    # happens when game is over
    color_over = pygame.Color((0,0,0)) 
      
    # color_passive store color(chartreuse4) which is 
    # color of input box. 
    color_passive = pygame.Color('chartreuse4') 
    color = color_passive 
    green=pygame.Color("green")
    yellow=pygame.Color("yellow")
    gray=pygame.Color("gray")
    #Lines above define a couple colors

    
    color=False
    list_1=[] #This is an empty list where the user's guesses will be stored


                
                

            
            
                    
    guesses=0 #This variable will count the guesses of the user               
    game_over=False #This variable will be set to true if either the user wins or loses
    while True: 

            
        def screenshot(): #defines the screenshot function
        #this function essentially saves the guesses of the user and displays them below
        #the input box
            if game_over==False: #This function only runs while the games running
                rect = pygame.Rect(200,235,140,32) #Defines a rectangle where the guesses appear
                sub = screen.subsurface(rect) #defines the subspace of the rectangle
                pygame.image.save(sub, "svs"+str(guesses)+".png") 
                #The above line takes a picture where the guess appears and stores it 
                #The picture will have the name of the guesses variable at the time it was taken
                if guesses>=2: #When guesses is >=2 it will load the image at location(200,267)
                    pic1=pygame.image.load('svs1.png').convert_alpha()
                    screen.blit(pic1, (200,267))
                if guesses>=3:#When guesses is >=3 it will load the image at location(200,299)
                    pic2=pygame.image.load('svs2.png').convert_alpha()
                    screen.blit(pic2, (200, 299))
                if guesses>=4:#When guesses is >=4 it will load the image at location(200,331)
                    pic3=pygame.image.load('svs3.png').convert_alpha()
                    screen.blit(pic3, (200, 331))
                if guesses>=5:#When guesses is >=5 it will load the image at location(200,363)
                    pic4=pygame.image.load('svs4.png').convert_alpha()
                    screen.blit(pic4, (200, 363))
                if guesses==6:#When guesses is >=6 it will load the image
                    pic5=pygame.image.load('svs5.png').convert_alpha()
                    
            
            
                
                
                
            
            
        subtext="" #sub text variable which will be used when checking guess vs answer
        
            
            
        for event in pygame.event.get(): 
      
          # if user types QUIT then hub is imported again
            if event.type == pygame.QUIT: 
                back_to_hub()
                
      
            
      
            if (event.type == pygame.KEYDOWN): 
      
                # Check for backspace 
                if event.key == pygame.K_BACKSPACE: 
      
                    # get text input from 0 to -1 excluding the last value i.e. end. 
                    # effectively deletes that value
                    user_text = user_text[:-1] 
      
                # Unicode standard is used for string 
                # formation 
                else:
                    #This basically checks if the length of the user's guess has 5 letters
                    #If true it stops them from writing anymore
                    if len(list(user_text))==5:
                        
                        #If The length is 5 and the user presses enter/return
                        #the guess is essentially "inputted"
                        if event.key == pygame.K_RETURN:
                            #When enter is pressed the guesses variable increases
                            guesses+=1
                            
                            #Then the user's guess will be appended to the end of the list
                            list_1.append(user_text)
                            #When checking for answer, it'll check the last item in the-
                            #-list of guesses
                            sub_text1=list_1[-1]
                            #sets subtext to the string of the last item in the list
                            sub_text=str(sub_text1)
                            #Creates an empty list of lists that will be indexed into, 
                            #will store colours and letters
                            word = [[], [], [], [], []]
                            #This for loop is saying:
                            #for any i in the range of the guess
                            #if the value in the location index of i is the same 
                            #as the value of the location index in answer
                            #Go to that same location index in the word list
                            #in the first value store the letter, and in the second value
                            #store the colour green as it is in the correct location
                            for i in range(len(sub_text)):
                                if sub_text[i] == answer[i]:
                                    word[i] = [sub_text[i], green]
                           
                            #This for loop is saying:
                            #for any i in the range of the guess
                            #if the letter corresponding to the index location
                            #is in the list of letters in answer, and if the letter
                            #in that location is not the letter in the same location in answer
                            #Then go to that location in the word list
                            #Place the letter in the first value, and store 
                            #The colour yellow in the second location
                            for i in range(len(sub_text)):
                                if sub_text[i] in answer and sub_text[i] != answer[i]:
                                    word[i] = [sub_text[i], yellow]
                                    
                            #This for loop is saying:
                            #for any i in the range of the guess
                            #If the letter is not in the list of letters in answer:
                            #Go into the same location index in the word list
                            #In the first value store the letter
                            #In the second value store the letter gray
                            for i in range(len(sub_text)):
                                if sub_text[i] not in answer:
                                    word[i] = [sub_text[i], gray]
                                    
                           #The above for loops basically store, the letter in the 
                           #correct location and assign the colour based on the guess
                             
                           #This is a for loop that runs infinitely
                            for i in range(len(sub_text)):
                                #These lines draw a rectangle in the spots corresponding
                                # to guesses
                                #and gives it the colour stores in the second value
                                # in each index in the array
                                #It draws the rectangles in the locations stated above
                                pygame.draw.rect(screen, word[0][1], output_rect1)
                                pygame.draw.rect(screen, word[1][1], output_rect2)
                                pygame.draw.rect(screen, word[2][1], output_rect3)
                                pygame.draw.rect(screen, word[3][1], output_rect4)
                                pygame.draw.rect(screen, word[4][1], output_rect5)
                                #The lines below basically render the letter that is 
                                #stored in those locations, 
                                #The letters will be white
                                text_surface2 = base_font.render(sub_text[0], True, (255,255,255))
                                text_surface3 = base_font.render(sub_text[1], True, (255,255,255)) 
                                text_surface4 = base_font.render(sub_text[2], True, (255,255,255)) 
                                text_surface5 = base_font.render(sub_text[3], True, (255,255,255)) 
                                text_surface6 = base_font.render(sub_text[4], True, (255,255,255))
                                #The lines below create a rectangle for each text letter
                                #And it sets the center of the rectangle to be the
                                #center of the output guess box
                                # this is to ensure that guesses don't overlap
                                #in their rectangles
                                center1=text_surface2.get_rect(center=output_rect1.center)
                                center2=text_surface3.get_rect(center=output_rect2.center)
                                center3=text_surface4.get_rect(center=output_rect3.center)
                                center4=text_surface5.get_rect(center=output_rect4.center)
                                center5=text_surface6.get_rect(center=output_rect5.center)
                                #The lines below actually place the text rectangles
                                #at the centers of their respective guess boxes
                                screen.blit(text_surface2, center1)
                                screen.blit(text_surface3, center2)
                                screen.blit(text_surface4, center3)
                                screen.blit(text_surface5, center4)
                                screen.blit(text_surface6, center5)
                            
                            
                            
                            
                            #This if statement checks if any of the recent guesses
                            #are exactly equal to the answer
                            #if that is so and if the guesses are less than or equal to 6
                            #They have won the game!
                            #The whole screen will turn black
                            #It will then render text that says that they've won
                            #it will also render the number of guesses
                            #The game over variable is set to true
                            #The jeopardy music will stop and the winner music will play
                            if ((str(list_1[-1])==word1) and guesses<=6):
                            
                                screen.fill((0,0,0))
                                pygame.draw.rect(screen, (0,0,0), input_rect)
                                winner_text=base_font.render("You win!"+" Guesses:"+str(guesses), True, (0,255,0))
                                screen.blit(winner_text, (200,400))
                                game_over=True
                                mixer.music.stop()
                                mixer.music.load("Final Fantasy.mp3")
                                mixer.music.set_volume(0.7)
                                mixer.music.play()
                            #This if statement checks if any of the recent guesses
                            #are not exactly equal to the answer
                            #if that is so and if the guesses are equal to 6
                            #They have lost the game
                            #The whole screen will turn black
                            #It will then render text that says that they've lost
                           
                            #The game over variable is set to true
                            #The jeopardy music will stop and the angry birds music will play
                            if ((str(list_1[-1])!=word1) and (guesses==6)):
                                screen.fill((0,0,0))
                                pygame.draw.rect(screen, (0,0,0), input_rect)
                                loser_text=base_font.render("You lose!", True, (0,255,0))
                                screen.blit(loser_text, (200,400))
                                game_over=True
                                mixer.music.stop()
                                mixer.music.load("Angry Birds Theme.mp3")
                                mixer.music.set_volume(0.7)
                                mixer.music.play()
                                
                            #Each time the loop repeats and a guess is made
                            #the screenshot function is run to take a picture of the guess
                            # and display it
                            screenshot()
                            

                                
                          
                            # the guess is made blank so they can guess again
                            user_text=""
                           
                            
                    else:
                        #When the key corresponding to unicode is pressed
                        #the user text will be equal to whatever the user presses added
                        #to the text
                        user_text += event.unicode
                    
                        
                    
                    
                        
                    
                
            
            
          
        # it will set background color of screen 
        
      #If game over is false the rectangle where things are input is green
        if game_over==False: 
            color=color_passive 
        #if game over is true, the color of the input rectangle is set to black
        if game_over: 
            color = color_over
            user_text=('')
            
            
              
        
        #This draws the rectangle on the screen and sets it to whatever the color variable is 
        # set to
        pygame.draw.rect(screen, color, input_rect) 
        
        
                
        
        
        
        #This creates the user's text with white colour
        text_surface = base_font.render(str(user_text), True, (255, 255, 255)) 
        
          
        # render at position stated in arguments 
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
        
        
          
          
      
          
       

         #The functions below updates the full display surface to the screen   
        pygame.display.flip()  
        #The functions below updates portions of the screen for software displays
        pygame.display.update()
        #The game will run at 60 frames per second
        clock.tick(60) 

    
    