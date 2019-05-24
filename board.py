from itertools import cycle
import random


class Board:
    USER = "O"
    COMPUTER = "X"
    CURRENT = cycle(["O", "X"])

    def __init__(self):
        self.field = self.generate_field()
        # self.last_position = None
        self.winner = None
        self.last_user = None
        self.last_bot = None

    #
    # def choose_figure(self):
    #     figures = ["x", "o"]
    #     user_choice = input("choose your figure: ")
    #     computer = [i for i in figures if i != user_choice][0]
    #     return computer

    def generate_field(self):
        f = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
        return f

    def get_user_position(self):
        x = int(input("Enter value for row "))
        y = int(input("Enter value for column "))
        self.field[x][y] = self.USER

    def get_bot_position(self):
        return

    def print_field(self):
        for i in self.field:
            print(i)

    def who_wins(self):
        if (self.field[0][0] and self.field[1][0] and self.field[2][
            0] == "O") or (self.field[0][1] and self.field[1][1] and
                           self.field[2][
                               1] == "O") or (
                self.field[0][2] and self.field[1][2] and
                self.field[2][2] == "O"):
            self.winner = self.USER

        elif ["O", "O", "O"] in self.field:
            self.winner = self.USER
        elif (self.field[0][0] and self.field[1][1] and self.field[2][
            2] == "O") or (self.field[2][2] and self.field[1][1] and
                           self.field[0][2] == "O"):
            self.winner = self.USER

        elif (self.field[0][0] and self.field[1][0] and self.field[2][
            0] == "X") or (self.field[0][1] and self.field[1][1] and
                           self.field[2][
                               1] == "X") or (
                self.field[0][2] and self.field[1][2] and
                self.field[2][2] == "X"):
            self.winner = self.COMPUTER

        elif ["X", "X", "X"] in self.field:
            self.winner = self.COMPUTER
        elif (self.field[0][0] and self.field[1][1] and self.field[2][
            2] == "X") or (self.field[2][2] and self.field[1][1] and
                           self.field[0][2] == "X"):
            self.winner = self.COMPUTER
        else:
            self.winner = None
        return self.winner

    def put_figure(self):
        while True:
            if self.CURRENT.__next__() == 'O':
                self.get_user_position()
            elif self.CURRENT.__next__() == "X":
                self.get_bot_position()




b = Board()
b.field = [['O', 'X', 'O'],
             ['_', 'X', '_'],
             ['_', 'X', '_']]
print(b.who_wins())
# b.choose_figure()
# field = (b.generate_field())
# for i in field:
#     print(i)
#
# b.put_figure()

# b.get_user_position()
# b.print_field()
