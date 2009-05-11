from tkinter import *
import sys

class Console(Frame):
    "Route stdout and stderr to a window."
    def build_widgets(self):
        self.txt = Text(self)
        self.txt.pack(side=TOP)
        self.input = Input(self)
        self.input.pack(side=BOTTOM)

    def write(self, txt):
        "Object can now act as stdout/stderr replacement!"
        self.txt.insert(INSERT, txt)
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.build_widgets()
        # Override default stdout/err.
        sys.stdout = self
        sys.stderr = self

class Input(Entry):
    "Route a window to stdin."
    def __init__(self, master=None):
        Entry.__init__(self, master)
        self.bind("<KeyPress-Return>", self.read)

    def read(self, line):
        sys.stdin.write(self.get())
        self.delete(0,END)
        
    
class Gui():
    def __init__(self):
        root = Tk()
        self.app = Console(master = root)
    def mainloop(self):
        self.app.mainloop()
    
