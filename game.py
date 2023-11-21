import pygame
pygame.init()
xr=-500
width = 1000
height = 500
red = (255,0,0)
white = (255, 255, 255)
flash = 1
R = 255
G = 255
B = 255
variable = True
#loop = 0

#Initialize Screen
screen = pygame.display.set_mode((width,height))

titleFont = pygame.font.Font('roman.otf', 30)#sets font
title = titleFont.render('START', True, red, white) #sets colour and text
titleRect = title.get_rect()
titleRect.center = (500, 250)




done=False
#Game Loop
while True : # start screen rectangle slides into place when it hits place lighting strikes screen turns white and everything appears
    #Game closes when you click little x
    #while loop == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

            done = True
            break
        
    #Make Background pink
    screen.fill((0,0,0))
    #Draw Rectangle
    pygame.draw.rect(screen,(255,255,255),(xr,125,500,100))
      #If rect x is less than 250
    if xr<=250:
        #Move Rect
        xr+=0.5
    if xr==(250.5):
        loop=1
            
  #  while loop == 1:
    if xr==250.5 and R>=1:
        
        screen.fill((R,G,B))
        R-=0.25
        G-=0.25
        B-=0.25
           
            
        screen.blit(title, titleRect)
        print(R)

      
            
    if done==True :
        break 
    
    pygame.display.flip()
    if R == .75:
        loop=5
        if loop==5:
            print("hi")
        
        
    
pygame.quit()
quit()