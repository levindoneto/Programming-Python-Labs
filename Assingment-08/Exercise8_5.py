import turtle
import math

''' 
	Initial letters of each integrant of the group:
    LA
    VH  
'''

def main():
	# Put the pen down (start drawing)
	turtle.pendown()

	# L
	turtle.backward(100)
	turtle.left(90)
	turtle.forward(150) 
	turtle.penup() # stop
	turtle.right(90)
	turtle.forward(150)

	# A
	turtle.right(90+15) # to start the A's diagonal
	turtle.pendown() # start
	turtle.forward(160) 
	turtle.left(180)
	turtle.forward(160/2)
	turtle.right(90-15)
	turtle.forward(160/2)
	turtle.left(90+15)
	turtle.forward(160/2)
	turtle.left(90-15)
	turtle.forward(40)
	turtle.right(180)
	turtle.forward(40)
	turtle.right(90-15)
	turtle.forward(160)
	turtle.penup()

	# V
	turtle.right(90)
	turtle.forward(240)
	turtle.right(90+180)
	turtle.pendown()
	turtle.forward(140)
	turtle.left(180-40)
	turtle.forward(150) #  in rads
	turtle.penup()

	# H
	turtle.right(40)
	turtle.forward(40)
	turtle.right(40/20+90+20)
	turtle.right(4)
	turtle.forward(15)
	turtle.pendown()
	turtle.forward(140)
	turtle.left(180)
	turtle.forward(140/2)
	turtle.right(90)
	turtle.forward(70)
	turtle.left(90)
	turtle.forward(70)
	turtle.right(180)
	turtle.forward(150)

if __name__ == '__main__':
    main()