#galaga tractor beam code

import pygame #bring in pygame library
import random
pygame.init #initialize pygame
pi = 3.1415
screen = pygame.display.set_mode((800, 1000)) #create game screen
pygame.display.set_caption("galaga beam") #window title

#load alien ship image
alienShip = pygame.image.load("boss.jpg")

#draw alien ship
screen.blit(alienShip, (210, 180))
pygame.display.flip()

#top arc

def arcmaker(a,b,c,d,e):
    pygame.draw.arc(screen, (5, a, 200), (b, c, d, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(e)
def arcmaker2(a,b,c,d,e):
    pygame.draw.arc(screen, (5, a, 200), (b, c, d, 100),  pi, 2*pi, 10)
    pygame.display.flip() #update screen 
    pygame.time.wait(e)
b = 200
c = 200
d = 100
for i in range(100):
    for i in range(6):
        arcmaker(100, b, c, d, 400)
        b-=10
        c+=30
        d+=20
        arcmaker2(200, b, c, d, 400)
        b-=10
        c+=30
        d+=20
#pygame.draw.arc(screen, (5, 100, 200), (200, 200, 100, 100),  pi, 2*pi, 10)
#pygame.display.flip() #update screen 
#pygame.time.wait(800)

##second arc
#pygame.draw.arc(screen, (5, 200, 200), (190, 230, 120, 100),  pi, 2*pi, 10)
#pygame.display.flip() #update screen 
#pygame.time.wait(800)

##last arc
#pygame.draw.arc(screen, (5, 100, 200), (115, 400, 300, 100),  pi, 2*pi, 10)
#pygame.display.flip() #update screen 
#pygame.time.wait(800)