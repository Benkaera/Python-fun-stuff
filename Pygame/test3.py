# Рисует красный прямоугольник

import pygame
pygame.init()
print(pygame.font.get_fonts())

W, H = 600, 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Не знаю что это - первая игра")
pygame.display.set_icon(pygame.image.load("ico.bmp"))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Текст по центру
f = pygame.font.SysFont('arial', 36)
sc_text = f.render('Рисуй - тяни', 1, BLACK, GREEN)
poss = sc_text.get_rect(center=(W//2, H//2))

clock = pygame.time.Clock()
FPS = 60


flStartDraw = False
sp = ep = None

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            pos = pygame.mouse.get_pos()

            if sp is None:
                sp = pos

            width = pos[0] - sp[0]
            height = pos[1] - sp[1]

            sc.fill(BLUE)
            sc.blit(sc_text, poss)
            pygame.draw.rect(sc, GREEN, pygame.Rect(sp[0], sp[1], width, height), 2)
            pygame.display.update()

        else:
            sp = None

    clock.tick(FPS)

print("Спасибо за игру")