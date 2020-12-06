import pygame
import random
import time

pygame.init()

height = 600
width = 800

clock = pygame.time.Clock()

y = -20
ly = 0.1

side = 20


gameDisplay = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0, 125)
green = (0,255,0)
brown = (255,183,25)
lred = (255,153,153)

a = (255,255,102)
b = (0,204,204)


held  = 0

img = pygame.image.load('back.png')
img2 = pygame.image.load('blue_block.png')
img3 = pygame.image.load('red_block.png')
img4 = pygame.image.load('flames.png')
img5 = pygame.image.load('gameover.png')
img6 = pygame.image.load('main.gif')

color =  brown
color1 = lred
color2 = green


radius1  = 70
radius2 = 40

font = pygame.font.SysFont(None,25)
font1 = pygame.font.SysFont(None,50)
font2 = pygame.font.SysFont(None,30)
sound=pygame.mixer.music.load("music.mp3")

def textobjects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface  
def message(msg,color,ydisplace):
    textSurf = textobjects(msg,color)
    textRect = textSurf.get_rect()
    textRect.center = (width/2),(height/2)+ydisplace
    gameDisplay.blit(textSurf, textRect)
def message1(msg,color,center):
    screen_text = font2.render(msg,True,color)
    gameDisplay.blit(screen_text,center)

gameExit = False
i = random.randrange(1,3)
def score(sc):
    text = font.render("score:"+str(sc),True,red)
    gameDisplay.blit(text,[0,5])
def score1(sc):
    text = font1.render("score:"+str(sc),True,red)
    gameDisplay.blit(text,[350,10])
def mes():
    text = font.render("press escape to pause",True,white)
    gameDisplay.blit(text,[0,20])
                     
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
                
            x,y = pygame.mouse.get_pos()
            c = pygame.mouse.get_pressed()
            if (x >=330 and x <= 470) and (y>=430 and y <=570):
                color1 = red
                radius1 = 85
                if c[0]==1:    
                    intro=False
                    return 1
            else:
                color1 = lred
                radius1 = 70
            if x >= 560 and x<= 640 and y >= 460 and y <= 540:
            
                color2 = green
                radius2 = 50
                if c[0]==1:
                    return 0
            else:
                color2 = b
                radius2 = 60
                    
        gameDisplay.blit(img6,[0,0])
        pygame.draw.circle(gameDisplay,color2,[400,500],radius1,0)
        pygame.draw.circle(gameDisplay,color1,[600,500],radius2,0)

        message1("PLAY",blue,[380,500])
        message1("EXIT",blue,[580,500])

        pygame.display.update()
        clock.tick(15)

def gameover():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return(1)
                if event.key == pygame.K_q:
                    return(0)
        gameDisplay.blit(img5,[0,0])
        score1(sc)
        pygame.display.update()
        clock.tick(15)
    
def pause():
    paused=True
    while paused == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    paused = False
                if event.key == pygame.K_q:
                    gameover()
                    
        message("PAUSED",white,-100)
        message("press E to continue or Q to quit",white,20)
        pygame.display.update()
        clock.tick(5)
        
    
sc = 0
pygame.mixer.music.play(-1)
def gameloop(ly,sc):
    i = random.randrange(1,3)
    gameExit = False
    
    
    
    k = random.randrange(1,4)
    if k == 1:
        randx = 384
        y = 70
    elif k == 2:
        randx = 150
        y = 90
    else:
        randx = 600
        y = 100

    side = 40

    
    
    held  = 0


    xp = randx
    yp =y

    while not gameExit:
            
                
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                    
                            gameExit = True
                            pygame.quit()
                            quit()
                            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pause()
                    
                    xa,ya = pygame.mouse.get_pos()
                    
                    b = pygame.mouse.get_pressed()
                    if xa > xp and xa < xp+40:
                            if ya > yp and ya < yp+40:
                                    if b[0] == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                                            held = 1
                    if event.type == pygame.MOUSEBUTTONUP:
                            held = 0
                    if held == 1:
                            xp,yp = pygame.mouse.get_pos()
                 
                    

            if xp > -100 and xp < 60 and yp > 150 and yp < 350 and i%2 != 0:
                            xp = -1000
                            
                            
            elif xp > 740 and yp > 200 and yp < 350 and i%2 == 0:
                            xp = -1000
                            

          
            

            
            if xp > -10 and yp >= 540:
                    
                    gameExit = True
            if xp < 0:
                sc = sc + 1
                break
            
                
                
                
                              
            if xp > 0 and xp < 60 and yp > 200 and yp < 350 and i%2 == 0:
                            gameExit = True
                            
                            
            if xp > 740 and yp > 200 and yp < 350 and i%2 != 0:
                            gameExit = True
                            
                    
            yp+=ly
            
            gameDisplay.blit(img,[0,0])
            gameDisplay.blit(img4,[0,450])
            gameDisplay.blit(img3,[xp,yp])
            if i%2 == 0:
                
                    gameDisplay.blit(img2,[xp,yp])

            
        
            
            score(sc)
            mes()
            pygame.display.update()

    if gameExit == True:
        return(0)
    else:
        return(1)
            
  

j = game_intro()
while i < 20 and j == 1:
    j=gameloop(i,sc)
    if j == 0:
        j = gameover()
        i = 0.9
        sc = 0
    else:
        sc = sc + 1
    i = i + 0.8
    
pygame.quit()
quit()
