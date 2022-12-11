from tkinter import *
from tkinter import filedialog

# Setup
root = Tk()

WIN_WIDTH, WIN_HEIGHT = 1000, 800

root.geometry(F"{WIN_WIDTH}x{WIN_HEIGHT}+{int((root.winfo_screenwidth()/2)-(WIN_WIDTH/2))}+{int((root.winfo_screenheight()/2)-(WIN_HEIGHT/2))}")
root.title("DIREKTO")
root.resizable(False, False)

frame1 = Frame(root, highlightthickness=2, highlightbackground="blue")
frame2 = Frame(root, highlightthickness=2, highlightbackground="blue")
frame3 = Frame(root, highlightthickness=2, highlightbackground="blue")
frame4 = Frame(root, highlightthickness=2, highlightbackground="blue")

frame1.grid(row=0, column=0, padx=20, pady=20, width=100, height=100)
frame2.grid(row=0, column=1, padx=20, pady=20, width=100, height=100)
frame3.grid(row=1, column=0, padx=20, pady=20, width=100, height=100)
frame4.grid(row=1, column=1, padx=20, pady=20, width=100, height=100)

root.mainloop()