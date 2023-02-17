from cmath import sqrt
from random import randint

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_x = randint(1, difficulty)
        self.secret_y = randint(1, difficulty)
        self.max_guesses = difficulty + 5
        self.guesses = 0
        self.won = False

    def play(self):
        while self.guesses < self.max_guesses:
            x = self.get_integer_input("GUESS FOR X ")
            y = self.get_integer_input("GUESS FOR Y ")

            distance = self.get_distance(x, y)
            if distance == 0:
                print(f"YOU DESTROYED IT IN {self.guesses+1} goes")
                self.won = True
                break
            if distance <= 3:
                print("CLOSE")
            else:
                print("NOT EVEN CLOSE")
            self.guesses += 1
        if not self.won:
            print("THE ROBOTS HAVE SEEN\nYOU - AGGHHHHH.....")

    def get_integer_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def get_distance(self, x, y):
        return abs(sqrt((self.secret_x - x) ** 2 + (self.secret_y - y) ** 2))


if __name__ == '__main__':
    print("SECRET WEAPON")
    difficulty = 0
    while difficulty < 4:
        difficulty = int(input("ENTER DIFFICULTY "))

    game = Game(difficulty)
    game.play()
