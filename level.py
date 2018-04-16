import pygame
import variables
import text
import random
import character
import bord1, bord2, bord3

class Level():
    """docstring for Level."""
    def __init__(self):
        self.level = 0
        self.isVictory  = False
        self.level1Done = False
        self.level2Done = False
        self.level3Done = False

    def mainView():
        run = True

        while run:
            # leyfa að loka glugga
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # spila leik
                        Level.levelOverview()
                    elif event.key == pygame.K_2:
                        # leikmaður
                        Level.char()
                    elif event.key == pygame.K_3:
                        # um leikinn
                        Level.about()
                    elif event.key == pygame.K_4 or event.key == pygame.K_ESCAPE:
                        # hætta
                        pygame.quit()
                        quit()

            var.gameDisplay.fill(var.light_grey)
            var.gameDisplay.blit(var.mainView_bg, (0, 0))

            text.message_to_screen("Velkomin/nn í leikinn",
                var.green,
                -250,
                "medium")
            text.message_to_screen("Aðförin",
                var.green,
                -190,
                "large")

            text.button("Spila leik", 40, 500, 120, 50, var.green, var.light_green, "play")
            text.button("Leikmaður", 240, 500, 120, 50, var.green, var.light_green, "character")
            text.button("Um leikinn", 440, 500, 120, 50, var.yellow, var.light_yellow, "about")
            text.button("Hætta", 640, 500, 120, 50, var.red, var.light_red, "quit")

            pygame.display.update()
            var.clock.tick(15)

    def about():
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2 or event.key == pygame.K_ESCAPE:
                        # til baka
                        return

            var.gameDisplay.fill(var.light_grey)

            # Prenta texta á skjá
            text.message_to_screen("Um leikinn",
                var.green,
                -180,
                "medium")
            text.message_to_screen("Sigmundur Davíð hefur nýverið verið svikinn um formannsembætti",
                var.black,
                -120,
                "small")
            text.message_to_screen("flokksins. Hann er þó ekki af baki dottinn, en til þess að sigrast",
                var.black,
                -95,
                "small")
            text.message_to_screen("á mótlætinu þarf hann að kljást við forna fjendur sem vilja aðeins eitt:",
                var.black,
                -70,
                "small")
            text.message_to_screen("fella kónginn.",
                var.red,
                -45,
                "small")
            text.message_to_screen("Höfundar eru Friðrik Árni Halldórsson, Guðrún Snorra Þórsdóttir og",
                var.black,
                20,
                "small")
            text.message_to_screen("Sigrún Sayeh Valadbeygi. Leikurinn var hannaður og þróaður í",
                var.black,
                45,
                "small")
            text.message_to_screen("áfanganum Þróun hugbúnaðar vorið 2018.",
                var.black,
                70,
                "small")


            text.button("Spila leik", 40, 500, 120, 50, var.green, var.light_green, action="play")
            btn = text.button("Til baka", 640, 20, 120, 50, var.yellow, var.light_yellow, action="back")
            #text.button("Hætta", 650, 500, 100, 50, var.red, var.light_red, action="quit")

            if btn == "back":
                btn = ""
                return


            pygame.display.update()
            var.clock.tick(15)

    def levelOverview():
        #pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # borð 1
                        Level.level1()
                    if event.key == pygame.K_2:
                        # borð 2
                        Level.level2()
                    if event.key == pygame.K_3:
                        # borð 3
                        Level.level3()
                    if event.key == pygame.K_4:
                        # borð 4
                        Level.level4()
                    if event.key == pygame.K_ESCAPE:
                        # til baka
                        return
                    elif event.key == pygame.K_0:
                        # hætta
                        pygame.quit()
                        quit()

            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Yfirlitssíða",
                var.green,
                -90,
                "large")
            text.message_to_screen("Hér getur þú valið um mismunandi borð.",
                var.black,
                -10,
                "small")

            text.button("Borð 1", 180, 420, 120, 50, var.green, var.light_green, "lvl1")
            text.button("Borð 2", 340, 420, 120, 50, var.green, var.light_green, "lvl2")
            text.button("Borð 3", 500, 420, 120, 50, var.green, var.light_green, "lvl3")
            btn = text.button("Til baka", 640, 20, 120, 50, var.yellow, var.light_yellow, "back")

            if btn == "back":
                btn = ""
                return

            pygame.display.update()
            var.clock.tick(15)

    def char():
        a = c.mainView()

    def level1():
        a = bord1.game_intro()
        if a != True:
            bord1.gameLoop()

    def level2():
        a = bord2.game_intro()
        if a != True:
            bord2.gameLoop()

    def level3():
        a = bord3.gameLoop()

pygame.init()

var = variables
c = character.Character()
