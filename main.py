from tkinter import *


class Block:
    def __init__(self, master, func):
        self.ent = Entry(master, width=20)
        self.ent2 = Entry(master, width=20)
        self.but = Button(master, text="+")
        self.lab = Label(master, width=20, bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.ent.pack()
        self.ent2.pack()
        self.but.pack()
        self.lab.pack()


    def sum(self):
        s = int(self.ent.get())
        s2 = int(self.ent2.get())
        sum=s+s2
        self.lab=sum


root = Tk()
first_block = Block(root, 'sum')
root.mainloop()
