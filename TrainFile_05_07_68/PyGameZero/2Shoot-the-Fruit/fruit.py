import pgzrun
from random import randint
def draw():
    # screen.fill((100, 200, 210))
    bg.draw()
    tree.draw()
    tree.y = 490
    tree.x = 120
    apple.draw()
    orange.draw()
    pineapple.draw()
    screen.draw.text("Score : " + str(score), topright=(790,10), fontsize = 30, color = "white")
    
def update():
    apple.y += apple.speed    
    if apple.y > 600:
        place_apple()
    orange.y += orange.speed    
    if orange.y > 600:
        place_orange()
    pineapple.y += pineapple.speed    
    if pineapple.y > 600:
        place_pineapple()
    
    
    
def place_apple():
    apple.x = randint(10, 750)
    apple.y = 0
    apple.speed = randint(1,3)
    
def place_orange():
    orange.x = randint(10, 750)
    orange.y = 0 #randint(10, 550)
    orange.speed = randint(2,4)
    
def place_pineapple():
    pineapple.x = randint(10, 750)
    pineapple.y = 0
    pineapple.speed = randint(2,5)
    
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        sounds.click.play() #foldername_filename.play()
        place_apple()
        score += 1
    elif orange.collidepoint(pos):
        sounds.click.play() #foldername_filename.play()
        place_orange()
        score += 1
    elif pineapple.collidepoint(pos):
        sounds.click.play() #foldername_filename.play()
        place_pineapple()
        score += 1
    else:
        print('Youu missed!')
    
TITLE = "Shoot the Fruit"
WIDTH = 800
HEIGHT = 600

bg = Actor('background')
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
tree = Actor('tree')
score = 0

place_apple()
place_orange()
place_pineapple()

pgzrun.go()
