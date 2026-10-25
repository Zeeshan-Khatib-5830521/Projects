from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0

        with open('score_tracker.txt') as file:
            self.highscore =int(file.read())


    def display(self):
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.write(f'Score: {self.score}     High Score {self.highscore}', align='center', font= ('Arial',24,'normal'))
        self.color('white')

        self.hideturtle()

    def if_food_hit(self):

        self.score += 1
        self.display()


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('score_tracker.txt', mode='w') as file:
                file.write(f'{self.highscore}')


        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color('white')
    #     self.write('GAME OVER', align = 'center', font = ('Arial', 50, 'normal'))















