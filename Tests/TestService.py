import unittest

from Errors.Errors import Endgame, ValidationError
from Repo.Board import Board
from Service.ServiceBoard import ServiceBoard
from Validators.Validators import Validators


class TestService(unittest.TestCase):

    def setUp(self):
        self.__board = Board()
        self.__validator = Validators()
        self.__service_board = ServiceBoard(self.__board, self.__validator)
        self.__service_board.new_move(6, 'X')
        self.__service_board.new_move(3, 'O')
        self.__service_board.new_move(6, 'X')
        self.__service_board.new_move(3, 'O')
        self.__service_board.new_move(6, 'X')

    def test_service(self):
        self.assertRaises(ValidationError, self.__service_board.new_move, 8, 'O')
        self.__service_board.new_move(1, 'O')
        self.assertEqual(self.__service_board.get_winner(), None)
        self.__service_board.new_move(6, 'X')
        self.assertRaises(Endgame, self.__service_board.move_and_endgame_check, 6, 'X')
        self.__service_board.clear_board()
        for column in range(1, 8):
            for row in range(0, 6):
                self.assertEqual(self.__service_board.get_board()[column][row].get_state(), '.')

    def test_minimax(self):
        '''
        .  .  .  .  .  .  .
        .  .  .  .  .  .  .
        .  .  .  .  .  .  .
        .  .  .  .  .  X  .
        .  .  O  .  .  X  .
        .  .  O  .  .  X  .
        1  2  3  4  5  6  7

        Computer(O) should try to block the opponent.

        .  .  .  .  .  .  .
        .  .  .  .  .  .  .
        .  .  .  .  .  O  .
        .  .  O  .  .  X  .
        X  .  O  .  .  X  .
        X  .  O  .  .  X  .
        1  2  3  4  5  6  7

        Computer should put the winning piece in column 3 instead of blocking opponent.
        '''
        player = 'X'
        computer = 'O'
        self.__service_board.computer_move(computer, player, 2)
        self.assertEqual(self.__service_board.get_board()[6][3].get_state(), computer)
        self.__service_board.your_move(1, player)
        self.__service_board.new_move(3, computer)
        self.__service_board.your_move(1, player)
        self.assertRaises(Endgame, self.__service_board.computer_move, computer, player, 2)




