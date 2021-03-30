from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f'Score : {self.score}', align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 24, 'normal'))

    def print_score(self):
        self.score += 1
        self.clear()
        self.update_score()
