import os.path 
import turtle
from PIL import Image 
from glob import glob
import cv2
def drawSquare(t):
    
    for i in range(4):
        t.forward(100)
        t.left(90)

def drawRect(t):
    
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(100)
        t.left(90)

def drawTri(t):

   for i in range(3): 
    t.forward(100) 
    t.left(120)

def drawLine(t):
    t.forward(100)
    
def drawCircle(t):
        
        for i in range(360):
                t.forward( 100 * 3.14/ 360 )
                t.right(1)

def drawPentagon(t):
    t.forward(100)
    t.left(90)
    t.forward(58)
    for i in range(2):
        t.left(60)
        t.forward(58)
    t.left(60)
    t.forward(58)
def drawHexagon(t):
        for i in range(6):
                t.forward(100)
                t.left(60)
                
        
with open("inputDraw.txt") as fp:
      inpt=fp.readlines()

if inpt:
        words = inpt[0].split()
        t = turtle.Turtle()
        t.pensize(3)
        
                
        for temp in words:
                if(temp=="rectangle" or temp=="Rectangle"):
                        drawRect(t);       
                if(temp=="square" or temp=="Square"):
                        drawSquare(t);
                if(temp=="circle" or temp=="Circle"):
                        drawCircle(t);
                if(temp=="triangle" or temp=="Triangle"):
                        drawTri(t);
                if(temp=="pentagon" or temp=="Pentagon"):
                        drawPentagon(t);
                if(temp=="hexagon" or temp=="Hexagon"):
                        drawHexagon(t);        
                if(temp=="line" or temp=="Line"):
                        drawLine(t);
        ts = turtle.getscreen()

        ts.getcanvas().postscript(file="duck.eps")
        turtle.exitonclick()
        
 
        
            
        img = cv2.imread('duck.eps')
        cv2.imwrite('duck.jpg',img);
        
else:
        print("Can't recognise your voice!")

        

