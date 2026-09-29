import turtle as t
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

def circle(x,y,radius, color):
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.pendown()
    t.begin_fill()
    
    t.circle(radius)
    
    t.end_fill()

#circle(100,100,100,"Blue")#Custom Filled Circle Function
#t.color("red")
#t.circle(50)#Turtle prebuilt circle function (not filled)

def draw_face(x,y, face_color):
    #Base Of Face
    circle(x,y,50,face_color)
    
    #Eyes
    
    circle(x-20,y+50,10,"white")#left white part
    circle(x+20,y+50,10,"white")#right
    
    #Pupils
    circle(x-20,y+55,5,"black")#left white part
    circle(x+20,y+55,5,"black")#right
    
    #Rectangle Mouth
    t.right(45)
    rectangle(x-15,y+35,30,10,"black")
    t.setheading(0)
    t.left(45)
    rectangle(x-5,y+15,30,10,"black")
    t.setheading(0)

def pentagon(x,y,color):
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.pendown()
    t.begin_fill()
    
    t.goto(x,y)
    t.goto(x+30,y-15)
    t.goto(x+20,y-30)
    t.goto(x-20,y-30)
    t.goto(x-30,y-15)
    t.goto(x,y)
    
    t.end_fill()

t.bgcolor("dark blue")
t.speed("fastest")
pentagon(0,0,"green")
pentagon(100,100,"blue")

#draw_face(0,0,"red")
draw_face(-100,-100,"blue")

