import turtle


def draw_canvas():
	window = turtle.Screen()
	window.bgcolor("red")

def close_canvas():
	window = turtle.Screen()
	window.exitonclick()

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_circle(some_turtle):
	some_turtle.left(40)
	some_turtle.circle(120)

def draw_art():
	draw_canvas()
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(5)

	for i in range(1,37):
		draw_square(brad)	
		brad.right(10)

#	angie = turtle.Turtle()
#	angie.shape("arrow")
#	angie.color("blue")
#	angie.speed(7)
#	draw_circle(angie)

	close_canvas()

draw_art()	
