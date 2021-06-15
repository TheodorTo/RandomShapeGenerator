
import turtle
import random

scn = turtle.Screen()
scn.bgcolor("white")
t = turtle.Turtle()
turtle.title("My Turtle Programm")
scn.colormode(255)


class Shapes():

    def __init__(self, positionxci, positionyci, positionxcu, positionycu, positionxor, positionyor, megethos, megethos2, thickness, rgb1, rgb2, rgb3):
        self.positionxci = positionxci
        self.positionyci = positionyci
        self.positionxcu = positionxcu
        self.positionycu = positionycu
        self.positionxor = positionxor
        self.positionyor = positionyor
        self.megethos = megethos
        self.megethos2 = megethos2
        self.thickness = thickness
        self.rgb1 = rgb1
        self.rgb2 = rgb2
        self.rgb3 = rgb3
        t.pencolor(int(self.rgb1), int(self.rgb2), int(self.rgb3))
        t.speed(13)
        t.fillcolor(self.rgb1, self.rgb2, self.rgb3)
        t.pensize(self.thickness)

    def circle(self):

        t.pu()
        t.goto(self.positionxci, self.positionyci)
        t.pd()
        t.begin_fill()
        t.circle(self.megethos)
        t.end_fill()
        t.penup()

    def orthogonio(self):
        t.pu()
        t.goto(self.positionxor, self.positionyor)
        t.pd()
        t.begin_fill()
        t.fd(self.megethos)
        t.rt(90)
        t.fd(self.megethos2)
        t.rt(90)
        t.fd(self.megethos)
        t.rt(90)
        t.fd(self.megethos2)
        t.rt(90)
        t.end_fill()

    def cube(self):
        t.pu()
        t.goto(self.positionxcu, self.positionycu)
        t.pd()
        t.begin_fill()
        t.fd(self.megethos)
        t.rt(90)
        t.fd(self.megethos)
        t.rt(90)
        t.fd(self.megethos)
        t.rt(90)
        t.fd(self.megethos)
        t.rt(90)
        t.end_fill()
        t.penup()


for i in range(0, 50):

    Teo = Shapes(positionxci=random.randint(-300, 300), positionyci=random.randint(-300, 300)
                 , positionxcu=random.randint(-300, 300), positionycu=random.randint(-300, 300)
                 , positionxor=random.randint(-300, 300), positionyor=random.randint(-300, 300)
                 , megethos=random.randint(30, 100)
                 , megethos2=random.randint(30, 200), thickness=random.randint(1, 20), rgb1=random.randint(0, 250), rgb2=random.randint(0, 250)
                 , rgb3=random.randint(0, 250))

    a = random.randint(0, 3)
    if a == 0:
        Teo.circle()
    if a == 1:
        Teo.cube()
    if a == 2:
        Teo.orthogonio()


turtle.done()
