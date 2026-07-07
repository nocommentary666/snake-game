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
snake = pygame.Rect(screen_width/2, screen_height/2, 30, 30)
red = (255, 0, 0)
black = (0,0,0)
speed = 5
#food
food = pygame.Rect(random.randint(1, screen_width), random.randint(1, screen_height), 15, 15)
pink = (255, 192, 203)

#game loop
while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        snake.x += speed
    if keys[pygame.K_a]:
        snake.x -= speed
    if keys[pygame.K_w]:
        snake.y -= speed
    if keys[pygame.K_s]:
        snake.y += speed
    if snake.colliderect(food):
        print("snake eat food")
    screen.fill(black)
        
    pygame.draw.rect(screen, red, snake)
    pygame.draw.rect(screen, pink, food)
    #updating window
    pygame.display.flip()
    clock.tick(60)