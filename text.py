import pygame
import variables
import level
import character
import time

def text_objects(text, color, size):
    if size == "small":
        textSurface = var.smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = var.medfont.render(text, True, color)
    elif size == "large":
        textSurface = var.largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)

    textRect.center = (var.display_width / 2), (var.display_height / 2) + y_displace
    var.gameDisplay.blit(textSurf, textRect)

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center  = ((buttonx + (buttonwidth/2)), buttony + (buttonheight/2))
    var.gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    var.action = action

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(var.gameDisplay, active_color, (x,y,width,height))
        # hægri smellur
        if click[0] == 1 and var.action != None:
            if var.action == "quit":
                pygame.quit()
                quit()
            elif var.action == "back":
                return var.action
            elif var.action == "play":
                var.action == ""
                lvl.Level.levelOverview()
            elif var.action == "character":
                var.action == ""
                lvl.Level.char()
            elif var.action == "about":
                var.action == ""
                lvl.Level.about()
            elif var.action == "outfit":
                var.action == ""
                c.setOutfit()
            elif var.action == "info":
                var.action == ""
                c.info()
            elif var.action == "black":
                return var.action
            elif var.action == "red":
                return var.action
            elif var.action == "yellow":
                return var.action
            else:
                pass
            if var.action == "lvl1":
                var.action == ""
                lvl.Level.level1()
            elif var.action == "lvl2":
                var.action == ""
                lvl.Level.level2()
            elif var.action == "lvl3":
                var.action == ""
                lvl.Level.level3()
            else:
                pass #print("Borð lokað. Þú verður að klára borðið á undan til þess að spila þetta borð.")
    else:
        pygame.draw.rect(var.gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text, var.black, x, y, width, height)


var = variables
lvl = level
c = character.Character()
