from BallBounce import BallBounce
import pygame
import sys

#Used to enter / exit game loop
running = True

#Asking user for inputs
print('Enter initial velocity (pixels per second)')
velo = input()
print('Enter angle in degrees (pixels per second)')
angle = input()

#Creating a ball in ballBounce
ball = BallBounce(int(velo), int(angle))
   

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Ball Bouncing by Neel Patel")



pygame.draw.circle(screen, (0, 200, 255), (20, 20), 20, 0) 

#Running the code every 17 ms
while running:
    pygame.time.delay(17)
    #for loop used to check if user clicks x button
    for event in pygame.event.get():
        #Stop loop
        if event.type == pygame.QUIT:
            running = False
    ball.fall()
    ball.Collision()
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 200, 255), (ball.returnXPos(), ball.returnYPos()), 20, 0) 
    pygame.display.update()
    
    

    
# Quit Window
pygame.quit()
sys.exit()
    