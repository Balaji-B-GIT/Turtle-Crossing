import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
carmanager = CarManager()
score = Scoreboard()


screen.onkey(fun=player.move, key="Up")
i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move()
    for cars in carmanager.cars:
        if player.player.distance(cars) < 20:
            score.game_over()
            game_is_on = False

    if player.is_finish_line():
        score.increase_level()
        carmanager.increase_speed()
        time.sleep(0.5)
        player.origin()


screen.exitonclick()
