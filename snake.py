import turtle
import random
import time

delay = 0.1
score = 0
highest_score = 0
bodies = []

# Screen setup
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)

# Head creation
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food creation
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Scoreboard creation
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | Highest Score: 0")


def moveup():
    """Moves the head up if not already moving down."""
    if head.direction != "down":
        head.direction = "up"


def movedown():
    """Moves the head down if not already moving up."""
    if head.direction != "up":
        head.direction = "down"


def moveleft():
    """Moves the head left if not already moving right."""
    if head.direction != "right":
        head.direction = "left"


def moveright():
    """Moves the head right if not already moving left."""
    if head.direction != "left":
        head.direction = "right"


def movestop():
    """Stops the snake movement."""
    head.direction = "stop"


def move():
    """Moves the head based on its direction, with edge bouncing."""
    if head.direction == "up":
        y = head.ycor()
        # Check for edge and bounce
        if y + 20 > 290:
            head.sety(-290)
        else:
            head.sety(y + 20)
    # Similar logic for other directions (down, left, right)
    elif head.direction == "down":
        y = head.ycor()
        if y - 20 < -290:
            head.sety(290)
        else:
            head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        if x - 20 < -290:
            head.setx(290)
        else:
            head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        if x + 20 > 290:
            head.setx(-290)
        else:
            head.setx(x + 20)


def game_over():
    """Handles game over actions (reset, display message)."""
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide and clear bodies
    for body in bodies:
        body.ht()
    bodies.clear()

    global score  # Access global score variable
    score = 0
    global delay  # Access global delay variable
    delay = 0.1

    # Update scoreboard
    sb.clear()
    sb.write(f"Score: {score} | Highest Score: {highest_score}")


def check_collision():
    """Checks for collision with the head and the body or edge."""
    # Check for edge collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        return True
    # Check for collision with body segments
    for body in bodies:
        if head.distance(body) < 20:
            return True
    return False


# Key bindings
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

while True:
    s.update()

    # Move the snake
    move()

    # Check for food collision and grow snake
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        score += 10
        delay -= 0.001

        # Update highest score
        if score > highest_score:
            highest_score = score

        # Update scoreboard
        sb.clear()
        sb.write(f"Score: {score} | Highest Score: {highest_score}")

    # Check for collision (body or edge) and handle game over
    if check_collision():
        game_over()

    # Move the body segments (optimized)
    if len(bodies) > 0:
        bodies[-1].goto(head.xcor(), head.ycor())
        for index in range(len(bodies) - 2, 0, -1):
            bodies[index].goto(bodies[index - 1].xcor(), bodies[index - 1].ycor())
        bodies[0].goto(head.xcor(), head.ycor())

    # Update game speed
    time.sleep(delay)

s.mainloop()
