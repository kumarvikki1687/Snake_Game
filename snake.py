import pygame
import time
import random
pygame.init() #initialise pygame
score=0
screen=pygame.display.set_mode((700,500)) #create frame
pygame.display.set_caption("Score :  "+str(score)+ "     SNAKE GAME")

white=(255,255,255) #color code
black=(0,0,0)
red=(255,0,0)
aqua=(0,255,255)
green=(0,155,0)
gameExit=False
clock=pygame.time.Clock()
#cat=pygame.image.load('cat1.jpg')
x=300
y=300
x_change=0
y_change=0
randX=round(random.randint(0,690)/20.0)*20.0
randY=round(random.randint(0,490)/20.0)*20.0

snakelist=[]
snakelength=1

font=pygame.font.SysFont(None,50) #define font and set size of font
font1=pygame.font.SysFont(None,20)

def print_msge(msg,score,color,color1):
    text=font.render(msg,True,color)
    text1=font.render("Your score is " + str(score),True,color)
    text2=font1.render("Try better next time :) ",True,color1)
    screen.blit(text,(200,200))
    screen.blit(text1,(250,230))
    screen.blit(text2,(270,290))
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(5)
def snake(d,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(screen,black,[XnY[0],XnY[1],d,d]) #graw rect inside the screen
while not gameExit:
    for i in pygame.event.get(): #any type of events done on window
        if i.type==pygame.QUIT:
            gameExit=True
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                x_change=-20
                y_change=0 #keep y-coordinate same
            elif i.key==pygame.K_RIGHT:
                x_change=20
                y_change=0 #keep y-coordanate same
            elif i.key==pygame.K_UP:
                y_change=-20
                x_change=0 #keep x-coordinate same
            elif i.key==pygame.K_DOWN:
                y_change=20
                x_change=0 #keep x_coordinate same
    if x>680 or x<0 or y>480 or y<0:
        gameExit=True
    x+=x_change
    y+=y_change
    screen.fill(aqua) #fill the screen
    
    if gameExit==False:
        pygame.draw.rect(screen,red,[randX,randY,20,20])
        #pygame.draw.rect(screen,green,[x,y,20,20]) #graw rect inside the screen
        snakeHead=[]
        snakeHead.append(x)
        snakeHead.append(y)
        snakelist.append(snakeHead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment==snakeHead:
                gameExit=True
        snake(20,snakelist)
    pygame.display.update() #update everytime
    if x==randX and y==randY:
        randX=round(random.randint(0,690)/20.0)*20.0
        randY=round(random.randint(0,490)/20.0)*20.0
        snakelength+=1
        score+=1
        pygame.display.set_caption("Score :  "+str(score)+ "     SNAKE GAME")
        pygame.display.update()
        #print "om nom nom"
    clock.tick(7)
#pygame.mixer.music.pause()
pygame.display.update()
print_msge("You lose",score,red,black)
pygame.display.update()
time.sleep(5) #wait for 5sec to display text
pygame.quit()
quit()
