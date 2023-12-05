# -*- coding: utf-8 -*-
"""
Lauren Robinson 
21067122
Hello! This is the base code from the tutorial I watched on youtube.I omitted the part of the tuotrial where sound was added, but I've pasted the video link here! I also changed the shoot keys from teh video, as I was on a different laptopsetup.  
https://www.youtube.com/watch?v=jO6qQDNa2UY
"""

                                                        #Imports!
import pygame #First, we must import pygame since we will using graphics and manipulating them.  
import os # By importing os, we are creating a file directory so we can import the graphics from our computer. Our graphics must be saved in the same file directory as our .py file. 
pygame.font.init() # This intializes the font module so we can write text in a desried font on the screen. 

                                                    # Creating Variables! 
#Creating the Screen!
WIDTH, HEIGHT = 900,500 # Since we will be using the width and height as perameters in our game, its best to make these into their own varaibles. That way if we change either, we don't have to re-write sections of code.  
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #This initalizes a our game window that our user will interact with. We will a tuple with our width and height!
pygame.display.set_caption('First Game') #This is simply creating a name for the window that our user interacts with. 
WHITE = (255,255,255) # In pygame, to use colours we must use their RBG (Red,Blue,Green) values. We can create a tuple for the R, B, and V value. Since we will be using colours multiple times, we make it into a variable. We can use this varible in the windows fill command. 
BLACK = (0,0,0) # RBG for Black. 
RED = (255,0,0) # RBG for Red.
YELLOW = (255,255,0) # RBG for Yellow.
FPS = 60 #FPS means frames per second. This controls the speed at which the game runs, and allows it to not be based on the speed of the users computer. 
VEL = 5 # This variable will serve as the velocity variable, which will determine how fast the spaceship moves. 
BULLET_VEL = 7 #This controls the speed that our bullets will fire at. The speed of the bullets is faster than the speed of the player to make the game more exciting!  
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40 #We are creating variables for the height and width of our player. In pygame, one way we can manipulate the characters is by making them rectangles. These variables will help us to crete these rectangles in our main function!
BORDER = pygame.Rect(WIDTH//2 -5 ,0,10,HEIGHT) #pygame.Rect creates a rectangle that we can later draw onto our screen. Since we want this rectangle to be a border in the middle of our screen, we integer divide the width by 2, and use the height as the length. 
                                                #Pygames grid coordniates work from the top left corner outwards. This means when we draw images we will be drawing them from their top left corner outwards. Understanding this will help us place rectangles where we need them on the screen. 
                                                #We are subtracting 5, half of our width to ensure that our border is in the middle of the screen and distrubited evenly across the center!
                                                #Here, and later on in the code when we divide our width or height to draw something at a given spot, we must use integer divison to get whole numbers. Pygame cannot run with decimal values. 

MAX_BULLETS = 5 #We don't want our user to be able to simply spam the shoot key and shoot an infinite amount of bullets. To counter this, we will create a variable stipluating the max amount they can shoot, which we will later call in our code!



HEALTH_FONT = pygame.font.SysFont('comicsans', 40) #Since we imported the font module, we can now create a variable that for text that displays the health of our characters. 
WINNER_FONT = pygame.font.SysFont('comicsons', 100) #Since we imported the font module, we can now create a variable that for text that displays the winner of our game.

YELLOW_HIT = pygame.USEREVENT +1  #Since we will be having things collide (the bullets and our character), we will be using event types to check if this has occured. We can check if this event occurs in the main function and then make adustments to our game, say to the health of characters, if this event occurs.  We had a count at the end of each variable we make to creat a unique evetn ID ypes!
RED_HIT = pygame.USEREVENT + 2 



YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship_yellow.png")) #Here, we are creating a path to the downloaded graphics
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)  #Using the pygame transfomr and rotate commands, we are able to resize our image to the pre-established width and height we created, and rotate it 90 degrees so our spaceships are facing eachother. 
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('spaceship_red.png')) 
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270) # We are doing the same transform, but rotating the red spaceship in the other direction so they're facing eachother. 
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('space.png')), (WIDTH, HEIGHT)) #Here, we are importing the background we would like to use, and scaling it to the size of our game screen.



                                                                    #Functions!
                                                                    
                                                                   #Drawing Images!
                                                                    
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health): #This function is where all our our drawing, or 'blitting' images will occur. In pygame, we need to blit surfaces onto other surfaces.The arguments are everything we want to draw!
                                                                                      #red and yellow are the rectangles we created in our main function. This way, our function will draw red and yellow wherever they get moved to on the screen
                                                                                      #The lists are the lists of our red and yellow bullets defined later in the code
    WIN.blit(SPACE,(0,0)) # First we are blitting our background on at the origin (0,0). THis way it will fill our entire screen. 
    pygame.draw.rect(WIN,BLACK,BORDER) # THis is drawing our border onto our screen. Since we already created all of variables for its position we can simply input them. 
    
    #We want to draw our health displays on the screen before we draw our characters so they can fly over them if needed. 
    
    red_health_text = HEALTH_FONT.render('Health: '+ str(red_health),1, WHITE) #In pygame, we can't directly draw text onto the screen. So, we need to use font.redner() to create a surface that we blit on another surface.  
                                                                                # Here, we are saying render the word health, plus the string of our red/yellow health variable (defined later in the code), 1 for antialisaing (removes the jagged edges effect ), and we the colour we want out text to be, in this case white 
    yellow_health_text = HEALTH_FONT.render('Health: '+ str(yellow_health), 1, WHITE) # The same logic applies here for the yellow health text 
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() -10 ,10 )) #We are blitting the red health on to the screen. Since this is on the right side of the screen, we are subtracting the width of the text from the width of the screen, and then subtractinv an additonal ten to add a gap at the edge (this will make it look nicer)
    WIN.blit(yellow_health_text,(10,10)) #Here we are blitting the yellow health text, at the point 10,10 on our screen which works nicely because yellow is already on the left side
    
    
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y)) #Here we are blitting our spaceships on to the screen. As previously mentoined, we are treating our spaceships like rectangles, so we are using their x and y coordinates that we previously defined in our main function (700,100) and (100,300) and assigning them as red.x and red.y (yellow.x respectively) 
    WIN.blit(RED_SPACESHIP,(red.x, red.y))
    
   
    
    for bullet in red_bullets: #This is drawing our red bullets onto the screen. The bullet and bullet lists are explained later on in the code!  
        pygame.draw.rect(WIN,RED,bullet)  
        
    for bullet in yellow_bullets: # We are doing the same thing here but for making our bullet yellow instead of red
            pygame.draw.rect(WIN,YELLOW,bullet)
    pygame.display.update() #This updates the pygame display, we must place this at the bottom of our draw function so it updates our screen everytime with the images we wish to have on it.



                                                            #Player Movement! 
                                                            
