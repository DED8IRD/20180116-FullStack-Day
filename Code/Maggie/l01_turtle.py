from turtle import *



def redund_draw():
    # tell turtle to draw a square using static function calls
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)

def redund_fillsq():
    # tell turtle to make a filled square
    fillcolor('green')
    begin_fill()
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)
    forward(90)
    left(90)

def drawsq(side):
    i = 0
    while i < 4:
        forward(side)
        left(90)
        i += 1

def fillsq(side):
    fillcolor('red')
    begin_fill()
    i = 0
    while i < 4:
        forward(side)
        left(90)
        i += 1
    end_fill()

def star_draw(side):
    i = 0
    while i < 5:
        forward(100)
        right(144)
        i += 1
def n_sided(side, n):
    i = 0
    while i < n:
        forward(side/n)
        right(360/side)
        i += 1

def draw_stick(size): # long form
    # draw head
    circle(size/5)
    right(90) #turn right

    # draw body
    forward(size)  # draw body

    # draw legs
    right(30)  # turn for first leg
    forward(size/3) # draw leg
    right(180) # turn around
    forward(size/3) # go back
    right(120) # turn 2
    forward(size/3) # draw leg 2
    right(180) # turn around

    # draw arms
    forward(size/3)
    right(30)
    forward(size/float(1.5))
    right(100)
    forward(size/2)
    right(180)
    forward(size/2)
    left(20)
    forward(size/2)

def draw_stick2(size):
    # draw head
    circle(size / 5)
    # draw body

def move_face(x, y, face):
    penup()
    goto(x, y)
    if face == up:
        towards (x, y + 100)
    elif face == down:
        towards(x, y - 100)
    elif face == 'left':
        towards(x - 100, y)
    elif face == 'right':
        towards(x + 100, y)
    pendown()

def relocate(x , y):  # puts the turtle somewhere on the screen
    penup()
    goto(x,y)
    pendown()


# run the program
home()
draw_stick(200)
done()
bye()