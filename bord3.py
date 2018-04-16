import pygame
import time
import random
import variables, text
import life


var = variables
#life.Life.changeLife(False)
# set up assets folders



FPS = 60
powerup_time = 5000

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Aðförin")

def draw_text(surf, text, size,x, y):
    font = pygame.font.Font(var.font, size)
    text_surface = font.render(text, True, var.white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length

    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, var.green, fill_rect)
    pygame.draw.rect(surf, var.white, outline_rect, 2)

def draw_lives (surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_go_screen():
    var.gameDisplay.blit(var.lvl2_background, var.lvl2_background_rect)
    draw_text(var.gameDisplay, "Borð 3", 64, var.display_width / 2, var.display_height / 4)
    draw_text(var.gameDisplay, "Notaðu örvatakkana til þess að hreyfa leikmann og bilstöng til þess að skjóta.", 22, var.display_width / 2, var.display_height / 2)
    draw_text(var.gameDisplay, "Ýttu á bilstöngina til þess að hefja leik.", 28, var.display_width / 2, var.display_height * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        var.clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
            elif event.type == pygame.KEYUP:
                waiting = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = var.lvl2_p_image#pygame.transform.scale(var.lvl2_p_image, (50, 38))
        self.image.set_colorkey(var.black)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = var.display_width / 2
        self.rect.bottom = var.display_height - 10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > powerup_time:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = var.display_width / 2
            self.rect.bottom = var.display_height - 10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -20
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 20
        if keystate[pygame.K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx
        # Hindra að player fari út úr glugga
        if self.rect.right > var.display_width - 3:
            self.rect.right = var.display_width - 3
        elif self.rect.left < 3:
            self.rect.left = 3

    def pow_sheild(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullets(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                var.shoot_sound.play()
            elif self.power >= 2:
                bullet1 = Bullets(self.rect.left, self.rect.centery)
                bullet2 = Bullets(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                var.shoot_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (var.display_width / 2, var.display_height + 200)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(var.mob_images)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(0, var.display_width - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(3, 11)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > var.display_height + 10 or self.rect.left < -125 or self.rect.right > var.display_width + 120:
            self.rect.x = random.randrange(0, var.display_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = var.bullet_img
        self.image.set_colorkey(var.black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -20
    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["gun", "powershield"])
        self.image = var.powerup_images[self.type]
        self.image.set_colorkey(var.black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top > var.display_height:
            self.kill()

class Border(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = var.lvl2_border
        self.image.set_colorkey(var.black)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = var.display_width / 2
        self.rect.bottom = var.display_height - 100

    def update(self):
        pass

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = var.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(var.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = var.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

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
        text.message_to_screen("Borð 3", var.green, -100, "large")
        text.message_to_screen("Forsætisráðherrastólinn er innan seilingar en óvinir Sigmunds eru",
            var.black,
            -30)
        text.message_to_screen("staðráðnir í að hindra för hans. Ef Sigmundi á að takast ætlunarverk",
            var.black,
            -5)
        text.message_to_screen("sitt þarf hann að sigrast á óvinum sínum og koma þeim fyrir kattarnef",
            var.black,
            20)
        text.message_to_screen("- í eitt skipti fyrir öll.",
            var.red,
            45)
        text.message_to_screen("Skjóttu niður óvini Sigmunds og tryggðu honum yfirráð.",
            var.black,
            100)
        text.message_to_screen("Notaðu örvatakkana til að fara til hliðar og bilstöng til að skjóta.",
            var.black,
            160)
        text.message_to_screen("Veldu BILSTÖNG til þess að spila, P til þess að stöðva leik og ESCAPE til að hætta.",
            var.black,
            185)

        pygame.display.update()
        var.clock.tick(15)

    return False


def gameLoop():
    # Load all game sounds
    pygame.mixer.music.load(var.space_music)
    pygame.mixer.music.set_volume(0.4)

    pygame.mixer.music.play(loops=-1)

    # Game loop
    running = True
    startScreen = True
    gameOver = False
    isVictory = False
    while running:
        if startScreen:
            game_intro()
            startScreen = False
            global all_sprites, mobs, bullets, powerups
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(10):
                newmob()

            m = Mob()

            score = 0

        while gameOver:
            pygame.mixer.music.stop()
            var.gameDisplay.fill(var.light_grey)

            text.message_to_screen("Ó nei!",
                var.red,
                -100,
                size="large")
            text.message_to_screen("Fjendur Sigmundar hafa sigrast á Sigmundi og náð að bola honum",
                var.black,
                -30,)
            text.message_to_screen("endanlega í burtu. Réttlætið neyðist til þess að lúta í gras fyrir",
                var.black,
                -5,)
            text.message_to_screen("ranglætinu.",
                var.black,
                20,)
            pLife = 2
            text.message_to_screen("Þú missir eitt líf og átt nú %d líf eftir." % pLife,
                var.black,
                70,)
            text.message_to_screen("Þú hlaust %d stig." % (score),
                var.black,
                95)

            text.button("Reyna aftur", 240, 500, 120, 50, var.green, var.light_green, "lvl3")
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
                        pygame.quit()
                        sys.exit()
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
            text.message_to_screen("Þér hefur tekist að sigra hrægammana og knýja fram sigur á mótlætinu.",
                var.black,
                -30,)
            life = 3
            text.message_to_screen("Forsætisráðherrastóllinn hefur verið endurheimtur og kominn til síns rétta",
                var.black,
                15,)
            text.message_to_screen("eigenda. Aðförinni er lokið og framundan bjartir tímar fyrir land og þjóð.",
                var.black,
                40,)
            text.message_to_screen("Þú hefur safnað %d stigum." % (score + 10),
                var.black,
                85)

            text.button("Ljúka leik", 240, 500, 120, 50, var.green, var.light_green, "quit")
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

        # keep loop running at the right speed
        var.clock.tick(FPS)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    return

        # Update
        all_sprites.update()

        # check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 20 #- hit.radius
            random.choice(var.expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random() > 0.90:
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
            newmob()

        # check if a mob hit the player
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player.shield <= 0:
                var.player_die_sound.play()
                death_explotion = Explosion(player.rect.center, "player")
                all_sprites.add(death_explotion)
                player.hide()
                player.lives -= 1
                player.shield = 100

        # if the player hit a powerup
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == "shield":
                player.shield += 30
                var.shield_sound.play()
                if player.shield >= 100:
                    player.shield = 100
            elif hit.type == "gun":
                player.powerup()
                var.power_sound.play()

        # if the player died and the explotion has finished playing
        if player.lives == 0 and not death_explotion.alive():
            gameOver = True
            #l.changeLife(gameOver)

        if score == 1000:
            isVictory = True

        # Draw / render
        var.gameDisplay.fill(var.black)
        var.gameDisplay.blit(var.lvl2_background, var.lvl2_background_rect)
        all_sprites.draw(var.gameDisplay)
        draw_text(var.gameDisplay, str(score), 18, var.display_width / 2, 10)
        draw_shield_bar(var.gameDisplay, 5, 5, player.shield)
        draw_lives(var.gameDisplay, var.display_width - 100, 5, player.lives, var.lvl2_p_mini_img)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()
