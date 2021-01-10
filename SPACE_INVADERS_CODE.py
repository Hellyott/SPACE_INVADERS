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
score = 0
hauteur = 1000
largeur = 1000
game_over = 0

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


### FONCTIONS ###

def crea_alien():

    Liste = []
    x = 1
    y = 1

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

        Liste = Liste + [[x, y]]

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

    core.fps = 30
    core.WINDOW_SIZE = [hauteur, largeur]

    vie = 3

    global char
    global alien

    alien = crea_alien()
    char = crea_char()


def run():

    #General

    global score, vie, game_over

    #Clavier

    touche = core.getkeyPressValue()
    l,r,e = clavier(touche)

    #Game Over

    if vie == 0:
        game_over = 1

    if game_over == 1:
        while e != 1:
            touche = core.getkeyPressValue()
            l,r,e = clavier(touche)
            print("game over")
        #if __name__ == "__main__":
            #core.main(setup, run)




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
            pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))

            i[0] = i[0] + 0.005
    if xD == -1:
        for i in alien:
            pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))

            i[0] = i[0] - 0.005

    if xD == 0:
        for i in alien:
            pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))


    for i in alien:
        if i[0] > 12:
            yD = 1
            xD = 0
        if i[0] < 0.75:
            yD = -1
            xD = 0
    if yD == 1 or yD == -1:
        for i in alien:
            i[1] = i[1] + 0.3
        if yD == 1:
            xD = -1
        else:
            xD = 1
        yD = 0

    #Tir Alien

    global tir_a, Av_a, Xe_a, Xs_a, Ye_a, Ys_a, tir_en_cour

    if tir_en_cour == 0:
        for i in alien:
            tir_a = random.randint(0, 1000)
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

    if Ys_a > char[1] and char[0] < Xs_a < char[0] + 40:
        vie = vie - 1


    #for i in alien:
        #if i[0]*75 < Ys < i[0]*75 + 50 and i[1]*75 < Ys < i[1]*75 + 50:
            #score = score + 1
            #Xs = 0
            #Xe = 0
            #Ys = 0
            #Ye = 0
            #Av = 0








if __name__ == "__main__":
    core.main(setup, run)