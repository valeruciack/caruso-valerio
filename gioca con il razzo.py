import pgzrun

WIDTH= 550

HEIGHT= 600

razzo = Actor("razzo")

def draw():
    screen.fill((128, 128, 105))
    razzo.draw()

pgzrun.go()
