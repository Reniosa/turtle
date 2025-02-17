# افزودن کتابخانه‌ها
import turtle
import time
import random

# تنظیمات اولیه
WIDTH, HEIGHT = 600, 600
DELAY = 0.09

# امتیاز
score = 0
high_score = 0

# رنگ‌های تکرار شونده 
c1 = ["PaleTurquoise4", "DarkSeaGreen4", "DarkSeaGreen3", "LightSteelBlue", "LightCyan3", "LightSteelBlue4"]

# تنظیمات صفحه
rina = turtle.Screen()
rina.title("Snake Game")
rina.bgcolor("black")
rina.setup(width=WIDTH, height=HEIGHT)
rina.tracer(0)

# مار
snake = []
for i in range(3):
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape("square")
    segment.color(c1[i % len(c1)])
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

# غذا
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("MediumPurple4")
food.penup()
food.goto(0, 100)

# متن امتیاز
pen = turtle.Turtle()
pen.speed(0)
pen.color("SlateGray3")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Snacks: 0  UltimateSnake: 0", align="center", font=("Regular", 24, "normal"))

# حرکت مار
direction = "stop"

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

def move():
    if direction == "up":
        y = snake[0].ycor()
        snake[0].sety(y + 20)
    if direction == "down":
        y = snake[0].ycor()
        snake[0].sety(y - 20)
    if direction == "left":
        x = snake[0].xcor()
        snake[0].setx(x - 20)
    if direction == "right":
        x = snake[0].xcor()
        snake[0].setx(x + 20)

# کنترل صفحه کلید
rina.listen()
rina.onkey(go_up, "w")
rina.onkey(go_down, "s")
rina.onkey(go_left, "a")
rina.onkey(go_right, "d")

# حلقه اصلی بازی
while True:
    rina.update()

    # بررسی برخورد با دیوار
    if (snake[0].xcor() > WIDTH//2 - 10 or snake[0].xcor() < -WIDTH//2 + 10 or
            snake[0].ycor() > HEIGHT//2 - 10 or snake[0].ycor() < -HEIGHT//2 + 10):
        time.sleep(1)
        for segment in snake:
            segment.goto(1000, 1000)
        snake.clear()
        score = 0
        direction = "stop"

        for i in range(3):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("square")
            segment.color(c1[i % len(c1)])
            segment.penup()
            segment.goto(-20 * i, 0)
            snake.append(segment)

    # بررسی برخورد با غذا
    if snake[0].distance(food) < 20:
        x = random.randint(-WIDTH//2 + 20, WIDTH//2 - 20)
        y = random.randint(-HEIGHT//2 + 20, HEIGHT//2 - 20)
        food.goto(x, y)

        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color(c1[len(snake) % len(c1)])
        segment.penup()
        snake.append(segment)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Snacks: {score}  Ultimate Snake: {high_score}", align="center", font=("Courier", 24, "normal"))

    # حرکت بدن مار
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    move()

    # بررسی برخورد با بدن خود
    for segment in snake[1:]:
        if snake[0].distance(segment) < 20:
            time.sleep(1)
            for segment in snake:
                segment.goto(1000, 1000)
            snake.clear()
            score = 0
            direction = "stop"

            for i in range(3):
                segment = turtle.Turtle()
                segment.speed(0)
                segment.shape("square")
                segment.color(c1[i % len(c1)])
                segment.penup()
                segment.goto(-20 * i, 0)
                snake.append(segment)

    time.sleep(DELAY)
