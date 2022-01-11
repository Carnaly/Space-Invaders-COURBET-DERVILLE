    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : ce programme regroupe toutes les actions possibles des entités dans le cadre du Space Invaders

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le 14 Décembre 2021 à 11:11

Que reste-t-il à faire ?
- déplacements joueur
- tir joueur
- dégats pris par le joueur
- déplacement ennemis
- tir ennemi
- dégats pris par l'ennemi
- Limite canvas
"""

#  Déplacement du joueur

from test import PosX


def deplacement(event):
    # Gestion de l'événement Appui sur une touche de clavier
    global PosX, PosY
    touche = event.keysym

    # Déplacement vers la gauche
    if touche == 'q' or touche == 'Left':
        if PosX - 30 > 0 :
            PosX -= 30
        Canevas.coords(Pion, PosX-10, PosY-10, PosX+10, PosY+10)
    
    # Déplacement vers la droite
    if touche == 'd' or touche == 'Right':
        if PosX + 30 < 1600 : 
            PosX += 30
        Canevas.coords(Pion, PosX-10, PosY-10, PosX+10, PosY+10)

Canevas.after(100000000000000, deplacement)

# Tir du joueur

def tir_joueur(event):
    global PosX, PosY
    touche = event.keysym
    print(touche)

    # Tir
    if touche == 'space' or touche == '<Up>':
        print('boom')
        



# Déplacement des ennemis 



# Tir des ennemis


