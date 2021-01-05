from Errors.Errors import ValidationError, RepoError, Endgame
from Validators.Validators import Validators


class UI:

    def __init__(self, board_service):
        self.__board_service = board_service
        self.__names = {}
        self.__pieces = {0: 'X', 1:'O'}

    def run_game(self):
        print('\nWelcome to CONNECT 4!\n')
        while True:
            print('Start a game:\n\n'
                  '1: Another player\n'
                  '2: Computer\n'
                  '3: Exit\n')
            option = input("Add your choice: ")
            if not option.isnumeric():
                raise Exception('Invalid option!')
            option = int(option)
            if option == 3:
                print('\nSee you next time! :)')
                break
            elif option == 1:
                self.run_game_player()
            elif option == 2:
                self.run_game_computer()
            else:
                raise Exception('Option not in the list!')
            self.__board_service.clear_board()

    def run_game_player(self):
        self.__names[0], self.__names[1] = self.add_names()
        move_number = 0
        while True:
            print('\n' + str(self.__board_service) + '\n')
            option = input("{}'s turn: ".format(self.__names[move_number % 2]))
            try:
                Validators.validate_option(option)
                option = int(option)
                self.__board_service.move_and_endgame_check(option, self.__pieces[move_number % 2], self.__names[move_number % 2])
                move_number += 1
            except ValidationError as ex:
                print(str(ex))
            except RepoError as ex:
                print(str(ex))
            except Endgame as ex:
                print('\n' + str(self.__board_service) + '\n')
                print(str(ex))
                break

    @staticmethod
    def choose_difficulty():
        print('\nChoose difficulty:\n1: easy\n2: medium\n3: hard\n')
        difficulty = input('Your choice: ')
        if not difficulty.isnumeric():
            raise Exception('Invalid option!')
        difficulty = int(difficulty)
        if difficulty not in [1, 2, 3]:
            raise Exception('Option not in the list!')
        return difficulty + 1

    def add_names(self):
        first_name = input("First player's name: ")
        second_name = input("Second player's name: ")
        return first_name, second_name

    def first_move(self):
        difficulty = self.choose_difficulty()
        print('\nWho plays first?\n1. You\n2. Computer\n')
        option = input('Add your option: ')
        if not option.isnumeric():
            raise Exception('Invalid option!')
        option = int(option)
        if option == 1:
            player, computer = self.__pieces[0], self.__pieces[1]
        elif option == 2:
            computer, player = self.__pieces[0], self.__pieces[1]
            self.__board_service.computer_move(computer, player, difficulty)
        else:
            raise Exception('Option not in the list!')
        return computer, player, difficulty

    def run_game_computer(self):
        computer, player, difficulty = self.first_move()
        move_number = 0
        while True:
            print('\n' + str(self.__board_service) + '\n')
            option = input("Your turn: ")
            try:
                Validators.validate_option(option)
                option = int(option)
                self.__board_service.your_move(option, player)
                self.__board_service.computer_move(computer, player, difficulty)
                move_number += 1
            except ValidationError as ex:
                print(str(ex))
            except RepoError as ex:
                print(str(ex))
            except Endgame as ex:
                print('\n' + str(self.__board_service) + '\n')
                print(str(ex))
                break
            except Exception as ex:
                print(str(ex))







