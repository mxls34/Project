import pgzrun
# function for draw graphics
def draw():
    screen.fill( (255, 255, 255) )
    screen.draw.text('Hello World',topleft=(10,10),fontsize=30,color='Red')
    screen.draw.text('Hello World',center=(200,150),fontsize=40,color='green')
    screen.draw.text('Hello World',topright=(390,270),fontsize=30,color='blue')

# define title and size of windows
WIDTH = 400
HEIGHT = 300
TITLE = "Hello World"
pgzrun.go()
