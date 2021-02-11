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
sc_text = f.render('влево-вправо жми', 1, BLACK, GREEN)
poss = sc_text.get_rect(center=(W//4, H//4))

clock = pygame.time.Clock()
FPS = 60

x = W // 2
y = H // 2
speed = 5

flStartDraw = False
flRight = flLeft = False
sp = ep = None

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flRight = flLeft = False
        elif event.type == pygame.MOUSEMOTION:
            # print("Позиция мыши: ", event.pos)
            print("Позиция мыши: ", event.rel)

    if flLeft:
        x -= speed
    elif flRight:
        x += speed

    sc.fill(WHITE)
    sc.blit(sc_text, poss)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)

print("Спасибо за игру")