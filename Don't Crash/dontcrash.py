import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

win_sound = pygame.mixer.Sound("cowabunga.wav")
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("twinturbo.wav")


black = (0,0,0)
white = (255, 255, 255)
light_red = (255,0,0)
red = (200,0,0)
road = (66, 65, 62)
green = (52, 142, 22)
light_green = (74, 219, 26)
block_color = (221, 162, 13)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("DON'T CRASH AND DIE")
clock = pygame.time.Clock()

carImg = pygame.image.load('speedracer.png')
carImg = pygame.transform.scale(carImg, (100,160))
died = pygame.image.load('died.jpg')
died = pygame.transform.scale(died, (800,600))
booimg = pygame.image.load('boo.png')
booimg = pygame.transform.scale(booimg, (100,100))
lvl2_background = pygame.image.load('level2.jpg')
lvl2_background = pygame.transform.scale(lvl2_background, (800,600))

def kingboo(boox, booy):
    gameDisplay.blit(booimg, (boox,booy))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    gameDisplay.blit(pygame.transform.scale(died, (800, 600)), (0, 0))
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects2("Ya Died.", large_text)
    TextRect.center = ((display_width/2), (display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                        
        button("Play Again", 350, 300, 150,50, green, light_green, game_loop)
        button("Quit", 350, 400, 150, 50, red, light_red, quit_game)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    
    small_text = pygame.font.SysFont("comicsansms", 20)
    TextSurf, TextRect = text_objects(msg, small_text)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)
    
def quit_game():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("DON'T CRASH AND DIE", large_text)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 350, 300, 100,50, green, light_green, game_loop)
        button("QUIT", 350, 400, 100, 50, red, light_red, quit_game)

        pygame.display.update()
        clock.tick(15)

def lvl2_intro():
    intro = True
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(win_sound)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("YOU BEAT THE 1ST LEVEL!", large_text)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)
        pygame.time.delay(4000)
        level2()

def credits():
    intro = True
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(win_sound)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("YOU WON!", large_text)
        TextRect.center = ((display_width/2), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        gameDisplay.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("This has been a terrible game by Trav", large_text)
        TextRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)
        pygame.time.delay(8000)
       
       
def game_loop():
    pygame.mixer.music.load("twinturbo.wav")
    pygame.mixer.music.play(-1)
    x = (display_width * 0.1)
    y = (display_height * 0.5)

    x_change = 0
    y_change = 0

    thing_starty = random.randrange(0, display_height)
    thing_startx = 900
    thing_speed = -4
    thing_width = 100
    thing_height = 100

    thing_count = 1

    dodged = 0
    
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5           
                if event.key == pygame.K_DOWN:
                    y_change = 5    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0 

        x += x_change
        y += y_change
        gameDisplay.fill(road)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_startx += thing_speed

        
        car(x,y)
        things_dodged(dodged)

       

        if x > display_width + 50 or x < 0 - 50:
            crash()
        if y > display_height + 20 or y < 0 - 20:
            crash()

        if thing_startx < 0 - thing_width:
            thing_startx = 900
            thing_starty = random.randrange(0, display_height)
            dodged += 1
            thing_speed -= 1

        if x + 90 > thing_startx and x < thing_startx + thing_width:

            if y > thing_starty and y < thing_starty + thing_height or y + 100 > thing_starty and y + 100 < thing_starty + thing_height:
                crash() 
        
        if dodged > 9:
            lvl2_intro()

        pygame.display.update()
        clock.tick(60)

def level2():
    pygame.mixer.music.load("spooky.wav")
    pygame.mixer.music.play(-1)
    x = (display_width * 0.1)
    y = (display_height * 0.5)

    x_change = 0
    y_change = 0

    boo_starty = random.randrange(0, display_height)
    boo_startx = 830
    boo_speed = -4
    boo_vertical = random.randrange(-2, 2)
    

    thing_count = 1

    dodged = 0
    
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5           
                if event.key == pygame.K_DOWN:
                    y_change = 5    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0 

        x += x_change
        y += y_change
        gameDisplay.blit(pygame.transform.scale(lvl2_background, (800, 600)), (0, 0))

        kingboo(boo_startx, boo_starty)
        boo_startx += boo_speed
        boo_starty += boo_vertical

        
        car(x,y)
        things_dodged(dodged)

        if x > display_width + 50 or x < 0 - 50:
            crash()
        if y > display_height + 20 or y < 100:
            crash()

        if boo_startx < -100:
            boo_startx = 900
            boo_starty = random.randrange(0, display_height)
            dodged += 1
            boo_speed -= 1

        if x + 90 > boo_startx and x < boo_startx + 100:

            if y > boo_starty and y < boo_starty + 100 or y + 100 > boo_starty and y + 100 < boo_starty + 100:
                crash() 
        
        if dodged > 9:
            credits()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()



