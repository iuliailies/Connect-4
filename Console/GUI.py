import tkinter.messagebox
from tkinter import *
from tkinter.simpledialog import askstring

from Errors.Errors import RepoError, Endgame
from Service.ServiceBoard import ServiceBoard
from Repo.Board import Board
from Validators.Validators import Validators


class GUI:

    def __init__(self, board_service, master):
        self.__board_service = board_service
        self.__frame = Frame(master, width=617, height=600, background="SystemButtonFace")
        self.__frame.pack(expand=True)
        self.__frame.grid_propagate(0)
        self.__move = 0
        self.__player = {0: 'X', 1: 'O'}
        self.__colors = {'X': 'indian red',
                         'O': 'steel blue',
                         '.': 'snow',
                         'board': 'gray84',
                         'canvas': 'SystemButtonFace',
                         'button': 'gray94',
                         'text': 'black',
                         'c1': 'white',
                         'c2': 'gray99',
                         'c3': 'gray96'
                        }
        self.__game_mode = None
        self.__first_player = None
        self.__canvas_dict = {}
        self.__status = None
        self.__button_var = IntVar(self.__frame)  # default value 0
        self.__names = {0: StringVar(self.__frame), 1: StringVar(self.__frame)}
        self.__dark_theme = IntVar(self.__frame)

    def run_game(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()
        welcome_label = Label(self.__frame, text='\nWelcome to CONNECT 4!\n', font='Courier 20 bold', width=30, fg=self.__colors['X'], bg = self.__colors['canvas'])
        welcome_label.grid(row=0, columnspan=18, padx=(70,0), pady=(30, 30))
        start_label = Label(self.__frame, text='Start a game:', font=('TkDefaultFont', 12), bg = self.__colors['canvas'], fg=self.__colors['text'])
        start_label.grid(row=1, padx=5,  pady=5)
        button_player = Button(self.__frame, text='Another player', height=2, width=12, command= lambda: self.set_mode('player'), bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        button_player.grid(row=2, rowspan=2, pady=(30,0))
        button_computer = Button(self.__frame, text='Computer',height=2, width=12, command= lambda: self.set_mode('computer'), bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        button_computer.grid(row=4, rowspan=2, pady=5)
        who_plays_first_button = Radiobutton(self.__frame, text='you begin', variable=self.__button_var, value=1, bg = self.__colors['canvas'], fg=self.__colors['text'], selectcolor=self.__colors['button'], activebackground=self.__colors['canvas'])
        who_plays_first_button.grid(row=4, column=1, sticky=SW)
        who_plays_first_button = Radiobutton(self.__frame, text='computer begins', variable=self.__button_var, value=0, bg = self.__colors['canvas'], fg=self.__colors['text'], selectcolor=self.__colors['button'], activebackground=self.__colors['canvas'])
        who_plays_first_button.grid(row=5, column =1, sticky=NW)
        button_exit = Button(self.__frame, text='Exit',height=2, width=12, command=self.__frame.quit, bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        button_exit.grid(row=6, rowspan=2, pady=(5, 0))
        self.__frame.rowconfigure(8, weight=1)
        dark_theme_button = Radiobutton(self.__frame, text='Dark theme', command= lambda: self.dark_theme('dark'), variable=self.__dark_theme, value=1, bg = self.__colors['canvas'], fg=self.__colors['text'], selectcolor=self.__colors['button'], activebackground=self.__colors['canvas'])
        dark_theme_button.grid(row=9, padx=(5,0), pady=10, sticky=W)
        light_theme_button = Radiobutton(self.__frame, text='Light theme', command= lambda: self.dark_theme('light'), variable=self.__dark_theme, value=0, bg = self.__colors['canvas'], fg=self.__colors['text'], selectcolor=self.__colors['button'], activebackground=self.__colors['canvas'], activeforeground=self.__colors['text'])
        light_theme_button.grid(row=9, column=1, pady=10, sticky = W)
        self.create_drawing()
        self.__board_service.clear_board()
        self.__move = 0

    def ask_name(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()
        welcome_label = Label(self.__frame, text='\nWelcome to CONNECT 4!\n', font='Courier 20 bold', width=30, fg=self.__colors['X'], bg = self.__colors['canvas'])
        welcome_label.grid(row=0, columnspan=18, padx=(70,0), pady=(30, 30))
        start_label = Label(self.__frame, text='Add your names:', font=('TkDefaultFont', 12), bg = self.__colors['canvas'], fg=self.__colors['text'])
        start_label.grid(row=1, padx=5,  pady=5, sticky=E)
        label_1 = Label(self.__frame, text="First player:", bg = self.__colors['canvas'], fg=self.__colors['text'])
        label_2 = Label(self.__frame, text="Second player:",bg = self.__colors['canvas'], fg=self.__colors['text'])
        entry_1 = Entry(self.__frame, textvariable= self.__names[0])
        entry_2 = Entry(self.__frame, textvariable= self.__names[1])
        label_1.grid(row=3, sticky=NE, pady=(10, 0))
        label_2.grid(row=4, sticky=E)
        entry_1.grid(row=3, column=1)
        entry_2.grid(row=4, column=1)
        start_button = Button(self.__frame, text = 'Start Game', height=2, width=12, command=self.convert_board_to_interface, bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        start_button.grid(row=6, padx=(0,5), sticky=E)
        back_button = Button(self.__frame, text='Go back', height=2, width=12, command=self.run_game, bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        back_button.grid(row=6, column=1, padx=(0,5), sticky=E)
        self.create_drawing()

    def set_mode(self, mode):
        self.__game_mode = mode
        if mode == 'player':
            self.ask_name()
        elif mode == 'computer':
            if self.__button_var.get() == 1:
                self.set_first('player')
            else:
                self.set_first('computer')

    def set_first(self, first):
        self.__first_player = first
        self.convert_board_to_interface()
        if first == 'computer':
            row, column = self.__board_service.computer_move(self.__player[0], self.__player[1], 3)
            canvas, circle = self.__canvas_dict[(5 - row, column - 1)]
            canvas.itemconfig(circle, fill=self.__colors[self.__player[0]])

    def convert_board_to_interface(self):
        if len(self.__names[0].get()) == 0:
            self.__names[0].set(value='Player 1')
        if len(self.__names[1].get()) == 0:
            self.__names[1].set(value='Player 2')
        for widget in self.__frame.winfo_children():
            widget.destroy()
        for row in range(5, -1, -1):
            for column in range (0,7):
                circle_button = Label(self.__frame, bg=self.__colors['board'])
                circle_button.grid(row=row, column=column)
                canvas = Canvas(circle_button, width=80, height=80, bg=self.__colors['board'], highlightbackground=self.__colors['.'])
                state = self.__board_service.get_board()[column + 1][5-row].get_state() # X, O or .
                circle = canvas.create_oval(10, 10, 70, 70, fill=self.__colors[state])
                canvas.grid(row=row, column=column)
                self.__canvas_dict[(row, column)] = (canvas, circle)
                canvas.bind('<Button-1>', self.click_handler)

        self.__status = Label(self.__frame, bg = self.__colors['canvas'], font=('TkDefaultFont', 11))
        self.__status.grid(row =6, column=0, columnspan=3, pady=10, ipadx=10, ipady=10, sticky=W)
        button_player = Button(self.__frame, text='New game', height=1, width=7, command=self.run_game, bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        button_player.grid(row=6, column=5, padx=(0, 3), pady=10, ipadx=10, ipady=10, sticky=E)
        button_player = Button(self.__frame, text='Exit', height=1, width=7,  command=self.__frame.quit, bg = self.__colors['button'], activebackground=self.__colors['button'], fg=self.__colors['text'])
        button_player.grid(row=6, column=6, padx=(0, 3),  pady=10, ipadx=10, ipady=10, sticky=E)

    def click_handler(self, event):
        if self.__game_mode == 'player':
            column = event.widget.grid_info()['column']
            try:
                row = self.__board_service.move_and_endgame_check(column + 1, self.__player[self.__move % 2], self.__names[self.__move % 2].get())
                canvas, circle = self.__canvas_dict[(5-row, column)]
                canvas.itemconfig(circle, fill=self.__colors[self.__player[self.__move % 2]])
                self.__move += 1
                self.__status.config(text="{}'s turn".format(self.__names[self.__move % 2].get()), fg=self.__colors[self.__player[self.__move % 2]])
            except RepoError:
                pass
            except Endgame as ex:
                self.convert_board_to_interface()
                tkinter.messagebox.showinfo('Endgame', ex)
                self.run_game()
        elif self.__game_mode == 'computer':
            if self.__first_player == 'computer':
                computer = self.__player[0]
                player = self.__player[1]
            else:
                player = self.__player[0]
                computer = self.__player[1]
            try:
                column = event.widget.grid_info()['column']
                row = self.__board_service.your_move(column + 1, player)
                canvas, circle = self.__canvas_dict[(5 - row, column)]
                canvas.itemconfig(circle, fill=self.__colors[player])
                self.__status.config({'text': "Computer's turn", 'fg': self.__colors[computer]})
                row, column = self.__board_service.computer_move(computer, player, 3)
                canvas, circle = self.__canvas_dict[(5 - row, column - 1)]
                self.__frame.after(1200, canvas.itemconfig, circle, {'fill': self.__colors[computer]})
                self.__frame.after(1200, self.__status.config, {'text': 'Your turn', 'fg': self.__colors[player]})
            except RepoError:
                pass
            except Endgame as ex:
                self.convert_board_to_interface()
                tkinter.messagebox.showinfo('Endgame', ex)
                self.run_game()

    def dark_theme(self, mode):
        if mode == 'dark':
            self.__colors = {'X': 'indian red',
                             'O': 'steel blue',
                             '.': 'gray42',
                             'board': 'gray20',
                             'canvas': 'gray20',
                             'button': 'gray25',
                             'text': 'white',
                             'c1': 'gray36',
                             'c2': 'gray25',
                             'c3': 'gray21'
                             }
            self.__frame.config(bg='gray20')
        else:
            self.__colors = {'X': 'indian red',
                             'O': 'steel blue',
                             '.': 'snow',
                             'board': 'gray84',
                             'canvas': 'SystemButtonFace',
                             'button': 'gray94',
                             'text': 'black',
                             'c1': 'white',
                             'c2': 'gray99',
                             'c3': 'gray96'
                            }
            self.__frame.config(bg='SystemButtonFace')
        self.run_game()

    def create_drawing(self):
        for i in range(3):
            for j in range(3-i):
                canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
                canvas.create_oval(10, 10, 40, 40, fill=self.__colors[self.__player[1]], outline=self.__colors[self.__player[1]])
                canvas.grid(row=6-i, column=18-j, sticky=S)

        for i in range(4):
            canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
            circle = canvas.create_oval(10, 10, 40, 40, fill=self.__colors[self.__player[0]], outline=self.__colors[self.__player[0]])
            canvas.grid(row=6-i, column=15+i, sticky=S)
            self.__frame.after(500 + (i + 1) * 200, canvas.itemconfig, circle, {'outline': self.__colors['text']})
            self.__frame.after(500 + (i + 2) * 200, canvas.itemconfig, circle, {'outline': self.__colors[self.__player[0]]})

        for i in range(5):
            canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
            canvas.create_oval(10, 10, 40, 40, fill=self.__colors['c3'], outline=self.__colors['c3'])
            canvas.grid(row=6 - i, column=14, sticky=S)

            canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
            canvas.create_oval(10, 10, 40, 40, fill=self.__colors['c3'], outline=self.__colors['c3'])
            canvas.grid(row=2, column=14 + i, sticky=S)

        for i in range(3):
            canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
            canvas.create_oval(10, 10, 40, 40, fill=self.__colors['c2'], outline=self.__colors['c2'])
            canvas.grid(row=5 - i, column=15, sticky=S)

            canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
            canvas.create_oval(10, 10, 40, 40, fill=self.__colors['c2'], outline=self.__colors['c2'])
            canvas.grid(row=3, column=15+i, sticky=S)

        canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
        canvas.create_oval(10, 10, 40, 40, fill=self.__colors['c1'], outline=self.__colors['c1'])
        canvas.grid(row=4, column=16, sticky=S)

        canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
        canvas.create_oval(10, 10, 40, 40, fill=self.__colors[self.__player[0]], outline=self.__colors[self.__player[0]])
        canvas.grid(row=5, column=18, sticky=S)
        canvas = Canvas(self.__frame, width=40, height=40, highlightthickness=0, bg=self.__colors['canvas'])
        canvas.create_oval(10, 10, 40, 40, fill=self.__colors[self.__player[0]], outline=self.__colors[self.__player[0]])
        canvas.grid(row=6, column=17, sticky=S)


Board = Board()
BoardValidator = Validators()
ServiceBoard = ServiceBoard(Board, BoardValidator)

root = Tk()
interface = GUI(ServiceBoard, root)
interface.run_game()
root.mainloop()

