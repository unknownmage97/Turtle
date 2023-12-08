import turtle
import random
import time

tommy = turtle.Turtle()
class Shapes:
    def add_color(self) -> None:
        '''
        adds a random color to turtle using rgb color scheme
        :return: None
        '''
        num_1 = random.randint(0, 255)
        num_2 = random.randint(0, 255)
        num_3 = random.randint(0, 255)
        tommy.pencolor(num_1, num_2, num_3)

    def star(self) -> None:
        '''
        creates 4 *-like shapes
        :return: None
        '''
        for z in range(4):
            tommy.penup()
            tommy.goto(random.randint(-500, 500), random.randint(-200, 200))
            tommy.pendown()
            for x in range(37):
                self.add_color()
                tommy.forward(170)
                tommy.left(30)
                tommy.forward(50)
                tommy.left(155)
                tommy.forward(190)
        time.sleep(3)

    def illusion(self) -> None:
        '''
        creates an illusion like shape
        :return: None
        '''
        tommy.penup()
        tommy.goto(random.randint(-350, 350), random.randint(-100, 100))
        tommy.pendown()
        for x in range(36):
            self.add_color()
            tommy.forward(100)
            tommy.left(20)
            tommy.forward(130)
            tommy.left(20)
            tommy.forward(130)
            tommy.left(130)
            tommy.forward(180)
        time.sleep(3)


    def rose(self) -> None:
        '''
        creates 5 rose-like shapes
        :return: None
        '''
        for z in range(5):
            tommy.penup()
            tommy.goto(random.randint(-500, 500), random.randint(-250, 250))
            tommy.pendown()
            for x in range(6):
                self.add_color()
                tommy.left(30)
                for x in range(12):
                    tommy.forward(70)
                    tommy.left(50)
        time.sleep(3)


    def non(self) -> None:
        '''
        creates nonagons in circle patterns
        :return:None
        '''
        for z in range(2):
            tommy.penup()
            tommy.goto(random.randint(-300, 300), 0)
            tommy.pendown()
            for x in range(9):
                self.add_color()
                tommy.left(40)
                for x in range(9):
                    tommy.forward(120)
                    tommy.left(40)
        time.sleep(3)


    def hex(self) -> None:
        '''
        creates 4 connected circles and fills them with 6 overlapping hexagons
        :return: None
        '''
        for z in range(2):
            tommy.penup()
            tommy.goto(random.randint(-300, 300), random.randint(-100, 100))
            tommy.pendown()
            for x in range(4):
                tommy.right(90)
                for x in range(6):
                    self.add_color()
                    tommy.forward(70)
                    tommy.left(30)
                    tommy.forward(70)
                    tommy.left(30)
                    for x in range(6):
                        tommy.forward(70)
                        tommy.left(60)
        time.sleep(3)


    def tri(self) -> None:
        '''
        creates star patterns using triangles
        :return: None
        '''
        for z in range(4):
            tommy.penup()
            tommy.goto(random.randint(-500, 500), random.randint(-400, 400))
            tommy.pendown()
            for x in range(35):
                self.add_color()
                tommy.forward(50)
                tommy.left(90)
                tommy.forward(70)
                tommy.left(150)
                tommy.forward(70)
                if x != 0 and x % 3 == 0:
                    tommy.left(30)
        time.sleep(3)


    def sun(self) -> None:
        '''
        creates an odd sun-like pattern
        :return: None
        '''
        for z in range(2):
            tommy.penup()
            tommy.goto(random.randint(-250, 250), random.randint(-100,100))
            tommy.pendown()
            for x in range(50):
                self.add_color()
                tommy.forward(50)
                tommy.left(50)
                tommy.forward(100)
                tommy.left(180)
                tommy.forward(100)
                tommy.left(50)
                tommy.forward(100)
                if x != 0 and x % 3 == 0:
                    tommy.left(30)
            time.sleep(3)


    def start(self) -> None:
        '''
        starts the program, creates an infinite loop that rotates through the various shapes randomly
        keep: randomly decides if the current drawing/shape is kept (20% chance to keep)
        redundant, option: if drawing is kept, will make sure the same drawing is not made twice in a row
        :return: None
        '''
        redundant = 5
        while True:
            option = random.randint(0, 6)
            keep = random.randint(1, 5)
            self.add_color()
            while redundant == option:
                option = random.randint(0, 6)
            if option == 0:
                self.illusion()
            elif option == 1:
                self.star()
            elif option == 2:
                self.hex()
            elif option == 3:
                self.non()
            elif option == 4:
                self.rose()
            elif option == 5:
                self.tri()
            elif option == 6:
                self.sun()
            if keep > 1:
                tommy.clear()
                redundant = 7
            elif keep == 1:
                redundant = option

