from tkinter import *
from tkinter.ttk import *
from settings import *
from tkinter.colorchooser import askcolor

# Setup
root = Tk()

WIN_WIDTH, WIN_HEIGHT = 1000, 800

root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{int((root.winfo_screenwidth()/2)-(WIN_WIDTH/2))}+{int((root.winfo_screenheight()/2)-(WIN_HEIGHT/2))}")
root.title("DIREKTO")
root.resizable(False, False)
root.iconbitmap("ressources/direkto_logo.ico")


# Tabs
notebook = Notebook(root, width=WIN_WIDTH-50, height=WIN_HEIGHT-50)
notebook.pack(pady=25)


tab1 = Frame(notebook, width=WIN_WIDTH-50, height=WIN_HEIGHT-50)
tab1.pack()

tab2 = Frame(notebook, width=WIN_WIDTH-50, height=WIN_HEIGHT-50)
tab2.pack()

tab3 = Frame(notebook, width=WIN_WIDTH-50, height=WIN_HEIGHT-50)
tab3.pack()

notebook.add(tab1, text="Directory Management")
notebook.add(tab2, text="File Management")
notebook.add(tab3, text="Settings")


# Menu 

menu = Menu(root)

def help():
    pass

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label="How to use Direkto")
help_menu.add_command(label="Troubleshooting")
menu.add_cascade(label="Help", menu=help_menu)
menu.add_command(label="Exit", command=root.destroy)

root.config(menu=menu)


#Tab1
#
#   
#
#

# Add sequence of directo0ries

# Frames
add_seq_dir_frame = LabelFrame(tab1, text="Add Sequence of Directories", width=200, height=200)
add_seq_dir_frame.grid(column=0, row=0, padx=15, pady=15)





# Settings tab3
#
#
#


# Frames
general_frame = LabelFrame(tab3, text="General", width=365, height=100)
customize_app_frame = LabelFrame(tab3, text="Customize Appearance")
#general_frame.grid_propagate(0)
#customize_app_frame.grid_propagate(0)

general_frame.grid(column=0, row=0, padx=15, pady=15)
customize_app_frame.grid(column=0, row=1, padx=15, pady=15)

# General : Change dimension
win_dim_label = Label(general_frame, text="Change Window Dimension : ")

win_dim_combobox = Combobox(general_frame, values=window_size_options, state=NORMAL)
win_dim_combobox.set("1000 x 800")

def apply_win_dim():
    global WIN_HEIGHT
    global WIN_WIDTH
    # Fullscreen
    if fullscreen_bool.get() == 1:

        WIN_WIDTH = int(root.winfo_screenwidth())
        WIN_HEIGHT = int(root.winfo_screenheight())

        root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+0+0")
        win_dim_combobox.config(state=DISABLED)

    elif fullscreen_bool.get() == 0:
        root.attributes("-fullscreen", False)
        win_dim_combobox.config(state=NORMAL)

    # Dimension
    dim = win_dim_combobox.get()
    if dim in window_size_options and fullscreen_bool.get() == 0:
        splitted_dim = dim.split(" ")

        WIN_WIDTH = int(splitted_dim[0])
        WIN_HEIGHT = int(splitted_dim[2])

        root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{int((root.winfo_screenwidth()/2)-(WIN_WIDTH/2))}+{int((root.winfo_screenheight()/2)-(WIN_HEIGHT/2))}")
    else:
        pass
    notebook.config(width=WIN_WIDTH-50, height=WIN_HEIGHT-50)
win_dim_apply = Button(general_frame, text="Apply", command=apply_win_dim)

fullscreen_label = Label(general_frame, text="Fullscreen")

fullscreen_bool = IntVar()
fullscreen_checkbox = Checkbutton(general_frame, variable=fullscreen_bool)


fullscreen_label.grid(column=0, row=0, padx=10, pady=10)
fullscreen_checkbox.grid(column=1, row=0, padx=10, pady=10)
win_dim_label.grid(column=0, row=1, padx=10, pady=10)
win_dim_combobox.grid(column=1, row=1, padx=10, pady=10)
win_dim_apply.grid(column=0, row=2, columnspan=2, pady=5)


# Appearance
#bg_color_label = Label(customize_app_frame, text="Background color : ")

#def changecolor():
#    color = askcolor(title="Color Picker")
#bg_color_btn = Button(customize_app_frame, text="Select a color", command=changecolor)


#bg_color_label.grid(column=0, row=0, padx=10, pady=10)
#bg_color_btn.grid(column=1, row=0, padx=10, pady=10, ipadx=3, ipady=2)






root.mainloop()

