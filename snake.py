from turtle import Turtle

# ~~~~~~~~~~~~~~~~~~~~~~ Snake Constants ~~~~~~~~~~~~~~~~~~~~~~
MOVE_DISTANCE = 20

# Directional Angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# ~~~~~~~~~~~~~~~~~~~~~~ Snake Class ~~~~~~~~~~~~~~~~~~~~~~
class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        """A method that creates a new snake."""
        x = 0
        for _ in range(3):
            self.add_segment((_, 0))
            x -= 20

    def reset_snake(self):
        """A method that resets the snake to its original state."""
        for segment in self.snake_parts:
            segment.ht()
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def add_segment(self, position):
        """A method that adds a segment to the snake."""
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def extend(self):
        """A method that extends the snake."""
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        """A method that makes the snake move."""
        for seg_number in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg_number - 1].xcor()
            new_y = self.snake_parts[seg_number - 1].ycor()
            self.snake_parts[seg_number].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        """A method that moves the snake up if possible."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """A method that moves the snake down if possible."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """A method that moves the snake left if possible."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """A method that moves the snake right if possible."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_game_over(self):
        """A method that checks if its the end of the game."""
        return self.collided_with_tail() or self.collided_with_wall()

    def collided_with_wall(self):
        """A method that checks if the snake collided with the walls."""
        return self.head.xcor() > 290 or self.head.xcor() < -299 or self.head.ycor() > 299 or self.head.ycor() < -290

    def collided_with_tail(self):
        """A method that checks if the snake collided with its tail."""
        for snake_part in self.snake_parts[1:]:
            if self.head.distance(snake_part) < 10:
                return True
        return False

