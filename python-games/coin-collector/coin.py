import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

#fox the coin collector
fox = Actor("fox")
fox.pos = 100,100

#coin
coin = Actor("coin")
coin.pos = 200,200


def draw():
    screen.fill("#00A300")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft= (10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final score "+ str(score), topleft =(10,10), fontsize = 60)


def coin_place():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 5
    elif keyboard.right:
        fox.x = fox.x +5
    elif keyboard.up:
        fox.y  = fox.y -5
    elif keyboard.down:
        fox.y = fox.y +5

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score +10
        coin_place()

clock.schedule(time_up,10.0)
coin_place()

pgzrun.go()
