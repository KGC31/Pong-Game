#Simple Pong game 
import turtle

window = turtle.Screen() # Window
window.title("Pong Game") #title
window.bgcolor("black") #Set background color
window.setup(height=600, width=800) #Set size of window

# Score
score_a = 0
score_b = 0

#Player 1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("white")
pad1.shapesize(stretch_len=1, stretch_wid=5)
pad1.penup()
pad1.goto(-350, 0)

#Player 2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("white")
pad2.shapesize(stretch_len=1, stretch_wid=5)
pad2.penup()
pad2.goto(350, 0)

#Middle line
line = turtle.Turtle()
line.shape("square")
line.color("red")
line.shapesize(stretch_wid=50, stretch_len=0.1)
line.penup()
line.goto(0,0)

#Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 7
ball.dy = -7

#Players Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Consolas", 24, "normal"))

#Key bindings for player1
def pad1_up():
    if pad1.ycor() < 250:
        y = pad1.ycor()
        y += 40
        pad1.sety(y)

def pad1_down():
    if pad1.ycor() > -250:
        y = pad1.ycor()
        y -= 40
        pad1.sety(y)

    
#Key bindings for player1
def pad2_up():
    if pad2.ycor() < 250:
        y = pad2.ycor()
        y += 40
        pad2.sety(y)

def pad2_down():
    if pad2.ycor() > -250:
        y = pad2.ycor()
        y -= 40
        pad2.sety(y)

#Key get for player 1
window.listen()
window.onkeypress(pad1_up, "w")
window.onkeypress(pad1_down, "s")
window.onkeypress(pad2_up, "Up")
window.onkeypress(pad2_down, "Down")


while True:
    window.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 380:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -380:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < pad1.ycor() + 50 and ball.ycor() >= pad1.ycor():
        ball.dx *= -1
        ball.dy = 7
    if ball.xcor() < -340 and ball.ycor() > pad1.ycor() - 50 and ball.ycor() <= pad1.ycor():
        ball.dx *= -1
        ball.dy = -7
    if ball.xcor() > 340 and ball.ycor() < pad2.ycor() + 50 and ball.ycor() >= pad2.ycor():
        ball.dx *= -1
        ball.dy = 7
    if ball.xcor() > 340 and ball.ycor() > pad2.ycor() - 50 and ball.ycor() <= pad2.ycor():
        ball.dx *= -1
        ball.dy = -7
