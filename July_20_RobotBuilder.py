import turtle as t
t.bgcolor("dark blue")
t.speed("fastest")


def rectangle(x,y,width,height,color):
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.pendown()
    t.begin_fill()
    
    for i in range(2):
        t.forward(width) #Moves the Width Distance
        t.right(90) #Turns 90 degrees
        t.forward(height) #Moves the Height Distance
        t.right(90)
    
    t.end_fill()


def left_arm(x,y,color):
    t.penup()
    t.goto(x,y)
    
    rectangle(x,y, 25, 50, color)
    rectangle(x,y-50, 75 ,25, color)
    
    #t.color(color)
def right_arm(x,y,color):
    t.penup()
    t.goto(x,y)
    
    rectangle(x-25,y, 25, 50, color)
    rectangle(x-75,y-50, 75 ,25, color) 
    
    

#Left Foot
rectangle(-100,-150, 50, 25,"yellow")
#Left Leg
rectangle(-60,-25, 10, 125, "black")

#Right Foot
rectangle(-25,-150, 50, 25, "yellow")
#Right Leg
rectangle(-25, -25, 10, 125, "black")

#Torso
rectangle(-100,175,125,200,"red")

#Neck
rectangle(-50,200, 25,25,"grey")

#Head
rectangle(-100,275,125,75,"red")

#Left eye
rectangle(-90,265,35,35,"white")
rectangle(-80,245,15,15,"black")

#Right eye
rectangle(-20,265,35,35,"white")
rectangle(-10,245,15,15,"black")

#Mouth
rectangle(-75,215, 75, 10, "black")


left_arm(-175,200,"grey")
left_arm(-175,115,"grey")

right_arm(100,200,"grey")
right_arm(100,115,"grey")
#finish rest for your hw
#Try to create a function for each of the arms
