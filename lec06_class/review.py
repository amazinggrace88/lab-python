class Score:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math


    def calc_total(self):
        return self.korean + self.english + self.math


    def calc_average(self):
        return self.calc_total() / 3


score1 = Score(90, 90, 90)
score1.math = 100
print(score1.calc_total())
print(score1.calc_average())
print(Score.calc_average(score1))


# list

