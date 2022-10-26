from turtle import Turtle
import csv


ALIGNMENT = 'center'
FONT = ('ArcadeClassic', 28, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 308)
        self.current_score = 0
        self.name_tag = ""
        self.high_score = 0
        self.leader_board = []
        self.high_score_reader()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.current_score}     '
                   f'High-score: {self.leader_board[0]["name"]} '
                   f'({self.leader_board[0]["score"]})',
                   align=ALIGNMENT, font=FONT)

    def increase(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.update_scoreboard()

    def high_score_writer(self, name):
        """Update leader_board list if someone got a record"""
        self.leader_board.append({"name": name, "score": self.current_score})

    def high_score_reader(self):
        """
        1. Read csv
        2. Fills the list with all records
        3. Gets highest score in file.
        """
        # Open file
        with open('high_score.csv', 'r') as f:
            # Output: {"name": name, "score": score}
            data = csv.DictReader(f)
            # placeholder for highest value
            temp_score = 0
            temp_name = ""
            # Parse all file for highest score
            for row in data:
                self.leader_board.append(row)
                if int(row["score"]) > temp_score:
                    temp_score = int(row["score"])
                    temp_name = row["name"]

            # Updates game right-top with highest score
            self.high_score = temp_score
            self.name_tag = temp_name

    def high_score_sorter(self):
        """ 1. Sort leader_board with bubble_sort reversed
            2. Rewriting csv with ordered values """
        n = len(self.leader_board)
        # Bubble sort algorithm
        for i in range(n-1):
            for j in range(n-i-1):
                one = self.leader_board[j]
                two = self.leader_board[j+1]
                if int(one["score"]) < int(two["score"]):
                    self.leader_board[j] = two
                    self.leader_board[j+1] = one

        # Replacing old csv with sorted list
        with open("high_score.csv", "w") as f:
            fieldnames = ['name', 'score']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(10):
                writer.writerow(self.leader_board[i])


class Leaderboard(Turtle):
    """ Leaderboard print module """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.game_terminated = False

    def reader(self):
        """ lb visualizator """
        counter = 0
        x, y = 0, 230
        self.goto(x, y)
        y -= 50
        self.write("Rank. name: score", align=ALIGNMENT, font=FONT)
        with open('high_score.csv', "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                if counter < 10:
                    counter += 1
                    self.goto(x, y)
                    y -= 50
                    self.write(f"{counter}. {row[0]}: {row[1]}",
                               align=ALIGNMENT,
                               font=FONT)
