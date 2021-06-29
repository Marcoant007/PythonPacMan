import pygame

pygame.init()
Amarelo = (255,255, 0)
Preto = (0,0,0)
Velocidade = 1
Raio = 30
x = 10
y = 10
velocidade_x = Velocidade
velocidade_y = Velocidade

#Criar janela grafica

tela = pygame.display.set_mode((640, 489), 0)
while True:
    x = x + velocidade_x
    y = y + velocidade_y

    if x + Raio > 640:
        velocidade_x = -Velocidade
    if x - Raio < 0:
        velocidade_x = Velocidade
    if y + Raio > 480:
        velocidade_y = -Velocidade
    if y - Raio < 0:
        velocidade_y = Velocidade



    tela.fill(Preto)#Colocado cor da tela

    pygame.draw.circle(tela, Amarelo, (int(x), int(y)), Raio, 0)
    pygame.display.update()


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()