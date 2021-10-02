import pygame
from pygame.locals import *

pygame.init()

# Fenêtre
screen = pygame.display.set_mode((450, 450))

# Titre
pygame.display.set_caption("DK Labyrinthe")

# Icône
ico = pygame.image.load("images/icone.jpg")
pygame.display.set_icon(ico)

# Sons
pygame.mixer.init()
son = pygame.mixer.Sound("sons/sound1.wav")
son.set_volume(0.3)
sonwin = pygame.mixer.Sound("sons/winsound.wav")
sonwin.set_volume(0.3)

# Images
bg = pygame.image.load("images/fond.jpg").convert()
win = pygame.image.load("images/win.jpg").convert()
menu = pygame.image.load("images/menu.jpg").convert()
lvl1 = pygame.image.load("images/lvl1.jpg").convert()
lvl2 = pygame.image.load("images/lvl2.jpg").convert()
bloc = pygame.image.load("images/mur.jpg").convert()
bloc_r = bloc.get_rect()  # Affichage bloc
start = pygame.image.load("images/depart.png").convert_alpha()
banane = pygame.image.load("images/arrivee.png").convert_alpha()
dk = pygame.image.load("images/dk_droite.png").convert_alpha()
dk_r = dk.get_rect()  # Affichage dk
dk_bas = pygame.image.load("images/dk_bas.png").convert_alpha()
dk_droite = pygame.image.load("images/dk_droite.png").convert_alpha()
dk_gauche = pygame.image.load("images/dk_gauche.png").convert_alpha()
dk_haut = pygame.image.load("images/dk_haut.png").convert_alpha()

# d = Donkey Kong
# 0 = vide
# m = mur
# n = passage secret
# a = arrivée

i = j = x = y = 0
plateau = [["d","0","0","m","m","m","m","m","m","m","m","m","m","m","m"],
           ["0","m","0","0","0","0","0","0","0","0","0","0","0","0","m"],
           ["0","m","m","m","m","m","0","m","m","m","0","m","m","0","0"],
           ["0","0","0","0","m","m","m","0","m","m","0","0","m","m","0"],
           ["m","m","m","0","0","0","0","0","m","m","0","m","m","0","0"],
           ["m","0","0","0","m","m","0","m","m","m","0","m","0","0","m"],
           ["m","0","m","0","0","0","0","0","0","0","0","m","0","m","m"],
           ["m","0","0","m","m","m","m","m","0","m","m","m","0","m","m"],
           ["m","m","0","m","m","m","m","0","0","m","0","0","0","0","m"],
           ["m","m","0","m","m","m","0","0","m","m","0","m","0","m","m"],
           ["0","0","0","0","0","0","0","m","m","0","0","m","0","0","m"],
           ["m","m","m","m","m","m","m","m","0","0","m","m","m","m","m"],
           ["m","m","0","m","0","0","0","0","0","m","m","m","0","0","m"],
           ["m","0","0","0","0","m","m","0","0","0","0","0","0","0","m"],
           ["m","m","m","m","0","0","m","m","0","m","0","m","m","0","a"]]

plateau2 = [["d","0","0","m","m","m","m","m","m","m","m","m","m","m","m"],
           ["0","m","0","0","0","0","0","0","0","0","0","0","0","0","m"],
           ["0","m","m","m","m","m","m","n","m","m","m","0","m","0","0"],
           ["0","0","m","m","m","m","m","0","m","m","m","0","m","m","0"],
           ["m","m","m","0","0","0","n","0","m","m","0","m","m","0","0"],
           ["m","0","0","n","m","m","n","m","m","m","0","m","0","0","m"],
           ["m","0","0","0","0","0","0","0","0","0","0","m","0","m","m"],
           ["m","0","0","m","m","m","m","m","0","m","0","m","0","m","m"],
           ["m","m","0","m","m","m","m","0","0","m","0","n","0","0","m"],
           ["m","m","n","m","m","m","n","0","m","m","m","m","0","m","m"],
           ["0","0","0","m","0","0","0","m","m","n","0","0","0","0","m"],
           ["m","m","m","m","0","m","m","m","m","0","m","m","0","m","m"],
           ["m","m","0","m","0","n","0","0","0","m","m","m","m","0","m"],
           ["0","0","0","0","0","m","m","m","m","0","0","0","0","0","m"],
           ["m","m","m","m","0","n","0","0","0","0","0","m","m","0","a"]]

