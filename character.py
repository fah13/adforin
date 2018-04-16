import pygame
import variables
import text
import random
import bord1, bord2, bord3

class Character():
    def __init__(self):
        self.image = var.sdg_black
        self.name = "Sigmundur Davíð"
        self.outfit = "svörtum"
        self.outfitPicked = False
        self.points = 0
        self.countLife = 4

    def mainView(self):
        print(self.outfit)
        run = True

        while run:
            # leyfa að loka glugga
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # Klæðnaður
                        pass #Level.levelOverview()
                    elif event.key == pygame.K_2:
                        # Upplýsingar
                        pass
                    elif event.key == pygame.K_3 or event.key == pygame.K_ESCAPE:
                        # til baka
                        return
                    elif event.key == pygame.K_q:
                        # hætta
                        pygame.quit()
                        quit()

            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Leikmaður",
                var.green,
                -180,
                "medium")
            text.message_to_screen("Velkomin/nn í leikmannahlutann. Hér getur þú valið fatnað á Sigmund,",
                var.black,
                -120,
                "small")
            text.message_to_screen("auk þess sem þú getur skoðað helstu upplýsingar um stöðu þína í leiknum.",
                var.black,
                -95,
                "small")
            text.message_to_screen("Veldu að neðan hvað þú vilt gera.",
                var.black,
                20,
                "small")

            text.button("Klæðnaður", 180, 420, 120, 50, var.green, var.light_green, "outfit")
            text.button("Upplýsingar", 340, 420, 130, 50, var.green, var.light_green, "info")
            btn = text.button("Til baka", 510, 420, 120, 50, var.yellow, var.light_yellow, "back")

            if btn == "back":
                btn = ""
                return

            pygame.display.update()
            var.clock.tick(15)


    def setOutfit(self):
        print(self.outfit)
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # Svartur
                        btn = "black"
                        c.changeOutfit(btn)
                    elif event.key == pygame.K_2:
                        # Rauður
                        btn = "red"
                        c.changeOutfit(btn)
                    elif event.key == pygame.K_3:
                        # Gulur
                        btn = "yellow"
                        c.changeOutfit(btn)
                    elif event.key == pygame.K_4 or event.key == pygame.K_ESCAPE:
                        # til baka
                        return
                    elif event.key == pygame.K_q:
                        # hætta
                        pygame.quit()
                        quit()

            var.gameDisplay.fill(var.light_grey)
            img_big = pygame.transform.scale(c.image, (80, 217)).convert_alpha()
            var.gameDisplay.blit(img_big, (372, 240))

            text.message_to_screen("Veldu klæðnað",
                var.green,
                -180,
                "medium")
            text.message_to_screen("Hér getur valið lit á jakka Sigmundar.",
                var.black,
                -120,
                "small")

            btn1 = text.button("Svartur", 180, 500, 120, 50, var.green, var.light_green, action="black")
            btn2 = text.button("Rauður", 340, 500, 120, 50, var.green, var.light_green, action="red")
            btn3 = text.button("Gulur", 500, 500, 120, 50, var.green, var.light_green, action="yellow")
            btn = text.button("Til baka", 640, 20, 120, 50, var.yellow, var.light_yellow, action="back")


            if btn == "back":
                btn = ""
                return
            elif btn1 == "black":
                c.changeOutfit(btn1)
            elif btn2 == "red":
                c.changeOutfit(btn2)
            elif btn3 == "yellow":
                c.changeOutfit(btn3)
            else:
                pass

            pygame.display.update()
            var.clock.tick(15)

    def changeOutfit(self, color):
        if color == "black":
            self.image = var.sdg_black
            self.outfit = "svörtum"
            print(self.outfit)
        elif color == "red":
            self.image = var.sdg_red
            self.outfit = "rauðum"
            print(self.outfit)
        elif color == "yellow":
            self.image = var.sdg_yellow
            self.outfit = "gulum"
            print(self.outfit)
        else:
            pass


    def info(self):
        print("Hér færð þú upplýsingar.")
        print(self.outfit)
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # Svartur
                        btn = "black"
                        c.changeImg(btn)
                    elif event.key == pygame.K_2:
                        # Rauður
                        btn = "red"
                        c.changeImg(btn)
                    elif event.key == pygame.K_3:
                        # Gulur
                        btn = "yellow"
                        c.changeImg(btn)
                    elif event.key == pygame.K_4 or event.key == pygame.K_ESCAPE:
                        # til baka
                        return
                    elif event.key == pygame.K_q:
                        # hætta
                        pygame.quit()
                        quit()

            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Upplýsingar",
                var.green,
                -180,
                "medium")
            text.message_to_screen("Hér koma fram upplýsingar um stöðu leikmanns í leiknum.",
                var.black,
                -120,
                "small")
            text.message_to_screen("Þú heitir %s." % self.name,
                var.black,
                0,
                "small")
            text.message_to_screen("Þú hefur safnað %d stigum." % self.points,
                var.black,
                30,
                "small")
            text.message_to_screen("Þú átt %d líf eftir." % self.countLife,
                var.black,
                60,
                "small")
            text.message_to_screen("Þú ert í %s jakka." % self.outfit,
                var.black,
                90,
                "small")

            btn = text.button("Til baka", 640, 500, 120, 50, var.yellow, var.light_yellow, "back")

            if btn == "back":
                btn = ""
                return

            pygame.display.update()
            var.clock.tick(15)



    def setName(self):
        self.name = "Sigmundur"

var = variables
c = Character()
