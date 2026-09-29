#July_25_KaleidoSpiral
import turtle as t
import random as r
t.speed("fastest")
t.bgcolor("black")

t.color("white")

"""
1. Circles Get Bigger [X]
2. Circles move arround in a circular pattern [X]
    A. Cursor move forward [X]
    B. Turn a bit [X]
3. Circles Change Color
"""
radius = 10

list_of_colors = ["red","orange","yellow","lime","green","turquoise","blue","purple","magenta"]
index = 0

while True:
    #t.color(list_of_colors[index])
    t.color(r.choice(list_of_colors))
    t.circle(radius)
    radius += 10
    index += 1
    
    if index == len(list_of_colors):
        index = 0
    
    t.forward(5)
    t.right(10)#Angle will change the size of the center void thing