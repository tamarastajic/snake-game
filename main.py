from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


# ~~~~~~~~~~~~~~~~~~~~~~ Necessary Functions ~~~~~~~~~~~~~~~~~~~~~~

def create_screen():
    """A function that creates and returns a screen."""
    created_screen = Screen()
    created_screen.setup(height=600, width=600)
    created_screen.bgcolor("black")
    created_screen.title("Snake Game")
    created_screen.update()
    created_screen.tracer(0)
    return created_screen


def listen_to_keys():
    """A function that listens to movement keys."""
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)


# ~~~~~~~~~~~~~~~~~~~~~~ Creating Necessary Objects ~~~~~~~~~~~~~~~~~~~~~~
snake = Snake()
screen = create_screen()
food = Food()
score = Score()

# ~~~~~~~~~~~~~~~~~~~~~~ Game Loop ~~~~~~~~~~~~~~~~~~~~~~
game_is_on = True
while game_is_on:
    score.write_score()
    screen.update()

    time.sleep(0.1)

    snake.move()
    listen_to_keys()

    # Detect collision with food.
    if snake.head.distance(food) < 16:
        score.score += 1
        score.write_score()
        snake.extend()
        food.move()

    # Check if lost
    if snake.is_game_over():
        snake.reset_snake()
        food.move()
        score.reset_score()
        screen.update()
        time.sleep(0.1)

screen.exitonclick()
