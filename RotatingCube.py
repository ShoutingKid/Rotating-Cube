import turtle
import sys
from math import sin,cos

class Cube:
    
    def __init__(self, side) -> None:

        self.win = turtle.Screen()
        self.win.setup(900, 600)
        self.win.tracer(0)

        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.color('black')

        self.side = side
        self.counter = 0
        self.e = [(0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)]
        self.v = []

        mid = side/2
        SIGNS = [(-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,1), (1,-1,1), ( 1,1,1), (-1,1,1)]
        for x, y, z in SIGNS:
            self.v.append((x*mid, y*mid, z*mid))

    def __clear(self):
        self.turtle.clear()

    def __update(self):
        self.win.update()

    def __fps(self):
        self.counter += 0.005
        if(self.counter > 10000): 
            self.counter = 0

    def __rotate(self, x,y,r):
        #return x, y
        s,c = sin(r), cos(r)
        return x*c-y*s, x*s+y*c

    def __draw(self):
        for edge in self.e:
            points = []
            
            for vertex in edge:
                x,y,z = self.v[vertex] 

                x,z = self.__rotate(x,z,self.counter) # Only this one to rotate around y
                y,z = self.__rotate(y,z,self.counter) # Only this for x
                x,y = self.__rotate(x,y,self.counter) # This for z
                
                z += 8
                if z != 0:
                    f = 400/(z)  # f gives size/distance (smaller value = smaller cube)
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)

            self.turtle.up()
            self.turtle.goto(points[0], points[1])
            self.turtle.down()
            self.turtle.goto(points[2], points[3])
            self.turtle.up()

    def loop(self):
        try:
            while (True):
                self.__clear()
                self.__draw()
                self.__update()
                self.__fps()
        except:
            pass


def main()->None:
    #sys.argv.append(4)
    argc = len(sys.argv)
    if(argc != 2): 
        print ('expected cube dimension as input!')
        exit(1)
    side = int(sys.argv[1])
    print(f'creating cube of length: {side}')
    cube = Cube(side)
    cube.loop()

if __name__ == "__main__":
    main()
