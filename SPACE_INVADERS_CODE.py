# Auteur : Mathéo, Axel, Timothée, Elliott
# Mail: Universitaire
# SPACE_INVADERS_CODE.py : Space invaders réalisé durant notre DUT GMP


### import ###

import pygame
import core
import random


### VARIABLES ###

#général

alien = []
xD = 1
yD = 0
char = [0,0,0]
vie = 0
mort = 0
mort_a = 0
score = 0
hauteur = 1000
largeur = 1000
game_over = False

ecran = pygame.display.set_mode((1000, 1000))

#Deplacements

keys = []
espace = 0
left = 0
right = 0
touche = 0

#Gestion Tir

tir = 0
Xs = 0
Ys = 0
Xe = 0
Ye = 0
Av = 0

Xs_a = 0
Ys_a = 0
Xe_a = 0
Ye_a = 0
tir_a = 0
Av_a = 0
tir_en_cour = 0
proba = 750


### FONCTIONS ###

def crea_alien():

    Liste = []
    x = 1
    y = 1
    et = 1

    for i in range(1, 56):

        if 1 < i <= 11:
            y = 1
            x = i
        if 11 < i <= 22:
            y = 2
            x = i - 11
        if 22 < i <= 33:
            y = 3
            x = i - 22
        if 33 < i <= 44:
            y = 4
            x = i - 33
        if 44 < i <= 55:
            y = 5
            x = i - 44

        Liste = Liste + [[x, y, et]]

    return Liste



def crea_char():

    charr = [20,900,1]
    return charr

def clavier(touche):

    left = 0
    right = 0
    espace = 0

    if touche == 1073741904:
        left = 1
    if touche == 1073741903:
        right = 1
    if touche == 32:
        espace = 1
    return left, right, espace




### STRUCTURE JEU ###


def setup():

    global left
    global right
    global score, vie, game_over, mort, gm


    core.fps = 30
    core.WINDOW_SIZE = [hauteur, largeur]

    gm = pygame.image.load("game_over.png").convert()

    vie = 3

    global char
    global alien

    alien = crea_alien()
    char = crea_char()


def run():

    #General

    global score, vie, game_over, mort, mort_a, gm, proba

    #Clavier

    touche = core.getkeyPressValue()
    l,r,e = clavier(touche)

    if game_over == True:

        ecran.blit(gm, (140, 200))
        touche = core.getkeyPressValue()
        l,r,e = clavier(touche)
        print(score)

        if e == 1:
            game_over = False

    if game_over == False:

        print(vie)
        if vie == 0:
            game_over = True
        #Char

        pygame.draw.rect(core.screen, (0,255,0), ((char[0], char[1]), (40, 40)))

        if l == 1:
            char[0] = char[0] - 5
        if r == 1:
            char[0] = char[0] + 5


        # Tir


        global tir, Xs, Ys, Xe, Ye, Av

        if e == 1:
            tir = 1
            Av = 1

        if tir == 1:
            Xs = char[0] + 20
            Ys = char[1]
            Xe = char[0] + 20
            Ye = char[1] - 50

        if Av == 1:
            Ys = Ys - 10
            Ye = Ye - 10
            pygame.draw.line(core.screen, (255,0,0), (Xs,Ys), (Xe,Ye))
            tir = 0

            if Ye < 0:
                Xs = 0
                Xe = 0
                Ys = 0
                Ye = 0
                Av = 0

        # Alien

        global xD, yD

        if xD == 1:
            for i in alien:
                if i[2] == 1:
                    pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))
                    i[0] = i[0] + 0.005

                else:
                    i[0] = -50
                    i[1] = -50

        if xD == -1:
            for i in alien:
                if i[2] == 1:
                    pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))
                    i[0] = i[0] - 0.005

                elif i[2] == 0:
                    i[0] = -50
                    i[1] = -50

        if xD == 0:
            for i in alien:
                if i[2] == 1:
                    pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))

                elif i[2] == 0:
                    i[0] = -50
                    i[1] = -50


        for i in alien:
            if 14 > i[0] > 12:
                yD = 1
                xD = 0
            if 0 < i[0] < 0.75:
                yD = -1
                xD = 0
        if yD == 1 or yD == -1:
            for i in alien:
                i[1] = i[1] + 0.45
            if yD == 1:
                xD = -1
            else:
                xD = 1
            yD = 0

        #Tir Alien

        global tir_a, Av_a, Xe_a, Xs_a, Ye_a, Ys_a, tir_en_cour

        if tir_en_cour == 0:
            for i in alien:
                tir_a = random.randint(0, proba)
                if tir_a == 100:
                    Av_a = 1
                    Xe_a = i[0]*75 + 25
                    Ye_a = i[1]*75 + 50
                    Xs_a = i[0]*75 + 25
                    Ys_a = i[1]*75 + 100
                    tir_en_cour = 1

        if Av_a == 1:
            pygame.draw.line(core.screen, (255,0,0), (Xe_a, Ye_a), (Xs_a, Ys_a))
            Ye_a = Ye_a + 10
            Ys_a = Ys_a + 10

        if Ye_a > 1000:
            tir_en_cour = 0


        #Collision

        if Ye_a > char[1] and char[0] < Xe_a < char[0] + 40:
            mort = 1
            Xe_a = 0
            Ye_a = 0
            Xs_a = 0
            Ys_a = 0

        if mort == 1:
            vie = vie -1
            mort = 0

        for m in alien:
            if m[2] == 1:
                if m[0]*75 < Xe < m[0]*75 + 50 and m[1]*75 < Ye < m[1]*75 + 50:
                    mort_a = 1
                    Xs = 0
                    Xe = 0
                    Ys = 0
                    Ye = 0
                    Av = 0
                    m[2] = 0
                    proba = proba - 10

        if mort_a == 1:
            score = score + 10
            mort_a = 0

        # Collision alien Char

        for i in alien:
            if i[1] > char[1]:
                game_over = True

if __name__ == "__main__":
    core.main(setup, run)