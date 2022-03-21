import turtle
tao = turtle.Pen()
tao.speed(100)

def flow():
    for i in range(10):
        tao.pensize(3)
        tao.pencolor('blue')
        tao.circle(50)
        tao.left(36)

    tao.pencolor('green')
    tao.right(90)
    tao.forward(250)
flow()

    



    
