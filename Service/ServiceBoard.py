import math
import random

from Errors.Errors import Endgame


class ServiceBoard:

    def __init__(self, board, board_validator):
        self.__board = board
        self.__board_validator = board_validator
        self.__pieces = {0: 'X', 1: 'O'}

    def get_board(self):
        return self.__board.get_board()

    def move_and_endgame_check(self, column, player, name):
        valid_columns = self.valid_columns()
        if len(valid_columns) == 0:
            raise Endgame("\nUff...It's a tie!\n")
        row = self.new_move(column, player)
        if self.get_winner() is not None:
            winner = self.get_winner()
            if winner.get_state() == player:
                raise Endgame("\n!!!{} wins!!!\n".format(name))
        return row

    def new_move(self, column, player):
        self.__board_validator.validate_column(column)
        row = self.__board.add_piece(column, player)
        return row

    def get_winner(self):
        winner = self.check_4_in_columns()
        if winner is None:
            winner = self.check_4_in_rows()
            if winner is None:
                winner = self.check_4_in_diagonals()
        return winner

    def check_4_in_columns(self):
        for column in range(1,8):
            rows = self.__board.get_board()[column]
            if rows[0].get_state() != '.':
                row = 0
                while row <= 2:
                    if rows[row].get_state() == '.':
                        break
                    if rows[row] == rows[row + 1] == rows[row + 2] == rows[row + 3]:
                        return rows[row]
                    row += 1
        return None

    def check_4_in_rows(self):
        board = self.get_board()
        for row in range(0,6):
            if board[4][row].get_state() != '.':
                column = 1
                while column <= 4:
                    if board[column][row] == board[column+1][row] == board[column+2][row] == board[column+3][row]:
                        return board[column][row]
                    column += 1
        return None

    def check_4_in_diagonals(self):
        board = self.get_board()
        for row in range(0, 3):
            for column in range(1, 5):
                if board[column][row].get_state() != '.':
                    if board[column][row] == board[column+1][row+1] == board[column+2][row+2] == board[column+3][row+3]:
                        return board[column][row]
            for column in range(4, 8):
                if board[column][row].get_state() != '.':
                    if board[column][row] == board[column-1][row+1] == board[column-2][row+2] == board[column-3][row+3]:
                        return board[column][row]
        return None

    def __str__(self):
        return str(self.__board)

    def clear_board(self):
        self.__board.clear_board()

    def your_move(self, column, player):
        self.__board_validator.validate_column(column)
        row = self.__board.add_piece(column, player)
        if self.get_winner() is not None:
            raise Endgame("\n!!!You win!!!\n")
        return row

    def computer_move(self, computer, player, difficulty):
        column, score = self.minimax(difficulty, True, -math.inf, math.inf, computer, player)
        self.__board_validator.validate_column(column)
        row = self.__board.add_piece(column, computer)
        if self.get_winner() is not None:
            raise Endgame("\n!!!Computer wins!!!\n")
        return row, column

    def valid_columns(self):
        valid_columns = []
        for column in range(1,8):
            positions = self.__board.get_board()[column]
            if positions[5].get_state() == '.':
                valid_columns.append(column)
        return valid_columns

    # def best_move_computer(self, computer, player)
        # valid_columns = self.valid_columns()
        # best_score = 0
        # best_column = random.choice(valid_columns)
        # for column in valid_columns:
        #     board_copy = self.__board.copy()
        #     board_copy.add_piece(column, computer)
        #     new_score = board_copy.score_check(computer, player)
        #     if new_score > best_score:
        #         best_score = new_score
        #         best_column = column
        # return best_column

    def minimax(self, depth,  maximizing_player, alfa, beta, computer, player):
        valid_columns = self.valid_columns()
        if (depth == 0) or (self.get_winner() is not None) or len(valid_columns) == 0:
            if depth == 0:
                return None, self.__board.score_check(computer, player)
            elif self.get_winner().get_state() == computer:
                return None, 1000000
            elif self.get_winner().get_state() == player:
                return None, -100000000
            elif len(valid_columns) == 0:
                return None, 0
        if maximizing_player: # computer
            best_score = -math.inf
            best_column = random.choice(valid_columns)
            for column in valid_columns:
                board_copy = self.__board.copy()
                board_service_copy = ServiceBoard(board_copy, self.__board_validator)
                board_service_copy.new_move(column, computer)
                new_column, new_score = ServiceBoard.minimax(board_service_copy, depth-1, False, alfa, beta, computer, player)
                if new_score > best_score:
                    best_score = new_score
                    best_column = column
                alfa = max(alfa, best_score)
                if alfa >= beta:
                    break
        else: # player
            best_score = math.inf
            best_column = random.choice(valid_columns)
            for column in valid_columns:
                board_copy = self.__board.copy()
                board_service_copy = ServiceBoard(board_copy, self.__board_validator)
                board_service_copy.new_move(column, player)
                new_column, new_score = ServiceBoard.minimax(board_service_copy, depth - 1, True, alfa, beta, computer, player)
                if new_score < best_score:
                    best_score = new_score
                    best_column = column
                beta = min(beta, best_score)
                if alfa >= beta:
                    break
        return best_column, best_score




























