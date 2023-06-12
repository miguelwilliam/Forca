import pygame as pg

palavras = ['banana','palmeiras','cuscuz','teclado','cachorro','vaca', 'naruto','cleiton','emidio','dias','macaco','computador','charuto','uva','ovo','fluminense','sapato', 'orangotango', 'vasco', 'paysandu', 'forca', 'minecraft', 'flamengo', 'atletico', 'galinha', 'roblox', 'priscilla', 'jubileu', 'carlos', 'melancia', 'pepino', 'pitaya', 'goiaba', 'acerola','raluca','diggo','jeanl','slipknot']

def escolher_palavra():
    global palavra_escolhida, resposta
    palavra_escolhida = random.choice(palavras)
    resposta = []
    for i in range(len(palavra_escolhida)):
        resposta.append('_')

def novo_jogo():
    global vidas, GAMESTATE
    escolher_palavra()
    vidas = 6
    GAMESTATE = 'jogo'

def mostrar_texto(texto,tamanho,pos):
    font = pg.font.Font('Minecraft.ttf',tamanho)
    text = font.render(texto,True,(255,255,255),)
    textRect = text.get_rect()
    textRect.center = (pos[0], pos[1])
    screen.blit(text,textRect)

novo_jogo()

while running:
    # CHECAR EVENTOS
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
            if GAMESTATE == 'gameover':
                if event.key == pg.K_r:
                    novo_jogo()

    
    # ------------- TICK -------------
    if GAMESTATE == 'jogo':
        if vidas <= 0:
            GAMESTATE = 'gameover'
        if '_' not in resposta:
            GAMESTATE = 'gameover'
            mensagem = f'PARABENS! A palavra era'
    
    elif GAMESTATE == 'gameover':
        if '_' in resposta:
            mensagem = f'GAMEOVER! A palavra era'

    
    screen.fill((26, 25, 50))
    # ------------- RENDER -------------
    if GAMESTATE == 'jogo':
        mostrar_texto(''.join(resposta), 64, [300,40])

        for i in range(vidas):
            screen.blit(img_coracao,[20+75*i, 50])
    
    elif GAMESTATE == 'gameover':
        mostrar_texto(mensagem, 32, [300,50])
        mostrar_texto(palavra_escolhida.upper(), 64, [300, 100])
        mostrar_texto('Pressione R para recomecar.', 32, [300,300])
    
    pg.display.flip()
    clock.tick(60)

pg.quit()
import random

# iniciar as coisa
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

palavra_escolhida = ''
resposta = []