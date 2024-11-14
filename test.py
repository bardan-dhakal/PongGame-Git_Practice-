import turtle

window = turtle.Screen()
window.title("My Game")
window.bgcolor("black")
window.setup(1200, 700, starty = 10)
window.tracer(0)

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(5,1)
paddle1.penup()
paddle1.setx(-550)

while True:
    window.update()

turtle.done()