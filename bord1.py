import pygame
import math, random, sys
from os import path
import text
import variables, character, text
import character

var = variables
char = character
# define display surface

# initialise display
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Aðförin")
FPS = 500


class Player:
    def __init__(self, x, y, circleX, size):
        self.posX = x
        self.posY = y
        self.platform_y = y
        self.circlePosX = circleX
        self.image = pygame.transform.scale(var.p_images[1], (56, 152))
        self.image_jump = pygame.transform.scale(var.p_images[0], (56, 152))
        self.image_jumpback = pygame.transform.scale(var.p_images[4], (56, 152))
        self.image_run = pygame.transform.scale(var.p_images[2], (56, 152))
        self.image_runback = pygame.transform.scale(var.p_images[3], (56, 152))
        self.size = size
        self.jumping = False
        self.playerVelocityX = 0
        self.velocity_index = 0
        self.direction = True

    def do_jump(self):
        global velocity
        velocity = list([-13, -10, -9, -7.5, -6.5, -6, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 6.5, 7.5, 9, 10, 13])

        if self.jumping:
            self.posY += velocity[self.velocity_index]
            self.velocity_index += 1
            if self.velocity_index > len(velocity) - 1:
                self.velocity_index = len(velocity) - 1
            if self.posY > self.platform_y:
                self.posY = self.platform_y
                self.jumping = False
                self.velocity_index = 0

    def draw(self):
        #global gameDisplay, white, solid_fill
        if self.jumping and self.direction:
            var.gameDisplay.blit(self.image_jump,(int(self.circlePosX), int(self.posY)))
        elif self.jumping and not self.direction:
            var.gameDisplay.blit(self.image_jumpback,(int(self.circlePosX), int(self.posY)))
        elif self.playerVelocityX == 0:
            var.gameDisplay.blit(self.image,(int(self.circlePosX), int(self.posY)))
        else:
            if self.direction:
                var.gameDisplay.blit(self.image_run,(int(self.circlePosX), int(self.posY)))
            else:
                var.gameDisplay.blit(self.image_runback,(int(self.circlePosX), int(self.posY)))

class Cake:
    def __init__(self):
        self.posX = 1220
        self.posY = 210
        self.image = var.cake_img
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(0, var.display_width - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 8)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.posX += self.speedx

    def draw(self):
        var.gameDisplay.blit(self.image, (int(self.posX), int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 300, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 500, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 580, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 800, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 1200, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 1350, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 1490, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 1600, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 2000, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 2100, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 2400, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 2700, int(self.posY)))
        var.gameDisplay.blit(self.image, (int(self.posX) + 2800, int(self.posY)))


def events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()

def keys(player, cake):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player.jumping == False:
        player.jumping = True
        var.jump_sound.play()
    if keys[pygame.K_RIGHT]:
        player.playerVelocityX = 10
        player.direction = True
        cake.speedx = -10
    elif keys[pygame.K_LEFT]:
        player.playerVelocityX = -10
        player.direction = False
        cake.speedx = 10
    elif keys[pygame.K_ESCAPE]:
        return True
    elif keys[pygame.K_p]:
        a = pause()
        if a:
            return True
    else:
        player.playerVelocityX = 0
        cake.speedx = 0

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    return True
        var.gameDisplay.fill(var.light_grey)
        text.message_to_screen("Leikur stöðvaður",
            var.green,
            -100,
            size = "large")
        text.message_to_screen("Veldu BILSTÖNG til þess að halda áfram eða ESCAPE til að hætta.",
            var.black,
            180)

        pygame.display.update()
        var.clock.tick(5)

