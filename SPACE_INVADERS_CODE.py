# Auteur : Mathéo, Axel, Timothée, Elliott
# Mail: Universitaire
# SPACE_INVADERS_CODE.py : Space invaders réalisé durant notre DUT GMP


### import ###

import pygame
import core
import random


### VARIABLES ###

alien = []
char = []
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

    global alien

    r = 255
    v = 255
    b = 255

    et = 1

    dx = 0
    dy = 0

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

        alien = alien + [[x, y, dx, dy, et, (r, v, b,)]]

    return (alien)



def crea_char():
    global char
    char = [0,0,0,0,1,(0,255,0)]
    return(char)



def crea_abris():

    global abris

    x = 1
    y = 1

    et = 5 #6 etats possible sachant que 0: plus d'abris

    for i in range(1,5):
        x = i
        abris = abris + [[x,y,et,(0,255,0)]]

    return(abris)




def clavier(touche):
    if touche == 1073741904:
        left = 1
    if touche == 1073741903:
        right = 1
    if touche == 32:
        espace = 1
    return(left, right, espace)





### STRUCTURE JEU ###


def setup():

    global left
    global right

    core.fps = 30
    core.WINDOW_SIZE = [hauteur, largeur]

    vie = 3

    crea_alien()
    crea_char()
    crea_abris()



def run():



    pygame.draw.rect(core.screen, (0,255,0), ((char.index(0), char.index(1)), (40, 40)))
    #Mouvement char
    touche = core.getkeyPressValue()
    clavier(touche)
    if left == 1:
        char[3] = char[3] - 5
    if right == 1:
        char[3] = char[3] + 5


    if vie == 0:
        game_over()





if __name__ == "__main__":
    core.main(setup, run)