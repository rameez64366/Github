import random
from turtle import Turtle,Screen
import time
screen=Screen()

screen.setup(width=800,height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)

LEFT_PADDLE_POSITION=(-370,0)
RIGHT_PADDLE_POSITION=(370,0)

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor()<260:
            new_y=self.ycor()+20
            self.goto(self.xcor(),new_y)

    def down(self):
        if self.ycor()>-250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.8,stretch_len=0.8)
        self.penup()
        self.xmove=3
        self.ymove=3
        self.move_speed=0.1


    def move_ball(self):
        new_x=self.xcor() + self.xmove
        new_y=self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.xmove*=-1
        self.move_speed*=0.9

    def bounce_y(self):
        self.ymove*=-1

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.right_score=0
        self.left_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,270)
        self.write(f"{self.left_score}", align="center", font=('Arial', 15, 'normal'))
        self.goto(100,270)
        self.write(f"{self.right_score}", align="center", font=('Arial', 15, 'normal'))

    def left_point(self):
        self.left_score+=1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()




right_paddle=Paddle(RIGHT_PADDLE_POSITION)
left_paddle=Paddle(LEFT_PADDLE_POSITION)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()

screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

is_game=True
while is_game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        scoreboard.left_point()
        ball.reset_ball()

    if ball.ycor()<-380:
        scoreboard.right_point()
        ball.reset_ball()

screen.exitonclick()
