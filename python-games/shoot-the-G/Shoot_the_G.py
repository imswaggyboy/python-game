import pgzrun
from random import randint 

WIDTH = 600
HEIGHT = 400

g = Actor("g")


score = 0
game_over = False

def draw():
    screen.clear()
    g.draw()
    screen.draw.text("Score: " + str(score), topleft = (10,10))

    if game_over:
        screen.fill("white")
        screen.draw.text("You Missed the G \n Total Score: " + str(score), color = "black", topleft = (10,10),fontsize = 70)

def place_p():
    g.x= randint(20, (WIDTH-20))
    g.y= randint(20, (HEIGHT-20))
    
    
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
