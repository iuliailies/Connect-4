
class Patratica:
    '''
    This class describes the unit of the board game, with the 'state' attribute:
    - . if the spot is not occupied
    - X if it's occupied by the first player
    - O if it's occupied by the second player
    '''

    def __init__(self):
        self.__state = '.'

    def get_state(self):
        return self.__state

    def set_state(self, player):
        self.__state = player

    def __str__(self):
        return self.__state

    def __eq__(self, other):
        return self.__state == other.__state



