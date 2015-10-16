




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

img = pygame.image.load('sample-tileset.png')
img_x=10
img_y=10

while True :
   setDisplay.blit(img,(img_x,img_y))
   for event in pygame.event.get() :
       if event.type == QUIT:
          pygame.quit()
          sys.exit()

   pygame.display.update()
















