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
snake = [(screen_width/2, screen_height/2)]
direction = (length, 0)

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
        direction = (length, 0)
    if keys[pygame.K_a]:
        direction = (-length, 0)
    if keys[pygame.K_w]:
        direction = (0, -length)
    if keys[pygame.K_s]:
        direction = (0, length)
    
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)
    
    head_rect = pygame.Rect(new_head[0], new_head[1], length, length)

    screen.fill(black)
    #if snake eat food, food spawn random and snake increase length
    if head_rect.colliderect(food):
        screen.fill(black)
        food = pygame.Rect(random.randint(1, screen_width-10), random.randint(1, screen_height-10), 15, 15)
    else:
        snake.pop()
    #draw snake
    for pos in snake:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], length, length))
        
    pygame.draw.rect(screen, pink, food)
    #updating window
    pygame.display.flip()
    clock.tick(10)