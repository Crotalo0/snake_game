"""Snake game."""
import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score, Leaderboard

# CHANGELOG:
#   - 3-10-22 Updated txt with csv and fixed scoreboard
#       Now score is saved consistently and updated if in top10

screen = Screen()
screen.setup(760, 760)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(1/10)
food = Food()
score_test = Score()
leaderboard = Leaderboard()

# Border turtles, used to check boundaries
y = Turtle(shape="circle")
y.color("white")
y.hideturtle()
y.penup()
y.goto(-310, 310)
y.pendown()
y.goto(310, 310)
y.goto(310, -310)
y.goto(-310, -310)
y.goto(-310, 310)
# ------------------------------------------------

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.right, "d")


def game():
    """Main game loop."""
    answer = ''
    ans_set = {"e", "l", "q"}
    run = True
    while run:
        screen.update()
        time.sleep(snake.sleep_timer)
        snake.move()

        # Detect food collision
        if snake.segments[0].distance(food) < 20:
            for seg in snake.segments:
                while food.distance(seg.pos()) < 20:
                    food.refresh()
            snake.extend()
            score_test.increase()

        if snake.border_crossed() or snake.tail_collision():
            for value in score_test.leader_board:
                score = int(value["score"])
                if score_test.current_score > score:
                    name = screen.textinput("High score!", "Your name: ")
                    score_test.high_score_writer(name)
                    break

            while answer not in ans_set:
                answer = screen.textinput("You lost!", '-e to start new game\n'
                                          '-l to watch leaderboard\n'
                                          '-q to quit')
                if answer == 'e':
                    leaderboard.clear()
                    snake.reset()
                    score_test.reset()
                    screen.listen()
                    game()
                elif answer == 'l':
                    leaderboard.clear()
                    score_test.high_score_sorter()
                    leaderboard.reader()
                    answer = ""
                elif answer == "q":
                    screen.bye()


game()
screen.mainloop()
