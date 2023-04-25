import pygame
from pygame.locals import *
import random

# shape parameters
size = width, height = (600, 800)
road_width = int(width/1.6)
roadmark_width = int(width/80)
# location parameters
right_line = width/2 + road_width/4
left_line = width/2 - road_width/4
# animation parameters
speed = 1

#does not working with speed = 0.5

# initiallize the app
pygame.init()
running = True

#set window size
screen = pygame.display.set_mode(size)
#set title
pygame.display.set_caption("Game1")
#set background color
screen.fill((10, 110, 60))
#apply changes
pygame.display.update()

#load player vehicle
car_one = pygame.image.load("..../car.png")
#resize image
#car_one = pygame.transform.scale(car, (250, 250))
car_one_loc = car_one.get_rect()
car_one_loc.center = right_line, height * 0.8
#load enemy vehicle
car_two = pygame.image.load("..../otherCar.png")
car_two_loc = car_one.get_rect()
car_two_loc.center = left_line, height * 0.2

counter = 0

#game loop
while running:
    counter += 1
    
    # increase game difficulty overtime
    if counter == 2048:    
        speed += 0.15
        counter = 0
        print('Level UP', speed)
        
    #animate enemy
    car_two_loc[1] += speed
    if car_two_loc[1] > height:
        if random.randint(0,1) == 0:
            car_two_loc.center = right_line, -200
        else:
            car_two_loc.center = left_line, -200            
    
    # end game logic
    if car_one_loc[0] == car_two_loc[0] and car_two_loc[1] > car_one_loc[1] -250:
        print("Game Over! YOU LOST!!!")
        break
    
    #event listener
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running=False
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                car_one_loc = car_one_loc.move([-int(road_width/2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                car_one_loc = car_one_loc.move([int(road_width/2), 0])
    # draw road
    pygame.draw.rect(
        screen, 
        (50, 50, 50),
        (width/2-road_width/2, 0, road_width, height)
        )
    # draw centre line
    pygame.draw.rect(
        screen, 
        (255, 240, 60),
        (width/2-roadmark_width/2, 0, roadmark_width, height)
        )
    #left line
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2-road_width/2 + roadmark_width*2, 0, roadmark_width, height)
        )
    #right line
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2+road_width/2 - roadmark_width*3, 0, roadmark_width, height)
        )
    # place car images on the screen
    screen.blit(car_one, car_one_loc)
    screen.blit(car_two, car_two_loc)
    # apply changes
    pygame.display.update()
            
pygame.quit()
