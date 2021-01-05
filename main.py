from tkinter import *

from Console.GUI import GUI
from Console.UI import UI
from Service.ServiceBoard import ServiceBoard
from Repo.Board import Board
from Validators.Validators import Validators

Board = Board()
BoardValidator = Validators()
ServiceBoard = ServiceBoard(Board, BoardValidator)
print('1.UI\n2.GUI\n')
interface = input('Choose your option: ')
if interface == '1':
    UI = UI(ServiceBoard)
    UI.run_game()
elif interface == '2':
    root = Tk()
    interface = GUI(ServiceBoard, root)
    interface.run_game()
    root.mainloop()