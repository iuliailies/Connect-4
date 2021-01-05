import unittest

from Errors.Errors import RepoError
from Repo.Board import Board


class TestBoard(unittest.TestCase):

    def test_board(self):
        board = Board()
        for column in range (1,8):
            for row in range(0,6):
                self.assertEqual(board.get_board()[column][row].get_state(), '.')
        board.add_piece(3, 'X')
        self.assertEqual(str(board.get_board()[3][0]), 'X')
        for row in range (1,6):
            board.add_piece(3, 'X')
        self.assertRaises(RepoError, board.add_piece, 3, 'X')
        copy_board = board.copy()
        for column in range(1, 8):
            for row in range(0, 6):
                self.assertEqual(board.get_board()[column][row].get_state(), copy_board.get_board()[column][row].get_state())
        copy_board.add_piece(4, 'O')
        self.assertEqual(board.get_board()[4][0].get_state(), '.')
        board.clear_board()
        for column in range (1,8):
            for row in range(0,6):
                self.assertEqual(board.get_board()[column][row].get_state(), '.')

        board.add_piece(3, 'X')
        board.add_piece(1, 'O')
        board.add_piece(3, 'X')
        board.add_piece(2, 'O')
        board.add_piece(4, 'X')
        board.add_piece(2, 'O')
        board.add_piece(5, 'X')
        '''
        .  .  .  .  .  .  .
        .  .  .  .  .  .  .
        .  .  .  .  .  .  .
        .  .  .  .  .  .  .
        .  O  X  .  .  .  .
        O  O  X  X  .  X  .
        1  2  3  4  5  6  7
        '''
        self.assertEqual(board.score_check('X', 'O'), 12)


