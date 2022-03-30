from src.exceptions.exception import MovingException


class Game:
    def __init__(self, board):
        self.board = board

    def generate_initial_state(self):
        self.board.generate_snake()
        self.board.generate_apples()

    def display_board(self):
        return str(self.board)

    def move_up(self):
        if self.board.find_direction() == "down":
            raise MovingException("opposite direction")
        elif self.board.find_direction() == "up":
            return
        self.board.move("up")

    def move_down(self):
        if self.board.find_direction() == "up":
            raise MovingException("opposite direction")
        elif self.board.find_direction() == "down":
            return
        self.board.move("down")

    def move_right(self):
        if self.board.find_direction() == "left":
            raise MovingException("opposite direction")
        elif self.board.find_direction() == "right":
            return
        self.board.move("right")

    def move_left(self):
        if self.board.find_direction() == "right":
            raise MovingException("opposite direction")
        elif self.board.find_direction() == "left":
            return
        self.board.move("left")

    def move(self, steps):
        direction = self.board.find_direction()
        while steps:
            self.board.move(direction)
            steps = steps - 1

