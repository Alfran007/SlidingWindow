x = 40
y = 30
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
import pygame
pygame.init()
import time
white = (255, 255, 255)
black = (0, 0, 0)
light_black = (211,211,211)
red = (200, 0, 0)
light_red = (255, 0, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
green = (34, 177, 76)
light_green = (0, 255, 0)
purple = (148,0,211)
dark_grey = (169,169,169)
display_width = 1300
display_height = 700
thing_width = 35
thing_height = 40
blue = (0,0,255)
initial_x = 50
startx = 50
starty = 350
thing_speed = 4
window_size = 4
guns = [pygame.image.load('gun1.jpg'),pygame.image.load('gun2.jpg'),pygame.image.load('gun3.jpg'),pygame.image.load('gun4.jpg'),pygame.image.load('gun5.jpg'),pygame.image.load('gun6.jpg'),pygame.image.load('gun7.jpg'),pygame.image.load('gun8.jpg'),pygame.image.load('gun9.jpg'),pygame.image.load('gun10.jpg'),pygame.image.load('gun11.jpg'),pygame.image.load('gun12.jpg'),pygame.image.load('gun13.jpg'),pygame.image.load('gun14.jpg'),pygame.image.load('gun15.jpg'),pygame.image.load('gun16.jpg'),pygame.image.load('gun17.jpg'),pygame.image.load('gun18.jpg'),pygame.image.load('gun19.jpg'),pygame.image.load('gun20.jpg')]
bool = [False for i in range(20)]
funs = [pygame.image.load('fun1.jpg'),pygame.image.load('fun2.jpg'),pygame.image.load('fun3.jpg'),pygame.image.load('fun4.jpg'),pygame.image.load('fun5.jpg'),pygame.image.load('fun6.jpg'),pygame.image.load('fun7.jpg'),pygame.image.load('fun8.jpg'),pygame.image.load('fun9.jpg'),pygame.image.load('fun10.jpg'),pygame.image.load('fun11.jpg'),pygame.image.load('fun12.jpg'),pygame.image.load('fun13.jpg'),pygame.image.load('fun14.jpg'),pygame.image.load('fun15.jpg'),pygame.image.load('fun16.jpg'),pygame.image.load('fun17.jpg'),pygame.image.load('fun18.jpg'),pygame.image.load('fun19.jpg'),pygame.image.load('fun20.jpg')]
whiteIm = pygame.image.load('white.jpg')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sliding Window Protocol')

gameDisplay.fill(white)

clock = pygame.time.Clock()
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

def blocks():
    pygame.draw.rect(gameDisplay, black, [10, 10, 1250, 650],3)
    pygame.draw.rect(gameDisplay, dark_grey, [35, 35, 1200, 275], 3)
    pygame.draw.rect(gameDisplay, dark_grey, [35, 325, 1200, 315], 3)
    pygame.draw.rect(gameDisplay, light_black, [45, 45, 600, 250], 3)
    pygame.draw.rect(gameDisplay, light_black, [650, 45, 575, 250], 3)
    # Coloured Blocks
    pygame.draw.rect(gameDisplay, red, [60, 54, 50, 25], 3)
    pygame.draw.rect(gameDisplay, green, [60, 97, 50, 25], 3)
    pygame.draw.rect(gameDisplay, light_yellow, [60, 139, 50, 25])
    pygame.draw.rect(gameDisplay, green, [60, 139, 50, 25], 3)
    pygame.draw.rect(gameDisplay, purple, [60, 180, 50, 25])
    pygame.draw.rect(gameDisplay, red, [60, 180, 50, 25], 3)
    pygame.draw.rect(gameDisplay, light_yellow, [60, 222, 50, 25])
    pygame.draw.rect(gameDisplay, purple, [60, 263, 50, 25])
    #Display Text Left Window
    myfont = pygame.font.SysFont("Verdana", 25)
    label = myfont.render("No data received yet", 1, blue)
    gameDisplay.blit(label, (130,47))
    label = myfont.render("No data arrived yet", 1, blue)
    gameDisplay.blit(label, (130, 90))
    label = myfont.render("Data is received", 1, blue)
    gameDisplay.blit(label, (130, 132))
    label = myfont.render("Acknowledgement Received", 1, blue)
    gameDisplay.blit(label, (130, 173))
    label = myfont.render("Data going to receiver", 1, blue)
    gameDisplay.blit(label, (130, 215))
    label = myfont.render("Acknowledgement going to sender", 1, blue)
    gameDisplay.blit(label, (130, 256))
    #Display Text Right Window
    label = myfont.render("Sliding Window Size", 1, blue)
    gameDisplay.blit(label, (655, 60))
    label = myfont.render("Speed", 1, blue)
    pygame.draw.rect(gameDisplay, black, [955, 60, 100, 30], 2)
    gameDisplay.blit(label, (655, 130))
    pygame.draw.rect(gameDisplay, black, [955, 130, 100, 30], 2)


def draw():
    # Above boxes
    pygame.draw.rect(gameDisplay, red, [50, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [110, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [170, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [230, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [290, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [350, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [410, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [470, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [530, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [590, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [650, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [710, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [770, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [830, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [890, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [950, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [1010, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [1070, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [1130, 350, 35, 40], 3)
    pygame.draw.rect(gameDisplay, red, [1190, 350, 35, 40], 3)

    # Below Boxes
    pygame.draw.rect(gameDisplay, green, [50, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [110, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [170, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [230, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [290, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [350, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [410, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [470, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [530, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [590, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [650, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [710, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [770, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [830, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [890, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [950, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [1010, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [1070, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [1130, 580, 35, 40], 3)
    pygame.draw.rect(gameDisplay, green, [1190, 580, 35, 40], 3)


def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "play":
               game_loop()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def win():
    global startx
    global starty
    global window_size
    pygame.draw.rect(gameDisplay, black, (startx - 10, starty  -10, 35 + (window_size - 1) * 60 + 20, 45 + 3 + 10), 3)
    pygame.draw.rect(gameDisplay, black, (startx - 10, starty + 580 - 350 -10, 35 + (window_size - 1) * 60 + 20, 45 + 3 + 10), 3)
    if starty == 580:
        pygame.draw.rect(gameDisplay, black, (startx - 10, starty - 580 + 350 - 10, 35 + (window_size - 1) * 60 + 20, 45 + 3 + 10), 3)

def pause():
    paused = True
    draw()
    blocks()
    win()
    pygame.diplay.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


    #clock.tick(5)
def inpt():
    global window_size
    global thing_speed
    word = ""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            curser = pygame.mouse.get_pos()
          #  print(curser)
            clicked = pygame.mouse.get_pressed()
           # print(clicked)
            if 955 <= curser[0] <= 1055 and 60 <= curser[1] <= 90:
                if clicked[0] == 1:
                    #pygame.display.flip()
                    done = True
                    while done:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_0:
                                    word+=str(chr(event.key))
                                elif event.key == pygame.K_1:
                                    word+=chr(event.key)
                                elif event.key == pygame.K_2:
                                    word+=chr(event.key)
                                elif event.key == pygame.K_3:
                                    word+=chr(event.key)
                                elif event.key == pygame.K_4:
                                    word += chr(event.key)
                                elif event.key == pygame.K_5:
                                    word += chr(event.key)
                                elif event.key == pygame.K_6:
                                    word += chr(event.key)
                                elif event.key == pygame.K_7:
                                    word += chr(event.key)
                                elif event.key == pygame.K_8:
                                    word += chr(event.key)
                                elif event.key == pygame.K_9:
                                    word += chr(event.key)
                                elif event.key == pygame.K_BACKSPACE:
                                    word = word[:-1]
                                elif event.key == pygame.K_RETURN:
                                    done = False
                myfont = pygame.font.SysFont("comicsansms", 20)
                old_word = word
                #print(word)
                print(str(word))
                print('hello')
                word = int(word)
                window_size = word
                word = ""
                # render text
                label = myfont.render(old_word, 1, black)
                gameDisplay.blit(label, (1000, 65))
            if 955 <= curser[0] <= 1055 and 130 <= curser[1] <= 160:
                if clicked[0] == 1:
                    # pygame.display.flip()
                    done = True
                    while done:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_0:
                                    word += str(chr(event.key))
                                elif event.key == pygame.K_1:
                                    word += chr(event.key)
                                elif event.key == pygame.K_2:
                                    word += chr(event.key)
                                elif event.key == pygame.K_3:
                                    word += chr(event.key)
                                elif event.key == pygame.K_4:
                                    word += chr(event.key)
                                elif event.key == pygame.K_5:
                                    word += chr(event.key)
                                elif event.key == pygame.K_6:
                                    word += chr(event.key)
                                elif event.key == pygame.K_7:
                                    word += chr(event.key)
                                elif event.key == pygame.K_8:
                                    word += chr(event.key)
                                elif event.key == pygame.K_9:
                                    word += chr(event.key)
                                elif event.key == pygame.K_BACKSPACE:
                                    word = word[:-1]
                                elif event.key == pygame.K_RETURN:
                                    done = False
                myfont = pygame.font.SysFont("comicsansms", 20)
                old_word = word
                # print(word)
                print(str(word))
                print('hello')
                word = int(word)
                thing_speed = word
                # render text
                label = myfont.render(old_word, 1, black)
                gameDisplay.blit(label, (1000, 135))
                pygame.display.update()



def main_loop():
    gameEx = False
    while not gameEx:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEx = True
        blocks()
        draw()
        #win()
        # Play and Pause
        inpt()
        inpt()
        #inpt2()
        pygame.display.update()
        button("start", 670, 247, 100, 40, green, light_green, action="play")
        button("stop", 850, 247, 100, 40, red, light_red, action="quit")


        pygame.display.update()
def resend(starx):
    global starty
    global startx
    global window_size
    global thing_speed
    global initial_x
    y = starty
    x = startx
    k=0
    store = [None]*window_size
    for i in range(0,window_size):
        #print('wolla2!')
        if bool[i] == True:
            store[k] = i
           # print('store k is' , store[k])
            k+=1
            bool[i] = False
           # print('wolla!')
            guns[i] = pygame.image.load('gun1.jpg')
            funs[i] = pygame.image.load('fun1.jpg')
            i+=1
    if k==0:
        initial_x = initial_x + 60*window_size
        if initial_x >= 1250:
            initial_x = 50
        starty = 350
        game_loop()


    starty = 350
    y = starty
    while y <= 580:
        y += thing_speed
        for cnt in range(0, window_size):
            gameDisplay.fill(white)
            draw()
            blocks()
            # clock.tick(60)
            win()
            c = 0
            for flag in store:
                c+=1
                if c>k:
                    break
                #print(flag)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        curser = pygame.mouse.get_pos()
                       # print(curser)
                        clicked = pygame.mouse.get_pressed()
                        #print(clicked)
                        for val in range(0, window_size):
                            if starx[val] <= curser[0] <= starx[val] + thing_width and y <= curser[1] <= y + thing_height:
                                if clicked[0] == 1:
                                   # print('hello')
                                    guns[val] = pygame.image.load('white.jpg')
                                    bool[val] = True
                                    funs[val] = pygame.image.load('white.jpg')
                                    # gameDisplay.blit(whiteIm, (starx[flag], starty))
                                    pygame.display.update()
                            val += 1

                gameDisplay.blit(guns[flag], (starx[flag], y))
                draw()
                win()
                #flag += 1
            pygame.display.update()
    starty = 580
    y = starty
    while y >= 350:
        y -= thing_speed
        for cont in range(0, window_size):
            gameDisplay.fill(white)
            draw()
            blocks()
            #win()
            # clock.tick(60)
            c=0
            for flag in store:
                c+=1
                if c>k:
                    break
                print(flag)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        curser = pygame.mouse.get_pos()
                       # print(curser)
                        clicked = pygame.mouse.get_pressed()
                       # print(clicked)
                        for val in range(0, window_size):
                            if starx[val] <= curser[0] <= starx[val] + thing_width and y <= curser[1] <= y + thing_height:
                                if clicked[0] == 1:
                                   # print('hello')
                                    guns[val] = pygame.image.load('white.jpg')
                                    bool[val] = True
                                    funs[val] = pygame.image.load('white.jpg')
                                    win()
                                    # gameDisplay.blit(whiteIm, (starx[flag], starty))
                                    pygame.display.update()
                            val += 1

                gameDisplay.blit(funs[flag], (starx[flag], y))
                draw()
                win()
                #flag += 1
            pygame.display.update()
        #i+=1
    count = 0
    for i in range(0,window_size):
        if bool[i] == False:
            count+=1
    if count!=window_size:
        resend(starx)
    if count == window_size:
        initial_x = initial_x + 60*window_size
        if initial_x >=1250:
            initial_x = 50
        starty = 350
        game_loop()

def game_loop():
    gameExit = False
    global thing_speed
    global window_size
    global startx
    global starty
    global initial_x
    #button("controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
    #button("quit", 550, 500, 100, 50, red, light_red, action="quit")
    startx = initial_x
    starty = 350
    draw()
    pygame.display.update()
    var = 0
    var1 = 0
    var2 = 0
    starx = [None]*window_size
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if gameExit == True:
                quit()
                pygame.quit()
            x = startx
            if var == 0:
                for count in range(0, window_size):
                    starx[count] = x
                    x += 60
                    count += 1
                var = count
                #print(count)
            if var1 == 0:
                y = starty
                while y <=580:
                        y += thing_speed
                        for cnt in range(0, window_size):
                            gameDisplay.fill(white)
                            draw()
                            blocks()
                            win()
                            #clock.tick(60)

                            flag =0
                            while flag < window_size:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        curser = pygame.mouse.get_pos()
                                       # print(curser)
                                        clicked = pygame.mouse.get_pressed()
                                       # print(clicked)
                                        for val in range(0,window_size):
                                            if starx[val] <= curser[0] <= starx[val] + thing_width and y <= curser[1] <= y + thing_height:
                                                if clicked[0] == 1:
                                                 #   print('hello')
                                                    guns[val] = pygame.image.load('white.jpg')
                                                    funs[val] = pygame.image.load('white.jpg')
                                                    bool[val] = True
                                                    #gameDisplay.blit(whiteIm, (starx[flag], starty))
                                                    pygame.display.update()
                                            val+=1

                                gameDisplay.blit(guns[flag], (starx[flag], y))
                                draw()
                                win()
                                flag += 1

                            pygame.display.update()

                    #starty = 350

                startx = initial_x
                starty = 580
                y = starty
                var1 = cnt
            if var2 == 0:
                while y >=350:
                        y -= thing_speed
                        for cont in range(0, window_size):
                            gameDisplay.fill(white)
                            draw()
                            blocks()
                            win()
                            #clock.tick(60)
                            flag =0
                            while flag < window_size:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        curser = pygame.mouse.get_pos()
                                      #  print(curser)
                                        clicked = pygame.mouse.get_pressed()
                                        #print(clicked)
                                        for val in range(0,window_size):
                                            if starx[val] <= curser[0] <= starx[val] + thing_width and y <= curser[1] <= y + thing_height:
                                                if clicked[0] == 1:
                                                   # print('hello')
                                                    guns[val] = pygame.image.load('white.jpg')
                                                    funs[val] = pygame.image.load('white.jpg')
                                                    bool[val] = True
                                                    #gameDisplay.blit(whiteIm, (starx[flag], starty))
                                                    pygame.display.update()
                                            val+=1
                                gameDisplay.blit(funs[flag], (starx[flag], y))
                                draw()
                                win()
                                flag += 1

                            pygame.display.update()
                resend(starx)
                    #starty = 350
                startx = initial_x
                var2 = cont
main_loop()
pygame.quit()
quit()