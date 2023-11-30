from tkinter import *
import tkinter.messagebox

class myGui():
    def __init__(self, filename):
        #making the code more efficient by making a dictionry from file 
        self.info = self.wordDict(filename)
        
        # making the window
        self.main_window = Tk()
        self.main_window.title('Word Statistic!')
        
        #left frame
        self.left_frame = Frame(self.main_window)
        self.left_top = Frame(self.left_frame)
        self.target_label = Label(self.left_top, text = 'Target', padx=5, pady=5)
        self.target_entry = Entry(self.left_top, width = 20)
        self.left_mid = Frame(self.left_frame)
        self.line_label = Label(self.left_mid, text = '# Line', padx=5, pady=5)
        self.line_entry = Entry(self.left_mid, width = 20)
        self.left_bot = Frame(self.left_frame)
        self.search_button = Button(self.left_bot, text = 'Search', command=self.search)
        self.clear_button = Button(self.left_bot, text = 'Clear', command=self.clear)
        self.quit_button = Button(self.left_bot, text = 'Quit', command=self.main_window.destroy)
        
        #right frame
        self.right_frame = Frame(self.main_window)
        self.header = Label(self.right_frame, text = 'Results')
        self.result_var1 = StringVar()
        self.search_res1 = Label(self.right_frame, width=45, textvariable=self.result_var1)
        self.result_var2 = StringVar()
        self.search_res2 = Label(self.right_frame, width=45, textvariable=self.result_var2)
        
        #pack frames
        self.left_frame.pack(side = 'left')
        self.left_top.pack()
        self.left_mid.pack()
        self.left_bot.pack()
        self.right_frame.pack(side = 'right')
        
        
        #pack misc.
        self.target_label.pack(side = 'left')
        self.target_entry.pack(side = 'left')
        self.line_label.pack(side = 'left')
        self.line_entry.pack(side = 'left')
        self.search_button.pack(side = 'left')
        self.clear_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        self.header.pack()
        self.search_res1.pack()
        self.search_res2.pack()

        mainloop()
        #end init


    #clear - clears the entry field
    def clear(self):
        self.target_entry.delete(0, 'end') #deletes all the characters from index 0 to the end. 
        self.line_entry.delete(0, 'end')
        self.result_var1.set('')
        self.result_var2.set('')
        #end function
        
        
    #search - searched the text file and returns how many times a word is in a line and how many unique words the line holds
    def search(self):
        if self.checkInputs(): 
            self.searchWord()

    def searchWord(self):
        word = self.target_entry.get().strip(' ')
        ln = self.line_entry.get().strip(' ')
        word_set = set()
        cn = 0
        for w in self.info[int(ln)]:
            if(w != ''):
                word_set.add(w)
                if(w.lower() == word.lower()):
                    cn += 1
        self.result_var1.set('-'+"'"+ word +"' "+'is repeated ' +str(cn)+ ' time(s) in line '+ ln)
        self.result_var2.set('-Line ' + ln + ' includes '+str(len(word_set))+' distinct word(s).')

        
    def checkInputs(self):
        flag = True
        try:
            ln = int(self.line_entry.get())
            if ln not in self.info.keys():
                tkinter.messagebox.showinfo('Info Error', 'The input file is shorter than ' + str(ln)+ ' lines. Please try again!')
                flag = False
        except Exception as err:
            tkinter.messagebox.showerror('Data Error', 'Invalid entry for line number.')
            flag = False
        word = self.target_entry.get().strip(' ').lower()
        if not (word.isalpha() and word != ''):
            tkinter.messagebox.showinfo('Info Error', 'The target is not valid. Please try again!')
            flag = False
        return flag
    
    #wordDict - reads in a text file and creates a dictionary where key = line # and value = list of words
    #@return word_records - a dictionary containing the words and their line numbers as key
    def wordDict(self, fname):
        infile = open(fname, 'r')
        lines = infile.readlines()
        records = dict()
        ln = 0
        for line in lines:
            ln += 1
            linels = line.split(' ')
            linels = [x.strip('\n\t?1234567890-=`"~!@#$%^&*()_+{}:|<>/.,;][') for x in linels]          
            records.update({ln:linels})
        infile.close()
        return records
        #end function

new_gui = myGui('textfile.txt')





