def yellow_handle_movement(keys_pressed,yellow): #Here we are creating a function that will let us move our character around. We want our character to only move when the move keys are pressed, so we must check if this occurs. 
                                                 #Keys_pressed and the yellow/red rectangles have been defined in our main function. We will call our movement functions there.
                                                    # Left Right Movement 
    if keys_pressed[pygame.K_a] and yellow.x- VEL > 0 :#A is the left key, so we want our spaceship to move backwards when this is pressed. Since (0,0) is the outermost left point on the screen, we are going to subtract from our spaceships x position to move us closer to this coordiante.
                                                        # We also must check that our character can't move backwards off the screen, which would mean it would have a negative x value. We create an if statment to ensure that subtracting velocity doesn't let us get into the negatives!
        yellow.x -= VEL #We want them to move backwards(left key) so we are subtracting to get closer to (0,0)
    if keys_pressed[pygame.K_d] and  yellow.x +  VEL  + yellow.width < BORDER.x:  #This is for the right key, we need to check that width is also not over the border
                                                                                   # we also need to check that it can't move past the border. We need to check that our character is less than the border's x positon 
                                                                                   #Since the (0,0) position of our spaceship could techincally still be past the x position of the border, so we also need to make sure that the width of our character isn't over the border!
        yellow.x += VEL #since we are moving forward (right key) we want to add to get further from (0,0).
        
        
                                                    # Up down Movement 
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #W is the up key. Since we are adjusting movement on the y-axis, we want to modif y here instead of x  #Like for the left key movement, we are ensuring we can't move off the screen by check that the y position-Vel doesnt land us in teh negatives
        yellow.y -= VEL #Subtracting for the up movement to bring is closer to (0,0) 
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT -15: #S is the down key. 
                                                                                #Again applying the same logic as the right key, we have to ensure the entire spaceship can exceed the height of the screen. We  subtracting 15 to create a little space gap so it's not directly to the end of the screen, and looks a bit more visually appealing 
        yellow.y += VEL # Adding for the down movemenet to get further from (0,0). ensures that the image cant move past down the screen
    


