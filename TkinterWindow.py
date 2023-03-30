import tkinter
from sys import exit
import tkinter as tk


class TkinterWindow:
    """
    Creates a tkinter window to ask for information regarding width and height of the maze we want to create.
    Also used for settings window
    """

    def __init__(self):
        self.window = None
        self.lbl = None
        self.board_dim = 0

    def create_window(self, title: str, width=300, height=300):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f'{width}x{height}')

    def call_mainloop(self):
        self.window.mainloop()


class setUpWindow(TkinterWindow):
    def __init__(self):
        super().__init__()
        self.b = None

    def create_attributes(self):
        self.lbl = tk.Label(self.window, text="Give Dimensions for the maze")
        self.lbl.pack(side=tkinter.TOP, padx=50)

        self.b = tk.Entry(self.window, width=35)
        self.b.pack()

        ok_btn = tk.Button(self.window, text="Ok", command=self.clicked_ok)
        ok_btn.pack(side=tkinter.BOTTOM, padx=0)

        cancel_btn = tk.Button(self.window, text="Cancel", command=self.clicked_cancel)
        cancel_btn.pack(side=tkinter.BOTTOM, padx=100)

    @staticmethod
    def validate_input(string):
        return True

    def clicked_ok(self):
        value = self.b.get()
        if self.validate_input(value):
            self.board_dim = value
            self.window.destroy()
        else:
            return

    @staticmethod
    def clicked_cancel():
        exit()


if __name__ == "__main__":
    t = setUpWindow()

    t.create_window("Setup window", 300, 250)
    t.create_attributes()
    t.call_mainloop()
