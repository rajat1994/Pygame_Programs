

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

setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('epic game')

singlePixel = pygame.PixelArray(setDisplay)

setDisplay.fill(cyan)
singlePixel[3 ][3] = black
pygame.draw.line(setDisplay,blue,(389,200),(300,70),4)
pygame.draw.circle(setDisplay,red,(50,50),20)
pygame.draw.rect(setDisplay,purple,(100,100,200,100))
pygame.draw.polygon(setDisplay,green,((50,20),(30,40),(60,100)))
while True :
   for event in pygame.event.get() :
       if event.type == QUIT:
          pygame.quit()
          sys.exit()

   pygame.display.update()






