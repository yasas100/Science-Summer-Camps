import pygame 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((600,600))
pygame.display.set_caption("Yasas Game")
gameExit = False
lead_x=300 
lead_y=300
lead_x_change=0 
lead_y_change=0 
clock = pygame.time.Clock()


while(not gameExit):
    for event in pygame.event.get(): ##Event handeling loop
        if (event.type == pygame.QUIT):##Quit Event 
            gameExit = True
        if (event.type == pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                lead_x_change-=10
                lead_y_change=0
            if (event.key == pygame.K_RIGHT):
                lead_x_change+=10 
                lead_y_change=0
            if (event.key==pygame.K_UP):
                lead_y_change-=10
                lead_x_change=0
            if (event.key==pygame.K_DOWN):
                lead_y_change+=10
                lead_x_change=0
    if (lead_x>=600 or lead_x<=0 or lead_y<=0 or lead_y>=600):
        gameExit = True
    
        
                
        """if (event.type == pygame.KEYUP): ##used for continous movement
            if (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                lead_x_change=0"""
                
    lead_x+=lead_x_change
    lead_y+=lead_y_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black, [lead_x,lead_y,10,10] )
    pygame.display.update()
    clock.tick(10)
pygame.quit()  