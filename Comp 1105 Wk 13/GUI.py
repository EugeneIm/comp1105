from tkinter import *
import tkinter.messagebox


class GUI():
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title("Python GUI")

        #frames
        self.leftFrame = tkinter.Frame(self.main)
        self.rightFrame = tkinter.Frame(self.main)
        self.topFrame = tkinter.Frame(self.leftFrame)
        self.midFrame = tkinter.Frame(self.leftFrame)
        self.botFrame = tkinter.Frame(self.leftFrame)


        #labels
        self.labelOne = tkinter.Label(self.topFrame, width = 10, height = 2, padx = 5, pady = 5, text = "Target")
        self.labelTwo = tkinter.Label(self.midFrame, width = 10, height = 2, padx = 5, pady = 5, text = "# Line")

        #entries
        self.entryOne = tkinter.Entry(self.topFrame, width = 15)
        self.entryTwo = tkinter.Entry(self.midFrame, width = 15)

        #buttons
        self.searchButton = tkinter.Button(self.botFrame, width = 8, text = 'search',)
        self.clear = tkinter.Button(self.botFrame, width = 8, text = 'clear')
        self.quit = tkinter.Button(self.botFrame, width = 8, text = 'quit', command = self.main.destroy)

        
        self.labelOne.pack(side = 'left')
        self.labelTwo.pack(side = 'left')
        self.entryOne.pack(side = 'right')
        self.entryTwo.pack(side = 'right')
        self.searchButton.pack(side = 'left')
        self.clear.pack(side = 'left')
        self.quit.pack(side = 'left')


        #packing them
        self.topFrame.pack()
        self.midFrame.pack()
        self.botFrame.pack()
        self.leftFrame.pack()
        self.rightFrame.pack()


        tkinter.mainloop()




gui = GUI()
