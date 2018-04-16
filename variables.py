import pygame
import time
import random
from os import path

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

icon = pygame.image.load('Myndir/sdg_200x200.png')
pygame.display.set_caption("Aðförin")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
solid_fill = 0

# Litir
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (0, 155, 0)
light_green = (0, 255, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
light_grey = (211, 211, 211)
dark_grey = (80, 80, 80)

# Letur
pygame.font.init()
font = "Letur/Raleway-Bold.ttf"
smallfont = pygame.font.Font(font, 20)
medfont = pygame.font.Font(font, 30)
largefont = pygame.font.Font(font, 60)


img_dir = path.join(path.dirname(__file__), "Myndir")
snd_dir = path.join(path.dirname(__file__), "Hljóð")

# Myndir
mainView_bg = pygame.image.load(path.join(img_dir, "background_blur.png")).convert_alpha()

sdg1_black = pygame.image.load(path.join(img_dir, "sdg_2_black.png")).convert_alpha()
sdg1_red = pygame.image.load(path.join(img_dir, "sdg_2_red.png")).convert_alpha()
sdg1_yellow = pygame.image.load(path.join(img_dir, "sdg_2_yellow.png")).convert_alpha()
sdg_yellow = []
sdg_yellow_list = ["sdg_1_yellow.png", "sdg_2_yellow.png", "sdg_3_yellow.png", "sdg_4_yellow.png", "sdg_5_yellow.png"]
for img in sdg_yellow_list:
    sdg_yellow.append(pygame.image.load(path.join(img_dir, img)).convert_alpha())


# Borð 1
lvl1_background = pygame.image.load(path.join(img_dir, "background.png")).convert()
cake_img = pygame.image.load(path.join(img_dir, "cake.png")).convert_alpha()
p_images = []
p_img_list = ["sdg_1.png", "sdg_2.png", "sdg_3.png", "sdg_4.png", "sdg_5.png"]
for img in p_img_list:
    p_images.append(pygame.image.load(path.join(img_dir, img)).convert_alpha())

# Borð 2
img_bord3 = pygame.image.load(path.join(img_dir, 'lest2.png')).convert_alpha()
img_midfl1 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/gunnarbragi.png')).convert_alpha()
img_midfl2 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/vigdis.png')).convert_alpha()
img_midfl3 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/thorsteinn.png')).convert_alpha()
img_midfl4 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/siggistormur.png')).convert_alpha()
img_midfl5 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/annakolbrun.png')).convert_alpha()
img_midfl6 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/bergthor.png')).convert_alpha()
img_midfl7 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/birgir.png')).convert_alpha()
img_midfl8 = pygame.image.load(path.join(img_dir,'Miðflokkurinn/sigurdurpall.png')).convert_alpha()
img_treat = img_midfl1

# Borð 3
lvl2_background = pygame.image.load(path.join(img_dir, "space_background.png")).convert()
lvl2_background_rect = lvl2_background.get_rect()
lvl2_p_image = pygame.image.load(path.join(img_dir, "ship_sdg.png")).convert_alpha()
lvl2_p_mini_img = pygame.transform.scale(lvl2_p_image, (25, 19)).convert_alpha()
lvl2_border = pygame.image.load(path.join(img_dir, "border.png")).convert()
mob_images = []
mob_list = ["piratar_big.png", "ruv_big.png", "samfylking_med.png", "vidreisn_med.png", "rme_med.png", "vg_small.png", "xb_big.png", "xd_small.png"]
for img in mob_list:
    mob_images.append(pygame.image.load(path.join(img_dir, img)).convert_alpha())
bullet_img = pygame.image.load(path.join(img_dir, "laserRed.png")).convert_alpha()
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = "sonicExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(black)
    explosion_anim['player'].append(img)
powerup_images = {}
powerup_images["gun"] = pygame.image.load(path.join(img_dir, "bolt_gold.png")).convert_alpha()
powerup_images["powershield"] = pygame.image.load(path.join(img_dir, "shield_gold.png")).convert_alpha()



# Hljóð
pygame.mixer.init()

# Borð 1
jump_sound = pygame.mixer.Sound(path.join(snd_dir, "jump.wav"))
city_noise = "city.ogg"

# Borð 2
snake_sound = pygame.mixer.Sound(path.join(snd_dir, "pow3.wav"))

# Borð 3
space_music = "tgfcoder-FrozenJam-SeamlessLoop.ogg"
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, "sfx_laser2.ogg"))
shield_sound = pygame.mixer.Sound(path.join(snd_dir, "pow2.wav"))
power_sound = pygame.mixer.Sound(path.join(snd_dir, "pow3.wav"))
player_die_sound = pygame.mixer.Sound(path.join(snd_dir, "rumble1.ogg"))
expl_sounds = []
for snd in ["Explosion3.wav", "Explosion12.wav"]:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))


action = "NaN"
