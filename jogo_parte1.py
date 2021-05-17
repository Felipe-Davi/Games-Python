import pygame

pygame.init()
x = 350
y = 300
pos_x = 250
pos_y = 300
vel = 15
vel_other = 20
fundo = pygame.image.load('rua.PNG')
carro = pygame.image.load('carrinho.png')
carro2 = pygame.image.load('carro2.png')
carro3 = pygame.image.load('carro3.png')
carro4 = pygame.image.load('carro4.png')

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Criando um jogo com Python')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= vel
    if comandos[pygame.K_DOWN]:
        y += vel
    if comandos[pygame.K_RIGHT]:
        x += vel
    if comandos[pygame.K_LEFT]:
        x -= vel

    if (pos_y <= -200):
        pos_y = 600

    pos_y -= vel_other

    janela.blit(fundo, (0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro2,(pos_x,pos_y))
    janela.blit(carro3, (pos_x + 110, pos_y ))
    janela.blit(carro4, (pos_x + 220, pos_y ))

    pygame.display.update()

pygame.quit()
