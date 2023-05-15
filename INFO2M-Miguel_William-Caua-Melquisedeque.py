import pygame as pg

SCREENSIZE = (600,600)
pg.init()
screen = pg.display.set_mode(SCREENSIZE)
pg.display.set_caption('Forca')
clock = pg.time.Clock()
running = True

teste = pg.image.load('nao sei.png')
teste.set_colorkey('white')

while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # ------------- TICK -------------

    screen.fill((47,69,65))
    # ------------- RENDER -------------
    screen.blit(teste,(10,10))
    
    pg.display.flip()
    clock.tick(60)

pg.quit()