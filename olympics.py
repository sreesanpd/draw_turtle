import turtle

def draw_canvas():
	window = turtle.Screen()
	window.bgcolor("red")

def close_canvas():
	window = turtle.Screen()
	window.exitonclick()

def draw_circle(some_turtle, radius):
	some_turtle.circle(radius)

def main():
	draw_canvas()
	
	bob = turtle.Turtle()
	bob.shape = turtle
	draw_circle(bob, 50)
	
	bob.penup()
	bob.setposition(-120, 0)
	bob.pendown()
	draw_circle(bob, 50)

	bob.penup()
	bob.setposition(60, 60)
	bob.pendown()
	draw_circle(bob, 50)
	
	bob.penup()
	bob.setposition(-60, 60)
	bob.pendown()
	draw_circle(bob, 50)

	bob.penup()
	bob.setposition(-180, 60)
	bob.pendown()
	draw_circle(bob, 50)
	
	close_canvas()
	
main()
	
