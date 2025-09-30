import turtle

def pythagoras_tree(t: turtle.Turtle, length: float, depth: int):
    if depth == 0:
        return

    # намалювати основну гілку
    t.forward(length)
    pos = t.pos()       # кінець цієї гілки
    angle = t.heading() # кут гілки

    # ліва гілка
    t.left(45)
    pythagoras_tree(t, length * 0.7, depth - 1)

    # відновлюємо стан
    t.penup()
    t.goto(pos)
    t.setheading(angle)
    t.pendown()

    # права гілка
    t.right(45)
    pythagoras_tree(t, length * 0.7, depth - 1)

    # повертаємося у початок поточної гілки
    t.penup()
    t.goto(pos)
    t.setheading(angle)
    t.backward(length)
    t.pendown()


def paint_pyphagor_tree(length: int, depth: int):
    window = turtle.Screen()
    window.bgcolor("white")


    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.left(90)
    t.goto(0, -100)
    t.pendown()

    pythagoras_tree(t, length, depth)

    window.mainloop()
paint_pyphagor_tree(100, 10)

