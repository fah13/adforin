import pygame
import variables
import text
import random
import character
import bord1, bord2, bord3


class Life():
    """Klasinn sem heldur utan um líf leikmanns"""
    def __init__(self):
        self.countLife = 4
        self.gameOver = False
        self.death = False

    def __des__(self):
        print ("Þetta er destructor")

    def changeLife(self, death):
        if death == True:
            self.countLife -= 1
            self.death == False
        if self.countLife == 0:
            self.gameOver = True
        return self.countLife           # skilar fjölda lífa
