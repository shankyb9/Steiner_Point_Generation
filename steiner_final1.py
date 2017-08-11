from sympy.geometry import *
import math
import numpy as np
import turtle

turtle.speed(1)
#turtle.hideturtle()
def create_triangle_point(p2,p4,p3):
    T1=Triangle(p2,p4,p3)#creating traingle

    x=(math.cos(math.pi/3)*(p4[0]-p2[0])-math.sin(math.pi/3)*(p4[1]-p2[1]))+p2[0]
    if p3[1] > p2[1]:
        y=-(math.sin(math.pi/3)*(p4[0]-p2[0])-math.cos(math.pi/3)*(p4[1]-p2[1]))+p2[1]
    else:
        y=(math.sin(math.pi/3)*(p4[0]-p2[0])-math.cos(math.pi/3)*(p4[1]-p2[1]))+p2[1] 

    #print x,y
    p7=Point(x,y)
    #print float(P4[0]),float(P4[1])
    T2=Triangle(p2,p4,p7)
    Centroid=T2.centroid
    #print Circum
    S1=Segment(Centroid,p7)
    radius= float(S1.length)
    C1=Circle(Centroid,radius)
    S2=Line(p3,p7)
    a1=np.array(C1.intersection(S2))
    #print float(a1[0,0])
    #print float(a1[0,1])
    x=float(a1[0,0])
    y=float(a1[0,1])
    p8=Point(x,y)
    #print x,y
    #print a1
    return p8

def create_rectangle_steiner(p1,p2,p3,p4):
    k=(p3[1]+p1[1])/2

    x=(k-p1[1])/math.tan(math.pi/3)
    SP1=Point(p1[0]+x,k) 
    SP2=Point(p2[0]-x,k) 

    return SP1,SP2


    
def triangle_func():
    print 'Enter x and y coordinate for 1st point'
    x=int(raw_input())
    y=int(raw_input())
    P1=Point(x,y)#0,0

    print 'Enter x and y coordinate for 2nd point'
    x=int(raw_input())
    y=int(raw_input())
    P2=Point(x,y)#40,0

    print 'Enter x and y coordinate for 3rd point'
    x=int(raw_input())
    y=int(raw_input())
    P3=Point(x,y)#20,20

    ST1=create_triangle_point(P1,P2,P3)

    
    turtle.pencolor("black")
    turtle.fillcolor("Yellow")
    turtle.penup()
    turtle.goto(P1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(P2)
    turtle.goto(P3)
    turtle.goto(P1)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(ST1)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(P1)
    
    print float(ST1[0]),float(ST1[1])


def rectangle_func():
    print 'Enter x and y coordinate for 1st point'
    x=int(raw_input())
    y=int(raw_input())
    P1=Point(x,y)#0,0

    print 'Enter x and y coordinate for 2nd point'
    x=int(raw_input())
    y=int(raw_input())
    P2=Point(x,y)#40,0

    print 'Enter x and y coordinate for 3rd point'
    x=int(raw_input())
    y=int(raw_input())
    P3=Point(x,y)#20,20

    print 'Enter x and y coordinate for 4th point'
    x=int(raw_input())
    y=int(raw_input())
    P4=Point(x,y)#20,20
    
    ST1,ST2=create_rectangle_steiner(P1,P2,P3,P4)

    turtle.pencolor("black")
    turtle.fillcolor("Yellow")
    turtle.penup()
    turtle.goto(P1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(P2)
    turtle.goto(P3)
    turtle.goto(P4)
    turtle.goto(P1)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(ST1)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(ST2)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(P1)
    
    print float(ST1[0]),float(ST1[1])
    print float(ST2[0]),float(ST2[1])

def pentagon_func():

    print 'Enter x and y coordinate for 1st point'
    x=int(raw_input())
    y=int(raw_input())
    P1=Point(x,y)#0,0

    print 'Enter x and y coordinate for 2nd point'
    x=int(raw_input())
    y=int(raw_input())
    P2=Point(x,y)#40,0

    print 'Enter x and y coordinate for 3rd point'
    x=int(raw_input())
    y=int(raw_input())
    P3=Point(x,y)#20,20

    print 'Enter x and y coordinate for 4th point'
    x=int(raw_input())
    y=int(raw_input())
    P4=Point(x,y)#20,20

    print 'Enter x and y coordinate for 5th point'
    x=int(raw_input())
    y=int(raw_input())
    P5=Point(x,y)#20,20

    ST1=create_triangle_point(P2,P4,P3)
    ST2,ST3=create_rectangle_steiner(P1,P5,P4,P2)

    turtle.pencolor("black")
    turtle.fillcolor("Yellow")
    turtle.penup()
    turtle.goto(P1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(P2)
    turtle.goto(P3)
    turtle.goto(P4)
    turtle.goto(P5)
    turtle.goto(P1)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(ST1)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(ST2)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(ST3)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(P1)

    
    print float(ST1[0]),float(ST1[1])
    print float(ST2[0]),float(ST2[1])
    print float(ST3[0]),float(ST3[1])

def hexagon_func():

    print 'Enter x and y coordinate for 1st point'
    x=int(raw_input())
    y=int(raw_input())
    P1=Point(x,y)#0,0

    print 'Enter x and y coordinate for 2nd point'
    x=int(raw_input())
    y=int(raw_input())
    P2=Point(x,y)#40,0

    print 'Enter x and y coordinate for 3rd point'
    x=int(raw_input())
    y=int(raw_input())
    P3=Point(x,y)#20,20

    print 'Enter x and y coordinate for 4th point'
    x=int(raw_input())
    y=int(raw_input())
    P4=Point(x,y)#20,20

    print 'Enter x and y coordinate for 5th point'
    x=int(raw_input())
    y=int(raw_input())
    P5=Point(x,y)#20,20

    print 'Enter x and y coordinate for 6th point'
    x=int(raw_input())
    y=int(raw_input())
    P6=Point(x,y)#20,20

    ST1=create_triangle_point(P1,P3,P2)#upper triangle
    ST2,ST3=create_rectangle_steiner(P6,P4,P3,P1)#middle rectangle
    ST4=create_triangle_point(P6,P4,P5)#lower triangle

    turtle.pencolor("black")
    turtle.fillcolor("Yellow")
    turtle.penup()
    turtle.goto(P1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(P2)
    turtle.goto(P3)
    turtle.goto(P4)
    turtle.goto(P5)
    turtle.goto(P6)
    turtle.goto(P1)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(ST1)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(ST2)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(ST3)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(ST4)
    turtle.pendown()
    turtle.dot(10,"red")
    turtle.penup()
    turtle.goto(P1)

    print float(ST1[0]),float(ST1[1])
    print float(ST2[0]),float(ST2[1])
    print float(ST3[0]),float(ST3[1])
    print float(ST4[0]),float(ST4[1])
    

shape=raw_input("Enter the shape u want(triangle,rectangle,pentagon,hexagon)?  ")
shapes={
    "triangle":triangle_func,
    "rectangle":rectangle_func,
    "pentagon":pentagon_func,
    "hexagon":hexagon_func}

shapes.get(shape)()
#turtle.showturtle()
turtle.done()



