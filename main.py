import random
import turtle

screen = turtle.Screen()
turtle.bgcolor("yellow")
turtle.title("Catch The Turtle")
# font neden büyük yazdık yazılım jargonunda yani bu proje bitene kadar bu şekilde kalıcı olarak yazcak .
FONT = ('Arial', 30, 'normal')
scor = 0
game_over = False

# 1. ADIM YAZI YAZMAYI ÇÖZDÜK.
turtle_list = []
# countdownTurtle
countdown_turtle = turtle.Turtle()

# score turtle
score_turtle = turtle.Turtle()
score = 0


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0, y)
    score_turtle.write(arg="SCORE : 0", move=False, align="center", font=FONT)


grid_size = 15


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score : {}".format(score), move=False, align="center", font=FONT)
        print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark blue")
    t.setposition(x * grid_size, y * grid_size)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10, ]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):

    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0, y -40)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time -1),1000)
    else :
        game_over= True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="GAME OVER !!! ", move=False, align="center", font=FONT)


turtle.tracer(0)

setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)

turtle.mainloop()
