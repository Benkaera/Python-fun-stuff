import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Не знаю что это - первая игра")
pygame.display.set_icon(pygame.image.load("ico.bmp"))

flRunning = True

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
pygame.draw.rect(sc, BLUE, (10, 10, 50, 100), 2)
pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 4)
pygame.draw.circle(sc, BLUE, (300, 250), 40)

pi = 3.14
pygame.draw.arc(sc, GREEN, (450, 30, 90, 150), pi, 2*pi, 5)

pygame.display.update()

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

    # pygame.time.delay(20)
    clock.tick(FPS)

print("Спасибо за игру")