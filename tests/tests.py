import tkinter as tk
from tkinter import filedialog
# Setup
root = tk.Tk()

WIN_WIDTH, WIN_HEIGHT = 1000, 800

root.geometry(F"{WIN_WIDTH}x{WIN_HEIGHT}+{int((root.winfo_screenwidth()/2)-(WIN_WIDTH/2))}+{int((root.winfo_screenheight()/2)-(WIN_HEIGHT/2))}")
root.title("DIREKTO")
root.resizable(False, False)



def btn():
    filename = filedialog.askdirectory()

    Labe


btn = tk.Button(root, text="Browse", command=btn) 

root.mainloop()