game = 1
while game == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            game = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = 0
            elif event.key == K_F1:
                son.play()
                screen.blit(lvl1, (0, 0))
                pygame.display.flip()
                pygame.time.delay(3000)
                game = start

    screen.blit(menu, (0, 0))
    pygame.display.flip()

while game == start:
    for event in pygame.event.get():

        if event.type == QUIT:
            game = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = 0
            elif event.key == K_DOWN and dk_r.bottom < 450:
                dk = dk_bas
                if plateau[y+1][x] != "m":
                    plateau[y][x] = "0"
                    plateau[y + 1][x] = "d"
                    y = y + 1
                    dk_r = dk_r.move(0,30)

            elif event.key == K_RIGHT and dk_r.right < 450:
                dk = dk_droite
                if plateau[y][x +1] != "m":
                    if plateau[y][x+1] != "a":
                        plateau[y][x] = "0"
                        plateau[y][x + 1] = "d"
                    x = x + 1
                    dk_r = dk_r.move(30, 0)

            elif event.key == K_LEFT and dk_r.left > 0:
                dk = dk_gauche
                if plateau[y][x - 1] != "m":
                    plateau[y][x]="0"
                    plateau[y][x-1]="D"
                    x=x-1
                    dk_r = dk_r.move(-30, 0)

            elif event.key == K_UP and dk_r.top > 0:
                dk = dk_haut
                if plateau[y - 1][x] != "m":
                    plateau[y][x] = "0"
                    plateau[y - 1][x] = "d"
                    y = y - 1
                    dk_r = dk_r.move(0, -30)

    screen.blit(bg, (0, 0))
    screen.blit(start, (0,0))
    screen.blit(banane, (420, 420))
    screen.blit(dk, dk_r)

    if plateau[y][x] == "a":
        game = win
        pygame.mixer.pause()
        sonwin.play()

    for i in range(15):
        for j in range(15):
            if plateau[j][i] == "m":
                screen.blit(bloc, (i * 30, j * 30))

    pygame.display.flip()

while game == win:
    screen.blit(win, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            game = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = 0
    pygame.time.delay(6000)
    screen.blit(lvl2, (0, 0))
    pygame.mixer.unpause()
    pygame.display.flip()
    pygame.time.delay(3000)
    dk_r.center = 15,15
    i = j = x = y = 0
    game = 2

while game == 2:
    for event in pygame.event.get():

        if event.type == QUIT:
            game = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = 0
            elif event.key == K_DOWN and dk_r.bottom < 450:
                dk = dk_bas
                if plateau2[y + 1][x] != "m":
                    plateau2[y][x] = "0"
                    plateau2[y + 1][x] = "d"
                    y = y + 1
                    dk_r = dk_r.move(0, 30)

            elif event.key == K_RIGHT and dk_r.right < 450:
                dk = dk_droite
                if plateau2[y][x + 1] != "m":
                    if plateau2[y][x + 1] != "a":
                        plateau2[y][x] = "0"
                        plateau2[y][x + 1] = "d"
                    x = x + 1
                    dk_r = dk_r.move(30, 0)

            elif event.key == K_LEFT and dk_r.left > 0:
                dk = dk_gauche
                if plateau2[y][x - 1] != "m":
                    plateau2[y][x] = "0"
                    plateau2[y][x - 1] = "D"
                    x = x - 1
                    dk_r = dk_r.move(-30, 0)

            elif event.key == K_UP and dk_r.top > 0:
                dk = dk_haut
                if plateau2[y - 1][x] != "m":
                    plateau2[y][x] = "0"
                    plateau2[y - 1][x] = "d"
                    y = y - 1
                    dk_r = dk_r.move(0, -30)

    screen.blit(bg, (0, 0))
    screen.blit(start, (0, 0))
    screen.blit(banane, (420, 420))
    screen.blit(dk, dk_r)

    if plateau2[y][x] == "a":
        game = win
        son.stop()
        sonwin.play()

    for i in range(15):
        for j in range(15):
            if plateau2[j][i] == "m":
                screen.blit(bloc, (i * 30, j * 30))

    for i in range(15):
        for j in range(15):
            if plateau2[j][i] == "n":
                screen.blit(bloc, (i * 30, j * 30))

    pygame.display.flip()

while game == win:
    screen.blit(win, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            game = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = 0
    pygame.time.delay(6000)
    game = 0

pygame.quit()