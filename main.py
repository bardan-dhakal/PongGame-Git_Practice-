import turtle
import winsound
window = turtle.Screen()
window.title("My Game")
window.bgcolor("black")
window.setup(1200, 700, starty = 10)
window.tracer(0)

#Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(5,1)
paddle1.penup()
paddle1.setx(-550)

#Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(5,1)
paddle2.penup()
paddle2.setx(550)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.2
ball.dy = 0.2


#Scoring
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player A : 0  Player B : 0", align="center", font = ("Courier", 24, "bold"))



#Function to move the paddles
def paddle1_up():
    y = paddle1.ycor()
    if y < 305 :
        y += 20
        paddle1.sety(y)
    

def paddle1_down():
    y = paddle1.ycor()
    if y > -305 :
        y -=20
        paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    if y < 305 :
        y += 20
        paddle2.sety(y)
    

def paddle2_down():
    y = paddle2.ycor()
    if y > -305 :
        y -=20
        paddle2.sety(y)

#Keyboard-Screen Binding
window.listen()

window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")

window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")


#Main Loop
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#Boundary Check 
    
    if ball.ycor() > 340:
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -340:
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

    if ball.xcor() > 590:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font = ("Courier", 24, "bold"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    if ball.xcor() < -590:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font = ("Courier", 24, "bold"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

#Collision of the ball and paddle
    
    if  (ball.xcor() > 540 and ball.xcor() < 550)  and(ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40):
        ball.setx(540)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if  (ball.xcor() < -540 and ball.xcor() > -550)  and(ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40):
        ball.setx(-540)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
  

    
        

    
turtle.done()