def score(score):
    text = var.smallfont.render("Stig : " + str(score), True, var.black)
    var.gameDisplay.blit(text, [720, 12])

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
                elif event.key == pygame.K_ESCAPE:
                    return True

        var.gameDisplay.fill(var.light_grey)
        text.message_to_screen("Borð 1", var.green, -100, "large")
        text.message_to_screen("Sigmundur Davíð hefur nýlega verið stunginn í bakið af samherjum",
            var.black,
            -30)
        text.message_to_screen("sínum og svikinn um forsætisráðherrastólinn. Hann er þó ekki af",
            var.black,
            -5)
        text.message_to_screen("baki dottinn og er staðráðinn að sigrast á mótlætinu, en til þess",
            var.black,
            20)
        text.message_to_screen("að styrkja sig fyrir komandi átök.",
            var.black,
            45)
        text.message_to_screen("Hjálpaðu Sigmundi að safna kökusneiðum á ferð sinni um borgina.",
            var.black,
            100)
        text.message_to_screen("Notaðu örvatakkana til að fara til hliðar og bilstöng til að hoppa.",
            var.black,
            160)
        text.message_to_screen("Veldu BILSTÖNG til þess að spila, P til þess að stöðva leik og ESCAPE til að hætta.",
            var.black,
            185)

        pygame.display.update()
        var.clock.tick(15)

    return False

def gameLoop():
    pygame.mixer.music.load(path.join(var.snd_dir, var.city_noise))
    pygame.mixer.music.set_volume(0.4)

    pygame.mixer.music.play(loops=-1)


    # Prepare
    bgWidth, bgHeight = var.lvl1_background.get_rect().size
    stageWidth = bgWidth * 3
    stagePosX = 0

    startScrollingPosX = var.display_width / 2

    playerSize = 60
    circlePosX = playerSize

    initialPosX = playerSize
    initialPosY = 260

    gameOver = False
    isVictory = False
    count = 0

    p = Player(initialPosX, initialPosY, circlePosX, playerSize)
    c = Cake()

    # main loop
    run = True
    while run:
        # Leik lokið skjár
        while gameOver == True:
            var.gameDisplay.fill(var.light_grey)
            text.message_to_screen("Leik lokið",
                var.red,
                -100,
                size="large")
            text.message_to_screen("Þú hlaust %d stig." % (count),
                var.black,
                -30)
            text.message_to_screen("Veldu C til að spila aftur eða Q til að hætta",
                var.black,
                180,)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        gameOver = False
                    elif event.key == pygame.K_c:
                        return False
                    elif event.key == pygame.K_r:
                        return True

        while isVictory == True:
            pygame.mixer.music.stop()
            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Til hamingju!",
                var.red,
                -100,
                size="large")
            text.message_to_screen("Göngutúrinn um miðbæ Reykavíkur hefur borið árangur og þú ert nú",
                var.black,
                -30,)
            text.message_to_screen("endurnærður og staðráðinn á ná þér niður á óvinum þínum. ",
                var.black,
                -5,)
            points = 0
            text.message_to_screen("Þú hefur safnað %d stigum." % points,
                var.black,
                65)

            text.button("Næsta borð", 240, 500, 120, 50, var.green, var.light_green, "lvl2")
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
                    elif event.key == pygame.K_r:
                        return True

        events()
        k = keys(p, c)
        p.do_jump()
        if k == True:
            k = False
            break

        p.posX += p.playerVelocityX
        c.update()

        if p.posX > stageWidth - playerSize:
            p.posX = stageWidth - playerSize
        if p.posX < 10:
            p.posX = 10
        if p.posX < startScrollingPosX:
            p.circlePosX = p.posX
        elif p.posX > stageWidth - startScrollingPosX:
            p.circlePosX = p.posX - stageWidth + var.display_width
        else:
            p.circlePosX = startScrollingPosX
            stagePosX += -p.playerVelocityX

        # Draw / render
        var.gameDisplay.fill(var.black)

        rel_x = stagePosX % bgWidth
        var.gameDisplay.blit(var.lvl1_background, (rel_x - bgWidth, 0))
        if rel_x < var.display_width:
            var.gameDisplay.blit(var.lvl1_background, (rel_x, 0))

        if p.posX > stageWidth - 100:
            isVictory = True

        """if p.posX >= c.posX and p.posX <= c.posX + 30 and p.posY < c.posY:
            count += 1
        print(c.posX)"""
        score(count)

        #print(cakeX)

        c.draw()
        p.draw()

        pygame.display.update()
        var.clock.tick(FPS)
        var.gameDisplay.fill(var.black)


#gameLoop()
