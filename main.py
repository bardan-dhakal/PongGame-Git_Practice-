import turtle
import winsound

# Set up the screen
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=1200, height=700)
window.tracer(0)

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-550, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(550, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)  # This is the animation speed, not movement speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Scoring
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Player A : 0  Player B : 0", align="center", font=("Courier", 24, "bold"))

# Functions to move the paddles
def paddle1_up():
    y = paddle1.ycor()
    if y < 305:
        paddle1.sety(y + 20)

def paddle1_down():
    y = paddle1.ycor()
    if y > -305:
        paddle1.sety(y - 20)

def paddle2_up():
    y = paddle2.ycor()
    if y < 305:
        paddle2.sety(y + 20)

def paddle2_down():
    y = paddle2.ycor()
    if y > -305:
        paddle2.sety(y - 20)

# Keyboard binding
window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")

# Main game loop
try:
    while True:
        window.update()
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision
        if ball.ycor() > 340 or ball.ycor() < -340:
            ball.dy *= -1
            winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

        if ball.xcor() > 590:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
            winsound.PlaySound("score.wav", winsound.SND_ASYNC)

        if ball.xcor() < -590:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
            winsound.PlaySound("score.wav", winsound.SND_ASYNC)

        # Paddle collision
        if (540 < ball.xcor() < 550) and (paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
            ball.setx(540)
            ball.dx *= -1
            winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

        if (-540 > ball.xcor() > -550) and (paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50):
            ball.setx(-540)
            ball.dx *= -1
            winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

except turtle.Terminator:
    print("Game exited.")
