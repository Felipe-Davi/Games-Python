import pygame
from random import randint

pygame.init()
x = 360  # max 530 min min 230 era 380
y = 100  # era 100
pos_x = 500
pos_y = 800
pos_y_a = 800
pos_y_c = 2500
timer = 0
time_sec = 0

vel_outros = 12

vel = 10
rua = pygame.image.load('rua.PNG')
carro = pygame.image.load('carrinho.png')
carro2 = pygame.image.load('carro3.png')
carro3 = pygame.image.load('carro2.png')
carro4 = pygame.image.load('carro4.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 480:
        x += vel
    if comandos[pygame.K_LEFT] and x >= 220:
        x -= vel

    #           verifica a colisao
    if ((x + 80 > pos_x and y + 180 > pos_y)):
        y = 1200

    if ((x - 80 < pos_x - 300 and y + 180 > pos_y_a)):
        y = 1200

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c)) and ((x - 80 < pos_x - 136 and y + 180 > pos_y_c)):
        y = 1200

    if (pos_y <= -80):
        pos_y = randint(800, 1000)

    if (pos_y_a <= -80):
        pos_y_a = randint(1200, 2000)

    if (pos_y_c <= -80):
        pos_y_c = randint(2200, 3000)

    if (timer < 20):
        timer += 1
    else:
        time_sec += 1
        texto = font.render("Tempo: " + str(time_sec), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y -= vel_outros
    pos_y_a -= vel_outros + 2
    pos_y_c -= vel_outros + 10  # carro preto

    janela.blit(rua, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(carro2, (pos_x, pos_y))
    janela.blit(carro3, (pos_x - 250, pos_y_a))
    janela.blit(carro4, (pos_x - 136, pos_y_c))
    janela.blit(texto, pos_texto)
    pygame.display.update()
