import pygame
import random
#initial setup
pygame.init()
clock = pygame.time.Clock()
#game window
screen_height = 700
screen_width = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

#snake
length = 30
snake = pygame.Rect(screen_width/2, screen_height/2, length, 30)

red = (255, 0, 0)
black = (0,0,0)
speed = 5
#food
food = pygame.Rect(random.randint(1, screen_width-10), random.randint(1, screen_height-10), 15, 15)
pink = (255, 192, 203)

#game loop
while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        snake.x += speed
    if keys[pygame.K_a]:
        snake.x -= speed
    if keys[pygame.K_w]:
        snake.y -= speed
    if keys[pygame.K_s]:
        snake.y += speed
    #if snake eat food, food spawn random and snake increase length
    if snake.colliderect(food):
        length +=30
        screen.fill(black)
        food = pygame.Rect(random.randint(1, screen_width-10), random.randint(1, screen_height-10), 15, 15)
        snake = pygame.Rect(screen_width/2, screen_height/2, length, 30)

    screen.fill(black)
        
    pygame.draw.rect(screen, red, snake)
    pygame.draw.rect(screen, pink, food)
    #updating window
    pygame.display.flip()
    clock.tick(60)