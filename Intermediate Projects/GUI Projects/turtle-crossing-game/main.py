import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
counter = 0

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()
cars = car_manager.all_cars

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move car
    car_manager.create_new_car()
    car_manager.move_cars()

    # Check when turtle collides with car
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # check when turtle has reached top of the screen
    if player.ycor() > 280:
        player.reset()
        scoreboard.level_up()
        car_manager.increase_speed()

screen.exitonclick()
