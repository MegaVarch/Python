import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 40, 40)

speed_x = 3
speed_y = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.x += speed_x
    player.y += speed_y

    if player.right > 600 or player.left < 0:
        speed_x = -speed_x

    if player.bottom > 400 or player.top < 0:
        speed_y = -speed_y

    screen.fill("black")
    pygame.draw.rect(screen, "red", player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()