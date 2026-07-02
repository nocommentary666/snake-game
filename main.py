import pygame

#initial setup
pygame.init()
clock = pygame.time.Clock()
#game window
screen_height = 800
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

#snake
snake = pygame.Rect(screen_width/2, screen_height/2, 30, 30)
red = (255, 0, 0)
speed = 5

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
        
    pygame.draw.rect(screen, red, snake)
    #updating window
    pygame.display.flip()
    clock.tick(60)