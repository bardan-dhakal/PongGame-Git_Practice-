import turtle
import winsound
import math

# Set up the screen
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=1200, height=700)
window.tracer(0)

# Constants
BALL_SPEED = 0.15  # Fixed ball speed

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
ball.speed(1)  # Animation speed, not movement speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Set initial angle
angle = 45  # You can change this to experiment with different start angles
ball.dx = BALL_SPEED * math.cos(math.radians(angle))
ball.dy = BALL_SPEED * math.sin(math.radians(angle))

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

def quit_game():
    """Function to quit the game and close the window."""
    window.bye()

# Keyboard binding
window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")
window.onkeypress(quit_game, "q")  # Press 'q' to quit the game

# Main game loop
try:
    while True:
        try:
            window.update()
        except turtle.Terminator:
            print("Game window closed.")
            break
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision (Top/Bottom)
        if ball.ycor() > 340 or ball.ycor() < -340:
            ball.dy = -ball.dy  # Reverse the y direction
            winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

        # Border collision (Left/Right - Scoring)
        if ball.xcor() > 590:
            ball.goto(0, 0)
            angle = 45 if score_a % 2 == 0 else 135  # Alternate angles for variety
            ball.dx = BALL_SPEED * math.cos(math.radians(angle))
            ball.dy = BALL_SPEED * math.sin(math.radians(angle))
            score_a += 1
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
            winsound.PlaySound("score.wav", winsound.SND_ASYNC)

        if ball.xcor() < -590:
            ball.goto(0, 0)
            angle = -45 if score_b % 2 == 0 else -135  # Alternate angles for variety
            ball.dx = BALL_SPEED * math.cos(math.radians(angle))
            ball.dy = BALL_SPEED * math.sin(math.radians(angle))
            score_b += 1
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
            winsound.PlaySound("score.wav", winsound.SND_ASYNC)

        # Paddle collision
        if (540 < ball.xcor() < 550) and (paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
            ball.setx(540)
            ball.dx = -ball.dx  # Reverse x direction
            winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

        if (-540 > ball.xcor() > -550) and (paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50):
            ball.setx(-540)
            ball.dx = -ball.dx  # Reverse x direction
            winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

except turtle.Terminator:
    print("Game exited.")
