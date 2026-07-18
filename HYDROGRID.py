import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

water_x = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((240,240,240))

    # Pipe
    pygame.draw.rect(screen, (80,80,80), (50,220,700,20))

    # Water
    pygame.draw.circle(screen, (0,150,255), (water_x,230), 10)

    water_x += 3
    if water_x > 750:
        water_x = 50

    pygame.display.update()
    clock.tick(60)

pygame.quit()