def red_handle_movement(keys_pressed,red): # Here we are repeating the process for our red spacship with a few adjustments.
                                    # Left Right Movement 
                                    #For red, we will be using the corresponding up, down, left, and right arrows. 
                                    #The logic for the restrictions is the exact same as the yellow spaceship, just adjusted for the flipped version since its on the opposite side of the screen!
                                    
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #We want to check if it's greater than the border x and its width, so it cannot move further left than the border 
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #This differs from yellow as the restriction on our right movement becomes the screen instead of the border
        red.x += VEL
        
                                        # Up down Movement 
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0 : 
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT -15 : 
        red.y += VEL
        
        
        
        
        
                                                            #Shooting 
        
    
def handle_bullets(yellow_bullets,red_bullets, yellow, red,): #Here we are passing in our defined lists and rectangles in main. This will handle the movement and collision of our bullets. 
    for bullet in yellow_bullets: 
        bullet.x += BULLET_VEL # This moves our bullet to the right, so our yellow spaceship is on the left-hand side of the screen 
        if red.colliderect(bullet): #Collide rect is a really cool feature in pygame that lets us check if two rectangles have collided! 
            pygame.event.post(pygame.event.Event(RED_HIT)) #We are posting the event of a collision, RED_HIT. This creates a new event saying the red character was hit! 
            yellow_bullets.remove(bullet) #This deletes the bullet if it collides with the opponenent. 
        elif bullet.x > WIDTH: #Here we use an elif to ensure we don't accidentally remove our bullet twice, and if the x coordinate of our bullet is greater than the screen width since its moving towards the left, we want to remove it from the list. 
            yellow_bullets.remove(bullet)
            
    for bullet in red_bullets: 
         bullet.x -= BULLET_VEL # We subtracted velocity since we want to move our red bullets to the left
         if yellow.colliderect(bullet): #collide rect checks if two rects collide 
             pygame.event.post(pygame.event.Event(YELLOW_HIT)) #The same logic from RED_HIT applies here 
             red_bullets.remove(bullet)
         elif bullet.x < 0 : # Here we are saying less than zero instead of width, since the bullet from this side is shooting to towards the left, and zero is the left-most point on the screen 
             red_bullets.remove(bullet) 
             
      
                                                                        #Winner Display!  
             
def draw_winner(text): #This function will display which character has one of the screen! We make a new function outside of draw, so we can call this in our main function to restart the game 
    draw_text = WINNER_FONT.render(text,1,WHITE) #This renders our winner text, which follows the same process as our red and yellow healths 
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2)) # We want to draw this in the cetner of the screen, so we divide the width by 2 and then subtracting half of the width of our text, we repeat this for height. Essentially this ensures that our text will be displayed in the center of our screen. 
    pygame.display.update() #Again we have to update our displaye
    pygame.time.delay(5000) #Pasues the game when someone wins

                                                                        #Main Function!
