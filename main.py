import tkinter as tk

#Text-Based and GUI
class view():

    def __init__(self):
        root = tk.Tk()
        board = tk.Frame(root)
        board.pack()
        canvas = tk.Canvas(root, bg="red", height = 100, width= 200)
        canvas.pack()
        root.mainloop()


start = view()
#Handle Connecting view and model
class controller():

    def __init__(self):
        return self



#Handle Logic
class model():

    def __init__(self):
        return self
