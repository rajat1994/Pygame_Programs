




import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black =(0,0,0)
red =(255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

setDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption('epic game')

FPS = 4500
img = pygame.image.load('hk.png')
FPS = 30
img_x=50
img_y=50
pixMove = 10
movement = 'down'

fpsTime = pygame.time.Clock()

while True :
   setDisplay.fill(black)
   if  movement == 'down' :
      img_y+= pixMove
      if img_y > 400 :
            movement = 'right'
   elif movement == 'right' :
        img_x += pixMove
        if img_x > 400 :
            movement = 'up'
   
   elif movement == 'up':
        img_y -= pixMove
        if img_y < 30:
            movement = 'left'
            
   elif movement == 'left' :
    img_x -= pixMove
    if img_x < 30 :
        movement = 'down'

       
   setDisplay.blit(img,(img_x,img_y))
   for event in pygame.event.get() :
       if event.type == QUIT:
          pygame.quit()
          sys.exit()

   pygame.display.update()
   fpsTime.tick(FPS)







