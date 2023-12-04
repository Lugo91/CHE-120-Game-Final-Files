# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:25:18 2023

@author: laure
"""


#Here is my changed code! I have left some of my original comments that I wrote g following the video, but I elaborated on the parts that I addded
import pygame 
import random #Since I want the healtcare packages to be falling at random from the sky, I needed to import the random module. 


import os #creating a file directory so we can import the graphics 
pygame.font.init()

def back_to_hub(): 
    import HubWorld2 
    HubWorld2.run_hubworld() 

def run_rainy_raiders(): 
    WIDTH, HEIGHT = 900,500 #can scale down the size of graphic
    WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #telling pygame to make a new window of this width and height
    pygame.display.set_caption('Rainy Raiders') #I changed the caption to the name of my game! 
    WHITE = (255,255,255) #we can use this varible in the windows fill command 
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0) 
    GREEN = (0,225,0) #Using what I learned about colours in pygame, I creted three new colours to use for my new elements! 
    PURPLE = (128,0,128)  
    BLUE = (0,0,225)
    FPS = 60 #controls the speed at which the game runs, and allows it to be based on more than just the speed of the users computer
    VEL = 5 # SPEED THAT IT MOVES
    BULLET_VEL = 7 # moves faster than characters so more fun 
    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,65  #I changed the spaceship width and height to match the new graphics I was using!
    BORDER = pygame.Rect(WIDTH//2 -5 ,0,10,HEIGHT)
    BORDER1 = pygame.Rect(WIDTH//2 - 250, 100,10, 300)  #Here I created two new parameters borders, which will serve as my jump points. Using what I learned about pygame graphics, I was able to place them appropriately on the screen.
    BORDER3 = pygame.Rect(WIDTH//2 + 250, 100, 10, 300) # Border1 is the jumppoint for the left side of the screen, and and Border3 is the jumpoint for the right side
    
    OBSTACLE1= pygame.Rect(WIDTH//3 + 200,50,100,50) # Here, I am creating the rectangle that will act as 'purple' hole on the right side
    
    OBSTACLE2 = pygame.Rect(WIDTH//3 - 305, 200,100,50) #This rectangle is the 'purple' hole on the left
    HEALTHPACKAGE = pygame.Rect(WIDTH//4, 200,10,50) #Here, I am creating the rectangle that will "rain" from the sky as a healthcare pacakge 
    
    
    MAX_BULLETS = 5 
    ASTEROID_SPEED = 5
    
    
    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
    WINNER_FONT = pygame.font.SysFont('comicsons', 100)
    
    YELLOW_HIT = pygame.USEREVENT +1  # TWO SEPERATE USERS EVENTS WE CAN CHECK FOR, creating events to check for in the main waller
    RED_HIT = pygame.USEREVENT + 2 
    
    
    
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("yellow_character.png")) #creating a path to the downloaded graphics
    YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)  #For both of my new characters I had to adjust the rotation angle since they were different than the ones used in the tutorial.
    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('red_character.png')) #idk why it didnt work with calling it assets, make sure youre running files in the game folder and tagging the file type 
    RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
    
    
    
    SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Background.png')), (WIDTH, (HEIGHT*2))) #Here I am just changing the backdrop. I had to resize it to twice the height so it looked visually better.  
    
    def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health): # all the drawing is happening here, drawinf red and yellow where argyment is 
        WIN.blit(SPACE,(0,0))
    
        pygame.draw.rect(WIN,BLACK,BORDER)
        pygame.draw.rect(WIN,RED,BORDER1) #Using,pygame.draw.rect I am simply creating the rectangles for the rain, the purple holes, and the jump points, using the variables I created earlier 
        pygame.draw.rect(WIN,BLUE,BORDER3) 
        pygame.draw.rect(WIN,PURPLE,OBSTACLE1)
        pygame.draw.rect(WIN,PURPLE,OBSTACLE2)
        pygame.draw.rect(WIN,GREEN,HEALTHPACKAGE)
        
      
    
        
    
        
        
        red_health_text = HEALTH_FONT.render('Health '+ str(red_health), 1, WHITE)
        yellow_health_text = HEALTH_FONT.render('Health '+ str(yellow_health), 1, WHITE)
        WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() -10 ,10 )) # ten fromt op 
        WIN.blit(yellow_health_text,(10,10))
        
        
        WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y)) #blit for drawing surfaces onto the screen , rectangel defiend in x and y
        WIN.blit(RED_SPACESHIP,(red.x, red.y))
        
       
        
        for bullet in red_bullets: 
            pygame.draw.rect(WIN,RED,bullet)
            
        for bullet in yellow_bullets: 
                pygame.draw.rect(WIN,YELLOW,bullet)
                
        
    
    
    
    
        pygame.display.update() #this updates the pygame display, we must do that after every step 
    
    
    def yellow_handle_movement(keys_pressed,yellow): #easier to see
        if keys_pressed[pygame.K_a] and yellow.x- VEL > 0 : 
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and  yellow.x +  VEL  + yellow.width < BORDER.x : 
            yellow.x += VEL
        if keys_pressed[pygame.K_d] and  yellow.x +  VEL  + yellow.width < BORDER1.x : #My border1, is simply a rectangle that I could adjust the character movements around. 
            yellow.x += 40*VEL                                                          #So, we need to check that when the entire yellow rectangle is behind border1 (we must add its width to the the x value, reasoning explained in original game file)
                                                                                        #If it is behind the jump point, we want to add 40 times the normal velocity to the x value when the forward key is pressed. This way, it acts like a 'jump point' and rushes the character to greater than border1, or ahead of border 1
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:                             #This only occurs when the character is behing the line, and the left key is pressed once. This makes it more challenging for the character to move adn dodge bullets seemlessly, and adds another fun element to the game!!
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT -15:
            yellow.y += VEL 
        
    
    
    def red_handle_movement(keys_pressed,red): #easier to see
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: 
            red.x -= VEL
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER3.x + BORDER3.width:  #I repeated the same logic here for border3, on the right side of the screen. When the entire character is on the left side of border3, and the left key is pressed, we want to have it move towards the origin (0,0) at ten times the original velocity 
            red.x -= 40*VEL                                                           #This, like border1 acts as the left sides jump point. For both characters, the jump point only works when they are BEHIND the border. Past this point the movement keys function as normal.  
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: 
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0 : 
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT -15 : # 
            red.y += VEL
        
    def handle_bullets(yellow_bullets,red_bullets, yellow, red,): #handles the bullets adn their collisions, and moving bullet when they got off screen 
        for bullet in yellow_bullets: 
            bullet.x += BULLET_VEL 
            if red.colliderect(bullet): #collide rect checks if two rects collide
                pygame.event.post(pygame.event.Event(RED_HIT)) # posting an event to check in main function
                yellow_bullets.remove(bullet)
            elif bullet.x > WIDTH:   #making sure doesnt go off the screen 
                yellow_bullets.remove(bullet)
                
        for bullet in red_bullets: 
             bullet.x -= BULLET_VEL 
             if yellow.colliderect(bullet): #collide rect checks if two rects collide 
                 pygame.event.post(pygame.event.Event(YELLOW_HIT))
                 red_bullets.remove(bullet)
             elif bullet.x < 0 :
                 red_bullets.remove(bullet) 
                 
           
                            
        
            
        
                 
    def draw_winner(text):
        draw_text = WINNER_FONT.render(text,1,WHITE)
        WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000) #Pasues game when someone wins
    
    
    def main(): #creating a loop so game will open and run 
        red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #rectangle reps red spacsgip
        yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        red_bullets = []
        yellow_bullets = []
    
        
    
        
        red_health = 10 
        yellow_health = 10 
        clock = pygame.time.Clock()
        run = True 
        while run: 
            clock.tick(FPS) #controls the speed of the while loop (60 times per second)
            for event in pygame.event.get(): #list of all the different evetns we can check 
                if event.type == pygame.QUIT: #if user closes game 
                    run = False #ends game 
                    back_to_hub()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5) # taking top left hand corner and hadding the height/2 so it comes frim mid 
                        yellow_bullets.append(bullet)            
                    if event.key == pygame.K_p and len(red_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5) # taking top left hand corner and hadding the height/2 so it comes frim mid 
                        red_bullets.append(bullet)
                if event.type == RED_HIT:
                    red_health -= 1
                if event.type == YELLOW_HIT :
                    yellow_health -=1
            
            
                if pygame.Rect.colliderect(red,OBSTACLE1): #Here using Rect.Colliderect in the main funciton, I am checking to see my either of the characters have collided with the purple hole. 
                    red_health -=2                          #If they have, then I have it set so their health value decreases by 2 instead of one!
                                                            #This was placed in the main loop so the statment is looped through while the game runs.
                    
                if pygame.Rect.colliderect(yellow,OBSTACLE2):
                     yellow_health -=2
                if pygame.Rect.colliderect(red,HEALTHPACKAGE): #Using the same logic, I was able to detect collisions between the characters and the healthcare package rain fallilng 
                    red_health +=1                              #If a collision was detected, then I the health is increased by one
                    
                if pygame.Rect.colliderect(yellow,HEALTHPACKAGE): 
                    yellow_health +=1 
           
            
               
            HEALTHPACKAGE.y +=20  #Since the healthcare package I created is a rectangle, like with my characters I can create a y coordiante for it. Here I am adding 20 to the y value, so it moves down the screen with a 'velocity' of 20!
                                    #I decided on the value 20 so the healthcare packages moved quickly, which make them hard for the characters to catch!
            if HEALTHPACKAGE.y > HEIGHT : #This conditional Statment checks that if the y coordinate has exceed the height of the screen, or gotten to the bottom of the screen (cont. on next line)
                HEALTHPACKAGE.y = -100 #It will then reassign the y value of the coordinate to -100, placing it out of the visbile game window,above the screen 
                HEALTHPACKAGE.x = random.randint(0,WIDTH) #Since the random module has been imported, I am now able to assign a random x value to x coordiante of the rectangle. 
                                                            #The x coordiante is a random integer between 0 and the width of my screen, which creates the appearance that its raining acorss the entire screen 
                    
                    
            
                    
            winner_text = ""       
            if red_health <= 0 : 
                winner_text = 'yellow wins'
            if yellow_health <= 0: 
                winner_text = 'red wins'
                
            if winner_text != "": 
                draw_winner(winner_text)
                break
      
      
              
              
                
            
            keys_pressed = pygame.key.get_pressed() #checks when keys r pressed 
            yellow_handle_movement(keys_pressed, yellow) #calling the movement fucntions
            red_handle_movement(keys_pressed, red)
            
            handle_bullets(yellow_bullets, red_bullets, yellow, red)
            
            draw_window(red,yellow,red_bullets,yellow_bullets, red_health, yellow_health) #calling the draw window funciton 
        
                   
           
        main() # so it restarts it 
    main()