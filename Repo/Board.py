import termcolor
import copy

from Domain.Patratica import Patratica
from Errors.Errors import RepoError

class Board:

    def __init__(self, board = None):
        if board is None:
            self.__board = self.create_board()
        else:
            self.__board = board

    @staticmethod
    def create_board():
        board = {}
        for column in range(1,8): #7 columns
            rows = [] # 6 rows => 6 elements in a column
            for row in range(0,6):
                rows.append(Patratica())
            board[column] = rows
        return board

    def add_piece(self, column, player):
        '''
        Function that adds a piece to the board.
        :param column: the column that the player chose - int from interval [0,7]
        :param player: x or o
        '''
        positions = self.__board[column]
        if positions[5].get_state() != '.':
            raise RepoError('\nThat column is full! Try again:\n')
        for position in range(len(positions)):
            if positions[position].get_state() == '.':
                positions[position].set_state(player)
                return position

    def __str__(self):
        board = ''
        for row in range (5, -1, -1):
            for column in range (1,8):
                if str(self.__board[column][row]) == 'X':
                    board = board + termcolor.colored((str(self.__board[column][row])).upper(), 'red') + '  '
                elif str(self.__board[column][row]) == 'O':
                    board = board + termcolor.colored(str(self.__board[column][row]).upper(), 'yellow') + '  '
                else:
                    board = board + str(self.__board[column][row]) + '  '
            board = board + '\n' + '\n'
        for column in range(1,8):
            board = board + str(column) + '  '
        return board

    def clear_board(self):
        for row in range (5, -1, -1):
            for column in range (1,8):
                self.__board[column][row].set_state('.')

    def copy(self):
        board_dict = copy.deepcopy(self.__board)
        board_copy = Board(board_dict)
        return board_copy

    def get_board(self):
        return self.__board

    def score_check(self, computer, player):
        '''
        This function provides a scoring mechanism for the AI. It analyses the state of a board after a new move
        was made The higher the score of a possible move, the better that move is.
        The computer will choose the move based on the highest score.
        Scoring mechanism:
        - 4 in a row : 100 points
        - 3 in a group of 4: 50 points
        - 2 in a group of 4: 5 points
        - center column(good for the beginning): 4 points

        - letting the player make a line of 2: -2 points
        - letting the player make a line of 3: -25 points
        - letting the player make a line of 4: -50 points
        :param computer: X or O
        :param player: opposite of computer
        '''
        score = 0

        # row check for points
        for row in range(0,6):
            for column in range(1,5):
                row_elements = []
                for i in range(0,4):
                    row_elements.append(self.__board[column + i][row].get_state()) # . , X or O
                score += self.score_count(row_elements, computer, player)

        # column check for points
        for column in range(1,8):
            for row in range(0,3):
                column_elements = []
                for i in range(0,4):
                    column_elements.append(self.__board[column][row+i].get_state())
                score += self.score_count(column_elements, computer, player)

        # diagonal check for points
        for row in range(0, 3):
            for column in range(1, 5):
                diagonal_elements = []
                for i in range (0,4):
                    diagonal_elements.append(self.__board[column+i][row+i].get_state())
                score += self.score_count(diagonal_elements, computer, player)
            for column in range(4, 8):
                diagonal_elements = []
                for i in range(0, 4):
                    diagonal_elements.append(self.__board[column - i][row + i].get_state())
                score += self.score_count(diagonal_elements, computer, player)

        # preference center
        # center_elements = []
        # for row in range(0,6):
        #     center_elements.append(self.__board[4][row].get_state())
        # center_count = center_elements.count(computer)
        # score = center_count * 4

        return score

    @staticmethod
    def score_count(direction_elements, computer, player):
        score = 0
        if direction_elements.count(computer) == 3 and direction_elements.count('.') == 1:
            score += 10
        elif direction_elements.count(computer) == 2 and direction_elements.count('.') == 2:
            score += 2

        elif direction_elements.count(player) == 3 and direction_elements.count('.') == 1:
            score -= 10
        elif direction_elements.count(player) == 2 and direction_elements.count('.') == 2:
            score -= 1

        return score








