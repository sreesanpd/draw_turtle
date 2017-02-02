import turtle


def draw_canvas():
	window = turtle.Screen()
	window.bgcolor("red")

def close_canvas():
	window = turtle.Screen()
	window.exitonclick()

def draw_square():
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(1)

	for i in [1,2,3,4]:
		brad.forward(100)
		brad.right(90)

def draw_circle():

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("green")
	angie.speed(7)

	angie.left(40)
	angie.circle(120)
	
	
draw_canvas()
draw_square()
draw_circle()
close_canvas()
