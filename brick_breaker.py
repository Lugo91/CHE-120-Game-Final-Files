# This game was not coded by our CHE 120 group and was found and downloaded off of github. 
# This game was created by the user "Marishwaran99" as a public repository called "BrickBreakerPy"
# link to Git repo: https://github.com/Marishwaran99/BrickBreakerPy
#- Luc Gorbet


import pygame,random,time
pygame.init()
def back_to_hub(): #Code added by LG
    import HubWorld2 #Code added by LG
    HubWorld2.run_hubworld() #Code added by LG
def run_brick_breaker():
    Aqua =( 0, 255, 255)
    Black= ( 0, 0, 0)
    Blue =( 0, 0, 255)
    Fuchsia= (255, 0, 255)
    Gray= (128, 128, 128)
    Green= ( 0, 128, 0)
    Lime= ( 0, 255, 0)
    Maroon= (128, 0, 0)
    NavyBlue= ( 0, 0, 128)
    Olive =(128, 128, 0)
    Purple =(128, 0, 128)
    Red= (255, 0, 0)
    Silver =(192, 192, 192)
    Teal =( 0, 128, 128)
    White= (255, 255, 255)
    Yellow =(255, 255, 0)
    dw=400
    dh=400
    screen=pygame.display.set_mode([dw,dh])
    pygame.display.set_caption("Brick Breaker")
    clock=pygame.time.Clock()
    def msg(txt,color,size,x,y):
        font=pygame.font.SysFont("bold",size)
        msgtxt=font.render(txt,True,color)
        msgrect=msgtxt.get_rect()
        msgrect.center=x,y
        screen.blit(msgtxt,msgrect)
    ##    pygame.display.flip()
    class Player(pygame.sprite.Sprite):
        def __init__(self,x,y):
            super().__init__()
            self.image=pygame.image.load("p1.png")
            self.image=pygame.transform.scale(self.image,[70,20])
            self.image.set_colorkey(White)
            
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
            self.vx=0
            self.vy=0
        def update(self):
           
           keys=pygame.key.get_pressed()
           if keys[pygame.K_LEFT]:
               self.vx=-5
           if keys[pygame.K_RIGHT]:
               self.vx=5
           self.rect.x+=self.vx
           if self.rect.right>=dw:
               self.rect.right=dw
           if self.rect.left<=0:
               self.rect.left=0
                
    class Ball(pygame.sprite.Sprite):
        def __init__(self,p,w,c):
            super().__init__()
            self.image=pygame.image.load("b1.png")
            self.image=pygame.transform.scale(self.image,[25,25])
            self.image.set_colorkey(White)
            self.rect=self.image.get_rect()
            self.rect.x=200
            self.rect.y=200
            self.p=p
            self.w=w
            self.c=c
            self.vy=3
            self.vx=0
            self.t_collide=False
            self.b_collide=False
            self.score=0
        def hit_wall(self):
            hits=pygame.sprite.groupcollide(balls,self.c.walls,False,True)
            
            
            if hits:
                
                return True
            else:
                return False
        def hit_player(self):
            hits=pygame.sprite.spritecollide(self.p,balls,False)
            if hits:
                
                    return True
            else:
                return False
        def Score(self):
            msg("Score:"+str(self.score),Blue,30,200,10)
        def update(self):
           if self.rect.left<=0:
               if self.t_collide:
                   self.vx=random.randrange(1,3)
                   self.vy=3
                   self.t_collide=False
               elif self.b_collide:     
                   self.vx=random.randrange(1,3)
                   self.vy=-3
                   self.b_collide=False
           elif self.rect.top<=0 :
               self.t_collide=True
               self.vx=random.randrange(-3,3)
               self.vy=3
           elif self.rect.right>=dw:
               if self.t_collide:
                   self.vx=random.randrange(-3,-1)
                   self.vy=3
                   self.t_collide=False
               elif self.b_collide:     
                   self.vx=random.randrange(-3,-1)
                   self.vy=-3
                   self.b_collide=False
           elif self.hit_player():
               self.vx=random.randrange(-3,3)
               self.vy=-3
               self.b_collide=True
           elif self.hit_wall():
               self.vx=random.randrange(-3,3)
               self.vy=3
               self.score+=1
               self.t_collide=True
            
           self.rect.x+=self.vx
           self.rect.y+=self.vy
                
    class Walls(pygame.sprite.Sprite):
        def __init__(self,x,y):
            super().__init__()
            self.image=pygame.Surface([40,20])
            self.image.fill(Green)
            self.rect=self.image.get_rect()
            self.rect.x=x*20
            self.rect.y=y*20
    def intro():
    
        screen.fill(White)
        msg("Brick Breaker",Red,40,200,100)
        icon=pygame.image.load("bimg1.png")
        icon=pygame.transform.scale(icon,[200,150])
        screen.blit(icon,[100,130])
        wait=1
        
        while wait:
            cur=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    back_to_hub()
        
            if  70+65>cur[0]>70 and 320+40>cur[1]>320:
                pygame.draw.rect(screen,Blue,[70,320,65,40]  )
                if click[0]==1:
                    wait=0
            else:
                pygame.draw.rect(screen,Aqua,[70,320,65,40]  )
                
            msg("Start",Red,30,100,340)
    
            if 270+60>cur[0]>270 and 320+40>cur[1]>320:
                 pygame.draw.rect(screen,Blue,[270,320,60,40])
                 if click[0]==1:
                    back_to_hub()
            else:
                pygame.draw.rect(screen,Aqua,[270,320,60,40])
        
            msg("Exit",Red,30,300,340)
            pygame.display.flip()
    def pause():
        paused=True
        screen.fill(White)
        msg("Paused",Red,40,200,100)
        while paused:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        paused=0
            pygame.display.flip()
    class Map:
        def __init__(self,map_file):
            self.map_file=map_file
            self.map_data=[]
            self.walls=pygame.sprite.Group()
        def update(self):
            with open(self.map_file,'r+') as f:
              for line in f:
                  self.map_data.append(line)
            for row ,tiles in enumerate(self.map_data):
                for col,tile in enumerate(tiles):
                        if tile=='1':
                            self.w=Walls(col,row)
                            self.walls.add(self.w)
                            all_sprites.add(self.walls)
    
    running=True
    start=True
    level=False
    gover=False
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    
    
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pause()
        if start :
            intro()
            start=False
            all_sprites=pygame.sprite.Group()
            balls=pygame.sprite.Group()
            walls=pygame.sprite.Group()
            p=Player(200,350)
            all_sprites.add(p)
            c=Map("map1.txt")
            c.update()
                     
    
            b=Ball(p,c.w,c)
            balls.add(b)
            all_sprites.add(b)
        if level:
            level=False
            all_sprites=pygame.sprite.Group()
            balls=pygame.sprite.Group()
            walls=pygame.sprite.Group()
            p=Player(200,350)
            all_sprites.add(p)
            c=Map("map.txt")
            c.update()              
            b=Ball(p,c.w,c)
            balls.add(b)
            all_sprites.add(b)
            
        if gover:
            gover=False
            all_sprites=pygame.sprite.Group()
            balls=pygame.sprite.Group()
            walls=pygame.sprite.Group()
            p=Player(200,350)
            all_sprites.add(p)
            c=Map("map1.txt")
            c.update()
            b=Ball(p,c.w,c)
            balls.add(b)
            all_sprites.add(b)
        all_sprites.update()
        if len(c.walls.sprites())<=0:
            level=True
            
        screen.fill(White)
        if b.rect.bottom>=dh:
            screen.fill(White)
            msg("Game Over!",Red,40,200,200)
            p.kill()
            b.kill()
            all_sprites.remove(c.walls)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    back_to_hub()
    #==============================================================================              
                if event.type == pygame.MOUSEBUTTONUP:#Code added by LG
                    pos = pygame.mouse.get_pos()#Code added by LG
                  
                    if pos[0] in range(75, 330) and pos[1] in range(270, 330): #Code added by LG
                        back_to_hub() #Code added by LG     
                  #quit button                 
            large_font = pygame.font.Font(None, 60) #Code added by LG
            text_quit = large_font.render('Quit to hub', True, 'White') #Code added by LG
            quit_rect = text_quit.get_rect(midtop = (200, 280)) #Code added by LG
            pygame.draw.rect(screen, 'Black', (75,270,255,60)) #Code added by LG
            screen.blit(text_quit, quit_rect) #Code added by LG
    #==============================================================================
        all_sprites.draw(screen)
        b.Score()
        pygame.display.flip()