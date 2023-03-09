from turtle import *
speed(2)
shape("turtle")

sides = 4
length = 20
angle = 360/sides

for count in range(sides):
 forward(length)
 right(angle)
 