def main(): #This function will act as our main that will check the main events of our game
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #Here, we are creating rectangles to represent our red and yellow spaceships. The first two arguments are its x and y position on the screen. Since pygame acts like a grid, we are saying to put the top left of the rectangle at point(700,300)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #Repeating this process for the yellow spaceship!
    red_bullets = [] #We need to maintain a list of the bulllets each character is shooting 
    yellow_bullets = [] #These lists will store all of the players bullets! To create a bullet we can simply add to the list!

    

    
    red_health = 10 #Here we are creating a starting health value for our characters
    yellow_health = 10 
    clock = pygame.time.Clock()
    run = True 
    while run: # This is creating while loop while our game is runnin!
        clock.tick(FPS) #We need a way to control the speed our game runs at. We can use clock.tick for this! This will controls the speed of the while loop (60 times per second, which is our predetermined FPS).
        for event in pygame.event.get(): #This creates a ist of all the different evetns we can check and allows us to loop through them. 
            if event.type == pygame.QUIT: # One of the first things we need to check is if the user closes game. We can use pygame.QUIT to check for this.
                run = False # This will end our while loop
                pygame.quit() # This will close down the window for us. The quit event is when we press the x on the top of our screen.
            if event.type == pygame.KEYDOWN: #Sinc we want the player to have to press the shoot key to fire,
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS: #ctrl is the left player shooting button. Since we only want our player to shoot the the max amount of bullets, we ensure that the length of the yellow bullets is less than our max bullets.
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)  # We are just making a yellow rectangle to act as our bullet. We want to fire from the middle of the character and move it towards the right. So it needs to come from their x position plus their width! Then we take the y poistion and add half the heigh so it comes directly from the middle of the character. Then we subtract approxtimately half of the height of the bullet so its more precisly in the center. 
                    yellow_bullets.append(bullet) # Now we append bullet into our yellow bullet list.         
                if event.key == pygame.K_p and len(red_bullets) < MAX_BULLETS: #p is the right player. The logic is the same for the max bullets as the yellow spaceship. 
                    bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5) #We repeat the same process for the red character, but since this character is already facing to the left,we want to fire the bullet from its left edge, which is already its x position. We do not need to add its width like we did for yellow which was facing right. 
                    red_bullets.append(bullet)
            if event.type == RED_HIT: # Now we are checking if the event type (the bullet collison) has occured, and if it has, we want to subtract 1 from the opponenets health.
                red_health -= 1
            if event.type == YELLOW_HIT :
                yellow_health -=1
        
      
       

                
                
        winner_text = "" # The winner text here is an empty string, however if either of the characters die, the winner text will become either "yellow wins" or "Red Wins" 
        if red_health <= 0 : 
            winner_text = 'yellow wins'
        if yellow_health <= 0: 
            winner_text = 'red wins'
            
        if winner_text != "": #Then, if the winner text is not an empty string, ie its been reassigned, we want to display who won. 
            draw_winner(winner_text) #This will call our draw winner function, display the text, and then we add a break so we can then call the main function to restart the game.
            break
        
       
  
          
          
            
        
        keys_pressed = pygame.key.get_pressed() #Everytime we run this while loop, this will tell us which keys are currently being pressed. 
        yellow_handle_movement(keys_pressed, yellow) #Here we are calling the movement fucntions to run in our main game function! The two seperate functions help the code be neater and more organized.
        red_handle_movement(keys_pressed, red)
            
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        draw_window(red,yellow,red_bullets,yellow_bullets, red_health, yellow_health) #calling the draw window funciton 
    
    main() # Here we call main so it restarts it     
       
    
    
    

if __name__ == "__main__":
    main() #This ensures that we run this file direclty, not if this file is imported.