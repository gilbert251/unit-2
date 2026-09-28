import turtle

t = turtle.Turtle()
t.speed(0)

def draw_star(size):
    for i in range(5):
        t.forward(size)
        t.right(144)

def draw_star_spiral():
    length = 5
    for i in range(2000):
        draw_star(length)
        t.right(5)
        length += 5

draw_star_spiral()
turtle.done()