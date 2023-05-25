import pygame as pg
import random

SCREENSIZE = (600,600)
pg.init()
screen = pg.display.set_mode(SCREENSIZE)
pg.display.set_caption('Forca')
clock = pg.time.Clock()
running = True
GAMESTATE = 'jogo'
# jogo
# gameover
mensagem = ''

img_coracao = pg.image.load('coracao.png')
img_coracao = pg.transform.scale(img_coracao, (64,64))
vidas = 6

palavras = ['banana','palmeiras','cuscuz','teclado','cachorro','vaca', 'naruto','cleiton','emidio','dias','macaco','computador','charuto','uva','ovo','fluminence','sapato']

palavra_escolhida = random.choice(palavras)
resposta = []
for i in range(len(palavra_escolhida)):
    resposta.append('_')

def novo_jogo():
    global palavra_escolhida, resposta
    palavra_escolhida = random.choice(palavras)
    
    resposta = []
    for i in range(len(palavra_escolhida)):
        resposta.append('_')

def mostrar_texto(texto,tamanho,pos):
    font = pg.font.Font('Minecraft.ttf',tamanho)
    text = font.render(texto,True,(255,255,255),)
    textRect = text.get_rect()
    textRect.center = (pos[0], pos[1])
    screen.blit(text,textRect)



while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:

            if GAMESTATE == 'jogo':
                tecla = pg.key.name(event.key)
                for i in range(len(palavra_escolhida)):
                    if tecla == palavra_escolhida[i]:
                        resposta[i] = tecla
                if tecla not in list(palavra_escolhida):
                    vidas-=1

            

            # debug
            '''
            if event.key == pg.K_a:
                if GAMESTATE == 'jogo':
                    GAMESTATE = 'gameover'
                else:
                    GAMESTATE = 'jogo'
            if event.key == pg.K_d:
                novo_jogo()
            '''
    
    # ------------- TICK -------------
    if GAMESTATE == 'jogo':
        if vidas <= 0:
            GAMESTATE = 'gameover'
        if '_' not in resposta:
            GAMESTATE = 'gameover'
            mensagem = f'Parabens você acertou a palavra! A palavra era'
    
    elif GAMESTATE == 'gameover':
        if '_' in resposta:
            mensagem = f'GAMEOVER! A palavra era'

    
    screen.fill((47,69,65))
    # ------------- RENDER -------------
    if GAMESTATE == 'jogo':
        mostrar_texto(''.join(resposta), 64, [300,400])

        for i in range(vidas):
            screen.blit(img_coracao,[20+75*i, 50])
    
    elif GAMESTATE == 'gameover':
        mostrar_texto(mensagem, 32, [300,50])
        mostrar_texto(palavra_escolhida.upper(), 64, [300, 100])
    

    pg.display.flip()
    clock.tick(60)

pg.quit()