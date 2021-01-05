from tkinter import *

''' basics '''
# root = Tk() # tkinter class we have just imported
# theLabel = Label(root, text='Hihi')
# theLabel.pack() # to display
# root.mainloop() # to keep it open

''' organizing and layout '''

# root = Tk()

# topFrame = Frame(root) # invisible container
# topFrame.pack() # don t forget to display!!!
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text='Bottom 1', fg='purple')
# button2 = Button(topFrame, text='Bottom 2', fg='blue')
# button3 = Button(topFrame, text='Bottom 3', fg='red')
# button4 = Button(bottomFrame, text='Bottom 4', fg='pink')
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack()
#
#
# root.mainloop()

''' fitting widgets in your layout'''

# root = Tk()
#
# one = Label(root, text = 'One', bg = 'red', fg = 'white') # background red; font white
# one.pack()
# two = Label(root, text = 'Two', bg = 'green', fg = 'black')
# two.pack(fill=X) # when we resize, the label will grow in X direction
# three = Label(root, text = 'Three', bg = 'blue', fg = 'white')
# three.pack(side=LEFT, fill=Y)
#
# root.mainloop()

''' Grid layout '''

# root = Tk()
#
# label_1 = Label(root, text='Name')
# label_2 = Label(root, text='Password')
# entry_1 = Entry(root) # blank space when you can write stuff in
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=E) # E from Est
# label_2.grid(row=1, sticky=E)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# checkbox = Checkbutton(root, text='Keep me logged in')
# checkbox.grid(columnspan=2) # fits in 2 collumns
#
# root.mainloop()

''' Binding functions to layouts'''

# def printName():
#     print('Hihi')
#
# def printMe(event):
#     print('Hihi')

# root = Tk()
#
# # METODA 1:
# button_1 = Button(root, text='Print', command=printName)
# button_1.pack()
#
# # METODA 2:
# button_2 = Button(root, text='Another print')
# button_2.bind('<Button-1>', printMe)
# button_2.pack()
#
# root.mainloop()


''' Mouse Click Events: left middle right'''

# root = Tk()
#
# def leftClick(event):
#     print('Left')
#
# def rightClick(event):
#     print('Right')
#
# def middleClick(event):
#     print('Middle')
#
# frame = Frame(root, width=300, height=250) # pixels
# frame.bind('<Button-1>', leftClick) # Button-1: left click on mouse
# frame.bind('<Button-2>', middleClick)
# frame.bind('<Button-3>', rightClick)
# frame.pack()
#
#
# root.mainloop()

''' Using Classes'''


# class Buttons:
#     def __init__(self, master): # master: root or main window
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text='print function', command = self.printmessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text='Quit', command=frame.quit) # breaks the main loop
#         self.quitButton.pack(side=LEFT)
#
#     def printmessage(self):
#         print('Message')
#
#
# root = Tk()
# object = Buttons(root)
# root.mainloop()

''' Creating drop down menus'''

# def doNothing():
#     print('Did nothing;)')

# root = Tk()
#
# menu = Menu(root) # Menu class to create a menu object
# root.config(menu=menu)
#
# # example: File, Edit
# subMenu = Menu(menu)
# menu.add_cascade(label='File', menu=subMenu)
# subMenu.add_command(label='New Project', command=doNothing)
# #creating a separator
# subMenu.add_separator()
# subMenu.add_command(label='Exit', command=doNothing)
#
#
# editMenu = Menu(menu)
# menu.add_cascade(label='Edit', menu=editMenu)
# editMenu.add_command(label='Redo', command=doNothing)

''' Creating toolbar '''

# toolbar = Frame(root, bg='blue')
# insertButton = Button(toolbar, text='Insert image', command=doNothing)
# insertButton.pack(side=LEFT, padx=2, pady=2) # pad - extra space
# insertButton = Button(toolbar, text='Print', command=doNothing)
# insertButton.pack(side=LEFT, padx=2, pady=2) # pad - extra space
# toolbar.pack(side=TOP, fill=X)

''' Creating Status bar '''

# status = Label(root, text='...', bd=1, relief=SUNKEN, anchor =W)
# status.pack(side=BOTTOM, fill=X)
#
# root.mainloop()


''' Message box '''

# import tkinter.messagebox
#
# root = Tk()
#
# tkinter.messagebox.showinfo('Window Title', 'popup') # no option, just ok button
#
# answer = tkinter.messagebox.askquestion('Question 1', 'Yes or no?')
# if answer == 'yes':
#     print('you said yes')
#
# root.mainloop()

''' Shapes and Graphics - CANVAS '''

# root = Tk()
#
# canvas = Canvas(root, width=200, height=100) # place to make shapes on
# canvas.pack()
#
# blackLine = canvas.create_line(0, 0, 200, 50) # beginning point and ending point (x, y coordinates)
# redLine = canvas.create_line(0, 100, 200, 50, fill='red')
#
# greenBox = canvas.create_rectangle(25,25, 130, 60, fill = 'green') # first: top left, width, height
#
# canvas.delete(redLine)
# canvas.delete(ALL)
#
# root.mainloop()

''' Images and icons '''

# check video 14 from thenewboston :)

# root = Tk()
#
# def get_column(event):
#     y = event.widget.grid_info()['column']
#     x = event.widget.grid_info()['row']
#     print(x, y)
#
#
# button = Button(root, text='B1')
# button.grid(row=1, column=2)
# button.bind('<Button-1>', get_column)
# root.mainloop()

# root = Tk()
# frame1 = Frame(root, width=50, height=100, background="bisque")
# root.mainloop()

root = Tk()
frame = Frame(root)
bg = frame.cget("background")
print(bg)