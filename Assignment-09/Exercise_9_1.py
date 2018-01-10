import turtle
import sys

window = turtle.Screen()
window.bgcolor("lightgreen")

turtle.shape("turtle")

turtle.pendown()
while True:
    print("Type 'exit' to leave the application")
    e = input()
    if (e == "exit"):
        break
    print("How many steps?")
    z = input()
    print("left or right? or type 'exit' to leave the application")
    y = input()
    
    if (int(z) >= 0 and y == "left"):
        turtle.left(90)
        turtle.forward(int(z))
        continue
    if (int(z) >= 0 and y== "right"):
        turtle.right(90)
        turtle.forward(int(z))
        continue
		
sys.exit(0)