import time
import random
from turtle import Turtle,Screen
STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_Y=280

COLORS=["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        if self.ycor()<FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def origin(self):
        self.goto(STARTING_POSITION)


class Cars_manager:
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed+=MOVE_INCREMENT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=0
        self.goto(-280,250)
        with open("day23_turtle_high_score.txt") as high_score:
           self.score=int(high_score.read())
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level},highscore:{self.score}", align="left", font= ("Courier", 18, "normal"))

    def add_level(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="left", font=("Courier", 18, "normal"))

    def new_game(self):
        if self.level>self.score:
            self.score=self.level
            with open("day23_turtle_high_score.txt",mode="w") as high_score:
                high_score.write(f"{self.score}")


screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)

cars=Cars_manager()
player=Player()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.move_up,"Up")

is_game=True

while is_game:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            scoreboard.new_game()
            is_game=False

    if player.ycor()==FINISH_LINE_Y:
        scoreboard.add_level()
        cars.speed_increase()
        player.origin()


screen.exitonclick()





























