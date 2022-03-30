from configparser import ConfigParser

from src.board.board import Board
from src.game.service import Game
from src.ui.console import UI

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read(r"E:\fundamentals_of_programming\homework\e1-teodoraarsene\src\settings.properties")
    DIM = parser.getint("settings", "DIM")
    number_of_apples = parser.getint("settings", "number_of_apples")
    board = Board(DIM, number_of_apples)
    game = Game(board)
    ui = UI(game)
    ui.run()
