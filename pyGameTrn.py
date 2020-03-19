import pygame
from random import randrange

black = (20, 20, 20)
fullblack = (0, 0, 0)
white = (255, 255, 255)
green = (0, 205, 0)
orange = (255, 102, 0)
blue = (51, 102, 255)
red = (255, 0, 0)

try:
    pygame.init()   #inicia pygame
    print("PyGame OK!")
except:
    print("Erro ao iniciar o PyGame.")

lar = 320
alt = 280   #altura e largura da tela
size = 10#tamanho da cobra

clock = pygame.time.Clock() #relogio
fundo = pygame.display.set_mode((lar, alt)) #inicializa a tela
pygame.display.set_caption("Snake Trn")    #edita titulo e icone da janela

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(posXY):
    for XY in posXY:
        pygame.draw.rect(fundo, green, (XY[0], XY[1], size, size) ) #desenha a cobra

def maca(posX, posY):
    pygame.draw.rect(fundo, orange, (posX, posY, size, size) ) #desenha a maçã

def jogo():
    gameOver = False
    posX = randrange(0, lar-size,10 )
    posY = randrange(0, (alt-40)-size,10 ) #posição inicial

    mposX = randrange(0, lar-size,10 )
    mposY = randrange(0, (alt-40)-size,10 )#posição da maçã

    velocidade = 10
    velX = 0
    velY = 0
    posXY = []
    comp = 1
    score = 0;

    render = True
    while render:
        
        while gameOver: #codigo do game over
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    render = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameOver = False
                        posX = randrange(0, lar-size,10 )
                        posY = randrange(0, (alt-40)-size,10 ) 
                        mposX = randrange(0, lar-size,10 )
                        mposY = randrange(0, (alt-40)-size,10 )
                        velocidade = 10
                        velX = 0
                        velY = 0
                        posXY = []
                        comp = 1
                        score = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex = pygame.mouse.get_pos()[0]
                    mousey = pygame.mouse.get_pos()[1]
                    if (mousex > 65 and mousey > 120) and (mousex < 255 and mousey < 147):
                        gameOver = False
                        posX = randrange(0, lar-size,10 )
                        posY = randrange(0, (alt-40)-size,10 ) 
                        mposX = randrange(0, lar-size,10 )
                        mposY = randrange(0, (alt-40)-size,10 )
                        velocidade = 10
                        velX = 0
                        velY = 0
                        posXY = []
                        comp = 1
                        score = 0
            fundo.fill(white)
            texto("Fim de Jogo!", red, 50, 55, 30)
            texto("Pontos x " + str(score), fullblack, 30, 100, 80)
            pygame.draw.rect(fundo, orange, (65, 120, 190, 27) )
            texto("Continuar(espaço)", white, 30 , 70, 125)
            pygame.display.update()
        for event in pygame.event.get():    #captura a entrada
            if event.type == pygame.QUIT:   #verifica se foi clicado o botao de fechar a janela
                render = False  #Sai do loop
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not velX == velocidade:
                        velX = -velocidade
                        velY = 0
                elif event.key == pygame.K_RIGHT:       #controles
                    if not velX == -velocidade:
                        velX = velocidade
                        velY = 0
                elif event.key == pygame.K_UP:
                    if not velY == velocidade:
                        velX = 0
                        velY = -velocidade
                elif event.key == pygame.K_DOWN:
                    if not velY == -velocidade:
                        velX = 0
                        velY = velocidade
                    
        fundo.fill(black) #preenche o fundo
        
        posX += velX
        posY += velY  #movimentação da cobra

        if posX == mposX and posY == mposY:
            comp += 1
            score += 1
            mposX = randrange(0, lar-size,10 )
            mposY = randrange(0, (alt-40)-size,10 )

        if posX + size > lar:
            gameOver = True
        if posX < 0:
            gameOver = True
                                #bordas
        if posY + size > alt - 40:
            gameOver = True
        if posY < 0:
            gameOver = True
        

        posCabeca = []
        posCabeca.append(posX)
        posCabeca.append(posY)
        posXY.append(posCabeca)
        if len(posXY) > comp:
            del posXY[0]
        if any(Bloco == posCabeca for Bloco in posXY[:-1]):
            gameOver = True

        pygame.draw.rect(fundo, fullblack, (0, alt-40, lar, 40) ) #desenha o placar
        texto("Pontuação:" + str(score), white, 18, 10, alt-30)
        
        cobra(posXY)
        maca(mposX, mposY)
        if velX == 0 and velY == 0:
            texto("START!", blue, 18, lar/10, alt/2)
        pygame.display.update() #atualiza a tela
        clock.tick(15)  #limitação de fps


        

    ######
jogo()
pygame.quit()   #fecha o pygame
