import random

from texttable import Texttable

from src.exceptions.exception import MovingException, GameOver


class Board:
    def __init__(self, DIM, apple_count):
        self.DIM = DIM
        self.apple_count = apple_count
        self.matrix = [[" " for j in range(DIM)] for j in range(DIM)]
        self.snake = []
        self.free_fields = []
        for i in range(self.DIM):
            for j in range(self.DIM):
                self.free_fields.append([i, j])

    def __str__(self):
        table = Texttable()
        for i in range(self.DIM):
            row = []
            for j in range(self.DIM):
                row.append(self.matrix[i][j])
            table.add_row(row)
        return table.draw()

    def generate_snake(self):
        middle = self.DIM // 2
        self.matrix[middle-1][middle] = "*"
        self.matrix[middle][middle] = "+"
        self.matrix[middle+1][middle] = "+"
        self.snake.append([middle-1, middle])
        self.snake.append([middle, middle])
        self.snake.append([middle+1, middle])
        self.free_fields.remove([middle-1, middle])
        self.free_fields.remove([middle, middle])
        self.free_fields.remove([middle+1, middle])

    def find_direction(self):
        if self.snake[0][0] == self.snake[1][0] - 1:
            return "up"
        if self.snake[0][0] == self.snake[1][0] + 1:
            return "down"
        if self.snake[0][1] == self.snake[1][1] + 1:
            return "right"
        if self.snake[0][1] == self.snake[1][1] - 1:
            return "left"

    def generate_apple(self):

        while True:
            apple = random.choice(self.free_fields)
            apple_row = apple[0]
            apple_column = apple[1]
            # apple_row = randint(0, self.DIM)
            # apple_column = randint(0, self.DIM)
            # total_fields = self.DIM ** 2
            # snake_fields = len(self.snake)
            # already_placed_apples = self.apple_count
            # free_fields = total_fields-snake_fields-already_placed_apples

            try:
                if not self.matrix[apple_row][apple_column] == " " or self.matrix[apple_row-1][apple_column] == "." or self.matrix[apple_row+1][apple_column] == "." or self.matrix[apple_row][apple_column-1] == "." or self.matrix[apple_row][apple_column+1] == ".":
                    continue
                else:
                    self.matrix[apple_row][apple_column] = "."
                    self.free_fields.remove(apple)

                    if apple_row - 1 >= 0 and [apple_row-1, apple_column] in self.free_fields:
                        self.free_fields.remove([apple_row-1, apple_column])
                    if apple_row + 1 <= self.DIM - 1 and [apple_row+1, apple_column] in self.free_fields:
                        self.free_fields.remove([apple_row+1, apple_column])
                    if apple_column - 1 >= 0 and [apple_row, apple_column-1] in self.free_fields:
                        self.free_fields.remove([apple_row, apple_column-1])
                    if apple_column + 1 <= self.DIM - 1 and [apple_row, apple_column+1] in self.free_fields:
                        self.free_fields.remove([apple_row, apple_column+1])
                    break
            except IndexError as ie:
                continue

    def generate_apples(self):
        apples = self.apple_count
        while apples:
            self.generate_apple()
            apples = apples - 1

    def move(self, direction):
        snake_head = self.snake[0]
        if direction == "up":
            new_head = [snake_head[0]-1, snake_head[1]]

        elif direction == "down":
            new_head = [snake_head[0]+1, snake_head[1]]

        elif direction == "right":
            new_head = [snake_head[0], snake_head[1]+1]

        elif direction == "left":
            new_head = [snake_head[0], snake_head[1]-1]

        if not (0 <= new_head[0] <= self.DIM-1 and 0 <= new_head[1] <= self.DIM-1):
            raise GameOver("you lost")

        if self.matrix[new_head[0]][new_head[1]] == "+":
            raise GameOver("you lost")

        if self.matrix[new_head[0]][new_head[1]] == ".":
            self.generate_apple()
        else:
            last_piece = self.snake.pop()
            self.matrix[last_piece[0]][last_piece[1]] = " "

        self.snake.insert(0, new_head)
        self.matrix[new_head[0]][new_head[1]] = "*"
        self.matrix[snake_head[0]][snake_head[1]] = "+"
