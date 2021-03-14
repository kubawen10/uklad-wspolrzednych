import pygame

running = True
pygame.init()
surface = pygame.display.set_mode((1400, 902))
pygame.display.set_caption("Układ!")
fpsClock = pygame.time.Clock()
FPS=20

while running:
    surface.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()

