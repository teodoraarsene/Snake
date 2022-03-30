from src.exceptions.exception import InputException, MovingException, GameOver


class UI:
    def __init__(self, game,):
        self.game = game
        self.commands = {"move": self.ui_move, "up": self.ui_up, "down": self.ui_down, "right": self.ui_right, "left": self.ui_left}

    def ui_move(self, parameter):
        if not parameter:
            steps = 1
        else:
            steps = parameter
        self.game.move(steps)

    def ui_up(self, parameter):
        if parameter:
            raise InputException("invalid param count")
        self.game.move_up()

    def ui_down(self, parameter):
        if parameter:
            raise InputException("invalid param count")
        self.game.move_down()

    def ui_right(self, parameter):
        if parameter:
            raise InputException("invalid param count")
        self.game.move_right()

    def ui_left(self, parameter):
        if parameter:
            raise InputException("invalid param count")
        self.game.move_left()

    def parse_command(self, raw_command):
        words = raw_command.split()
        if len(words) == 1:
            return words[0].strip(), None
        elif len(words) == 2:
            squares_to_be_moved = int(words[1])
            return words[0], squares_to_be_moved
        raise InputException("invalid param count")

    def run(self):
        self.game.generate_initial_state()
        while True:
            try:
                print(self.game.display_board())
                raw_command = (input(">>")).strip()
                command_word, command_parameter = self.parse_command(raw_command)
                if command_word in self.commands:
                    self.commands[command_word](command_parameter)
                else:
                    print("invalid command")
            except (InputException, ValueError, MovingException) as exc:
                print(exc)
            except GameOver as go:
                print(go)
                break




