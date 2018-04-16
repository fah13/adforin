import pygame
import time
import random
import variables
import text

pygame.init()
pygame.display.set_caption("Aðförin")

var = variables

border = 40

block_size = 20
AppleThickness = 30
FPS = 15

direction = "right"


def pause(snakeLength):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        var.gameDisplay.fill(var.dark_grey)
        pygame.draw.rect(var.gameDisplay, var.light_grey, [0, border, var.display_width, var.display_height - (2*border)])
        text.message_to_screen("Leikur stöðvaður",
            var.green,
            -100,
            size = "large")
        text.message_to_screen("Veldu BILSTÖNG til þess að halda áfram." ,
            var.black,
            180)

        score(snakeLength - 1)

        pygame.display.update()
        var.clock.tick(5)

def score(score):
    text = var.smallfont.render("Stig : " + str(score), True, var.white)
    var.gameDisplay.blit(text, [720, 12])

def randAppleGen():
    randAppleX = round(random.randrange(0, var.display_width - AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(border, var.display_height - border - AppleThickness))#/10.0)*10.0

    return randAppleX, randAppleY

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_ESCAPE:
                    return True

        var.gameDisplay.fill(var.light_grey)
        text.message_to_screen("Borð 2", var.green, -100, "large")
        text.message_to_screen("Sigmundur Davíð hefur ákveðið að stofna Miðflokkinn og leitast nú",
            var.black,
            -30)
        text.message_to_screen("við að boða út fagnaðarerindið og fjölga stuðningsmönnum um borð í",
            var.black,
            -10)
        text.message_to_screen("Miðflokkslestinni. En vegurinn er háll og hætturnar leynast víða.",
            var.black,
            10)
        text.message_to_screen("Safnaðu liði um borð í Miðflokkslestina en gættu",
            var.black,
            90)
        text.message_to_screen("þess um leið að fara ekki út af sporinu.",
            var.black,
            110)
        text.message_to_screen("Veldu BILSTÖNG til þess að spila og ESC til að stöðva leik.",
            var.black,
            180)

        pygame.display.update()
        var.clock.tick(15)

    return False

def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(var.img_bord3, 270)
    if direction == "left":
        head = pygame.transform.rotate(var.img_bord3, 90)
    if direction == "up":
        head = var.img_bord3
    if direction == "down":
        head = pygame.transform.rotate(var.img_bord3, 180)

    var.gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(var.gameDisplay, var.green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = var.smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = var.medfont.render(text, True, color)
    elif size == "large":
        textSurface = var.largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def changeImg():
    old_r = 0
    while True:
        r = random.randint(1, 8)

        if r == 1 and not r == old_r:
            old_r = r
            return var.img_midfl1
        elif r == 2 and not r == old_r:
            old_r = r
            return var.img_midfl2
        elif r == 3 and not r == old_r:
            old_r = r
            return var.img_midfl3
        elif r == 4 and not r == old_r:
            old_r = r
            return var.img_midfl4
        elif r == 5 and not r == old_r:
            old_r = r
            return var.img_midfl5
        elif r == 6 and not r == old_r:
            old_r = r
            return var.img_midfl6
        elif r == 7 and not r == old_r:
            old_r = r
            return var.img_midfl7
        elif r == 8 and not r == old_r:
            old_r = r
            return var.img_midfl8

def gameLoop():
    global direction
    direction = "right"

    gameExit = False
    gameOver = False
    isVictory = False

    # Upphafsstaðsetning
    lead_x = var.display_width/4
    lead_y = var.display_height/2
    # Upphafsbreyting
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    old_r = 0
    currentImage = var.img_midfl1

    while not gameExit:
        # Leik lokið skjár
        while gameOver == True:
            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Ó nei!",
                var.red,
                -100,
                size="large")
            text.message_to_screen("Þú misstir stjórn á lestinni með þeim afleingum að hún fór út af sporinu.",
                var.black,
                -30,)
            life = 3
            text.message_to_screen("Þú missir eitt líf og átt nú %d líf eftir." % life,
                var.black,
                15,)
            text.message_to_screen("Þú hlaust %d stig." % (snakeLength - 1),
                var.black,
                55)

            text.button("Reyna aftur", 240, 500, 120, 50, var.green, var.light_green, "lvl2")
            btn = text.button("Til baka", 440, 500, 120, 50, var.yellow, var.light_yellow, "back")

            if btn == "back":
                btn = ""
                return

            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        return False
                    elif event.key == pygame.K_ESCAPE:
                        return True

        while isVictory == True:
            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Til hamingju!",
                var.red,
                -100,
                size="large")
            text.message_to_screen("Miðflokkslestin er nú stútfull af nýjum og harðduglegum fylgjendum.",
                var.black,
                -30,)
            life = 3
            text.message_to_screen("Nú er ekkert í vegi fyrir því að bjóða fram í næstu kosningum og leiðin",
                var.black,
                15,)
            text.message_to_screen("að sjálfum forsætisráðherrastólnum greið.",
                var.black,
                40,)
            text.message_to_screen("Þú hefur safnað %d stigum." % (snakeLength - 1),
                var.black,
                65)

            text.button("Næsta borð", 240, 500, 120, 50, var.green, var.light_green, "lvl3")
            btn = text.button("Til baka", 440, 500, 120, 50, var.yellow, var.light_yellow, "back")

            if btn == "back":
                btn = ""
                return

            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        return False
                    elif event.key == pygame.K_ESCAPE:
                        return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change -= block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change += block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change -= block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change += block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    pause(snakeLength)
                    time.sleep(.5)


        if lead_x >= var.display_width or lead_x < -10 or lead_y >= var.display_height - border or lead_y < border:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        var.gameDisplay.fill(var.dark_grey)
        #posx, posy, width, height
        pygame.draw.rect(var.gameDisplay, var.light_grey, [0, border, var.display_width, var.display_height - (2*border)])

        var.gameDisplay.blit(currentImage, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        score(snakeLength - 1)

        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness + 10:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                currentImage = changeImg()
                var.snake_sound.play()
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness + 10:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                currentImage = changeImg()
                var.snake_sound.play()

        if snakeLength - 1 == 10:
            isVictory = True

        pygame.display.update()
        var.clock.tick(FPS)

    pygame.quit()
    quit()
