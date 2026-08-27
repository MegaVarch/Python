import Pygame

Pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = Pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
Pygame.display.set_caption('Adding image and background image')

background_image = Pygame.transform.scale(
    Pygame.image.load('all-white-background.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = Pygame.transform.scale(
    Pygame.image.load('lambo.jfif').convert_alpha(), (200.200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30 ))

text = Pygame.font.Font(None, 36).render('Hello World', True, Pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = Pygame.time.Clock()
    running = True
    while running:
        for event in Pygame.event.get():
            if event.type == Pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)

        Pygame.display.flip()

        clock.tick(30)

    Pygame.quit()

if __name__ == '__main__':
    game_loop()




