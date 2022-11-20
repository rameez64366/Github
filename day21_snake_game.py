from turtle import Turtle,Screen
import random
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
POSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.body=[]
        self.create_snake()
        self.snake_head = self.body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_body_part(position)

    def add_body_part(self,position):
        body_part=Turtle()
        body_part.shape("square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.body.append(body_part)

    def rese(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.body=[]
        self.create_snake()
        self.snake_head = self.body[0]

    def move(self):
        for part in range(len(self.body)-1,0,-1):
            self.body[part].goto(self.body[part-1].xcor(),self.body[part-1].ycor())
            self.body[part].setheading(self.body[part-1].heading())
        self.snake_head.forward(20)

    def extend_body(self):
        self.add_body_part(self.body[-1].position())

    def Up(self):
        if self.snake_head.heading()!=270:
            self.snake_head.setheading(90)

    def Down(self):
        if self.snake_head.heading()!=90:
            self.snake_head.setheading(270)

    def Right(self):
        if self.snake_head.heading()!=180:
            self.snake_head.setheading(0)

    def Left(self):
        if self.snake_head.heading()!=0:
            self.snake_head.setheading(180)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.score=0
        with open("day21_snake_game_highscore.txt") as data:
            self.highscore=int(data.read())
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}, highscore:{self.highscore}", align="center", font=('Arial', 15, 'normal'))

    def add_score(self):
        self.score+=1
        self.update_score()

    def rese(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("day21_snake_game_highscore.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()


    # def hit_wall(self):
    #     self.home()
    #     self.write("Game Over!", align="center", font=('Arial', 15, 'normal'))


snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.tracer(0)
screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Right,"Right")
screen.onkey(snake.Left,"Left")
is_game=True
while is_game:
    screen.update()
    time.sleep(0.1)
    if snake.snake_head.xcor()<280 and snake.snake_head.xcor()>-280 and snake.snake_head.ycor()>-280 and snake.snake_head.ycor()<280:
        snake.move()
        if snake.snake_head.distance(food)<15:
            scoreboard.add_score()
            food.refresh()
            snake.extend_body()
        # for parts in snake.body:
        #     if parts==snake.snake_head:
        #         pass
        #     elif snake.snake_head.distance(parts)<10:
        #         scoreboard.hit_wall()
        #         is_game=False
        for parts in snake.body[1:]:
           if snake.snake_head.distance(parts)<10:
               snake.rese()
               scoreboard.rese()
    else:
        snake.rese()
        scoreboard.rese()

screen.exitonclick()