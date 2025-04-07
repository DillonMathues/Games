import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

scorea = 0
scoreb = 0

#paddles
pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid=5, stretch_len=1)
pa.penup()
pa.goto(-350, 0)
pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid=5, stretch_len=1)
pb.penup()
pb.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .07
ball.dy = .07

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"player 1: {scorea} Player 2: {scoreb}", align="center",font=("Courier", 24, "normal"))




def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)
def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)
def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)
def pb_down():
    y = pb.ycor()
    y -= 20
    pb.sety(y)


wn.listen()
wn.onkeypress(pa_up,"w")
wn.onkeypress(pa_down,"s")
wn.onkeypress(pb_up,"Up")
wn.onkeypress(pb_down,"Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        scorea += 1
        pen.clear()
        pen.write(f"player 1: {scorea} Player 2: {scoreb}", align="center",font=("Courier", 24, "normal"))
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreb += 1
        pen.clear()
        pen.write(f"player 1: {scorea} Player 2: {scoreb}", align="center",font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1