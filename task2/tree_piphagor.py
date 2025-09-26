import turtle



def tree_piphagor_segment(t: turtle.Turtle, length: int, depth: int, angle: int = 30):

    if depth == 0:
       return t.pos()

    t.forward(length)
    current_pos = t.pos()
    current_heading = t.heading()

    t.left(30)
    tree_piphagor_segment(t, length * 0.7, depth - 1, angle)

    t.penup()
    t.setpos(current_pos)
    t.setheading(current_heading)
    t.pendown()

    t.right(30)
    tree_piphagor_segment(t, length * 0.7, depth - 1, angle)

    t.penup()
    t.setpos(current_pos)
    t.setheading(current_heading)
    t.pendown()


def paint_piphagor_tree(length: int, depth: int):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.left(90)
    t.goto(0, -300)
    t.pendown()

    tree_piphagor_segment(t, length, depth)
    current_pos = t.pos()
    current_heading = t.heading()

    for _ in range(10):
        for i in range(3):
            t.left(30)
            tree_piphagor_segment(t, length,  depth)
        t.penup()
        t.setpos(current_pos)
        t.setheading(current_heading)
        t.pendown()
        for i in range(3):
            t.right(30)
            tree_piphagor_segment(t, length, depth)
        t.penup()
        t.setpos(current_pos)
        t.setheading(current_heading)
        t.pendown()
        t.left(30)


    window.mainloop()

paint_piphagor_tree(100, 2)