import pgzrun

def draw():
    screen.fill((255,255,255))
    screen.draw.text("Hello World",topleft = (10,10), fontsize = 30, color = "red")
    screen.draw.text("Hello World",center = (200,150), fontsize = 40, color = "green")
    screen.draw.text("Hello World",topright = (390,270), fontsize = 30, color = "blue")
    

TITLE = "PY GAME"
WIDTH = 400
HEIGHT = 300

pgzrun.go() # last statement
