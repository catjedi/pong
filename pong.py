import turtle

# Creating a game window to be able to play
game_Window = turtle.Screen()
game_Window.title("Pong")
game_Window.bgcolor("black")
game_Window.setup(width=800, height=600)

# Stops the window from updating in order
# for the game to run at a faster rate
game_Window.tracer(0)

# Score
score_A = 0
score_B = 0

# Paddle A
paddle_A = turtle.Turtle()  # making game/paddle object
paddle_A.speed(0)  # speed of animation
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()  # turtle objects draw lines when they move - this method makes the object to not draw lines
paddle_A.goto(-350, 0)  # starting point of the paddle

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.14  # speed of ball moving horizontally
ball.dy = 0.14  # speed of ball moving vertically

# Pen
# A scoreboard is made for the game
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center",
          font=("Courier", 24, "normal"))


def paddle_A_up():
    y = paddle_A.ycor()  # returns y-coordinate
    y += 20  # paddle moves up
    paddle_A.sety(y)  # sets the new y-coordinate


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20  # paddle moves down
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# Keyboard binding
# When pressing a key (game object moves), it calls a function in order to
# reassign the x and y coordinates of the objects
game_Window.listen()
game_Window.onkeypress(paddle_A_up, "w")
game_Window.onkeypress(paddle_A_down, "s")
game_Window.onkeypress(paddle_B_up, "Up")
game_Window.onkeypress(paddle_B_down, "Down")
# Main game loop
while True:
    game_Window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # If the ball makes contact with the top or bottom border,
    # it will bounce from the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # If the ball makes contact with the left or right border,
    # it will reset its position at the center (0, 0)
    if ball.xcor() > 390:
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B),
                  align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -390:
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B),
                  align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions / ball bounces off of paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
