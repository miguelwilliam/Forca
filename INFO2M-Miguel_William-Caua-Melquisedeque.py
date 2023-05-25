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

img_coracao = pg.image.load('coracao.png')
img_coracao = pg.transform.scale(img_coracao, (40,40))

palavras = ['banana','palmeiras','cuscuz','teclado','cachorro','vaca', 'naruto','cleiton','emidio','dias','macaco','computador']

palavra_escolhida = random.choice(palavras)
resposta = ''
for i in range(len(palavra_escolhida)):
    resposta += '_'

def novo_jogo():
    global palavra_escolhida, resposta
    palavra_escolhida = random.choice(palavras)
    
    resposta = ''
    for i in range(len(palavra_escolhida)):
        resposta += '_'

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
            # debug
            if event.key == pg.K_a:
                if GAMESTATE == 'jogo':
                    GAMESTATE = 'gameover'
                else:
                    GAMESTATE = 'jogo'
            if event.key == pg.K_d:
                novo_jogo()
    
    # ------------- TICK -------------
    if GAMESTATE == 'jogo':
        pass
    
    elif GAMESTATE == 'gameover':
        pass

    screen.fill((47,69,65))
    # ------------- RENDER -------------
    if GAMESTATE == 'jogo':
        mostrar_texto(resposta, 50, [300,500])
        screen.blit(img_coracao, [10,10])
    
    elif GAMESTATE == 'gameover':
        mostrar_texto('gameover', 50, [300,50])
    

    pg.display.flip()
    clock.tick(60)

pg.quit()