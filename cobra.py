# Bibliotecas Necessárias
import pygame
import random

# Configurações Iniciais
pygame.init()
pygame.display.set_caption("Snake")
largura, altura = 1200, 800 # Definindo largura e altura da tela
tela = pygame.display.set_mode((largura,altura)) # Utilizando a largura e a altura para definir o tamanho da tela.
relogio = pygame.time.Clock() # Criando uma função de relógio.

# Cores (Padrão RGB)
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Definições do jogo
tamanho_quadrado = 20 #Quantos pixels um bloco da cobra e da comida ocupam na tela.
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Roboto", 25)
    texto = fonte.render(f"Pontuação: {pontuacao}", True, branca)
    tela.blit(texto, [5, 5])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

# Criar loop infinito
def rodar_jogo():
    fim_jogo = False

    x = largura / 2 #Posição Inicial da cobra no eixo X
    y = altura / 2 # Posição inicial da cobra no eixo Y

    velocidade_x = 0 #Velocidade inicial da cobra no eixo x
    velocidade_y = 0 #Velocidade inicial da cobra no eixo y

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Desenho dos objetos do jogo na tela
        desenhar_pontuacao(tamanho_cobra - 1)

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #> Caso a cobra bata na parede, finalizar o jogo
        if x < 0 or x >= largura - 1 or y < 0 or y >= altura - 1:
            fim_jogo = True
        
        #> Atualizar Posição da Cobra
        x += velocidade_x
        y += velocidade_y

        #Desenhar Cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]: #Verificação se a cobra bateu em si mesma.
            if pixel == [x, y]: #Se o pixel encontrar consgo mesmo
                fim_jogo = True #Fim de jogo

        desenhar_cobra(tamanho_quadrado, pixels)

        # Atualização da Tela
        pygame.display.update()


        #Nova Comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        #Passar o tempo
        relogio.tick(velocidade_jogo)

rodar_jogo()