import pgzrun
from random import randint 

WIDTH = 600
HEIGHT = 400

#a = Actor("a")
#d = Actor("d")
g = Actor("g")
#o = Actor("o")


score = 0
game_over = False

def draw():
    screen.clear()
    #a.draw()
    #d.draw()
    g.draw()
    #o.draw()
    screen.draw.text("Score: " + str(score), topleft = (10,10))

    if game_over:
        screen.fill("white")
        screen.draw.text("You Missed the G \n Total Score: " + str(score), color = "black", topleft = (10,10),fontsize = 70)

def place_p():
    #a.x = randint(20, (WIDTH-20))
    #a.y= randint(20, (HEIGHT-20))
    #d.x = randint(20, (WIDTH-20))
    #d.y = randint(20, (HEIGHT-20))
    g.x= randint(20, (WIDTH-20))
    g.y= randint(20, (HEIGHT-20))
    #o.x = randint(20, (WIDTH-20))
    #o.y = randint(20, (HEIGHT-20))

def on_mouse_down(pos):
    global score
    global game_over
    if g.collidepoint(pos):
        score +=1
        print(score)
        print("Good shot!")
        place_p()
    else:
        game_over= True
    '''elif d.collidepoint(pos):
        print("Wrong shot!")
        game_over= True
        
    elif a.collidepoint(pos):
        print("Wrong shot!")
        game_over= True
    elif o.collidepoint(pos):
        print("Wrong shot!")
        game_over= True
    '''
    
        

place_p()

pgzrun.go()
