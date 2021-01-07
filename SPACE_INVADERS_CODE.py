# Auteur : Mathéo, Axel, Timothée, Elliott
# Mail: Universitaire
# SPACE_INVADERS_CODE.py : Space invaders réalisé durant notre DUT GMP


### import ###

import pygame
import core
import random


### VARIABLES ###

alien = []
char = [0,0,0]
soucoupe = []
vie = 0
abris = []
score = 0
hauteur = 1000
largeur = 1000
keys = []
espace = 0
left = 0
right = 0
touche = 0


#importer sprites/musique

### FONCTIONS ###

def crea_alien():

    Liste = []
    et = 1


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

        Liste = Liste + [[x, y, et]]

    return Liste



def crea_char():

    charr = [20,900,1]
    return charr



def crea_abris():

    global abris

    x = 1
    y = 1

    et = 5 #6 etats possible sachant que 0: plus d'abris

    for i in range(1,5):
        x = i
        abris = abris + [[x,y,et,(0,255,0)]]

    return abris




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
    crea_abris()




def run():



    pygame.draw.rect(core.screen, (0,255,0), ((char[0], char[1]), (40, 40)))
    #Mouvement char

    touche = core.getkeyPressValue()
    l,r,e = clavier(touche)


    if l == 1:
        char[0] = char[0] - 5
    if r == 1:
        char[0] = char[0] + 5

    # Tir

    #if e == 1:


    # Alien
    xD = 1
    yD = 0

    for i in alien:
        pygame.draw.rect(core.screen, (255, 255, 255), ((i[0]*75,i[1]*75), (50,50)))

        i[0] = i[0] + 0.005



    for i in alien:
        if i[0] > 12:
            c = 1
    if  == 1:
        for i in alien:
            i[1] = i[1] + 0.025





if __name__ == "__main__":
    core.main(setup, run)