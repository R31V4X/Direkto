from tkinter import *
from tkinter.ttk import *
from settings import *

# Setup
root = Tk()

WIN_WIDTH, WIN_HEIGHT = 1000, 800

root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{int((root.winfo_screenwidth()/2)-(WIN_WIDTH/2))}+{int((root.winfo_screenheight()/2)-(WIN_HEIGHT/2))}")
root.title("DIREKTO")
root.resizable(False, False)
root.iconbitmap("ressources/direkto_logo.ico")


# Tabs
notebook = Notebook(root)
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

# Add sequence of directories

add_seq_dir_frame = LabelFrame(tab1, text="Add Sequence of Directories", width=200, height=200)
add_seq_dir_frame.grid(column=0, row=0, padx=20, pady=20)




# Settings tab3
#
#
#


# Frames
general_frame = LabelFrame(tab3, text="General")
customize_app_frame = LabelFrame(tab3, text="Customize Appearance")

general_frame.grid(column=0, row=0, padx=15, pady=15)
customize_app_frame.grid(column=0, row=1, padx=15, pady=15)

# General : Change dimension
win_dim_label = Label(general_frame, text="Change Window Dimension : ")

win_dim_combobox = Combobox(general_frame, values=window_size_options)
win_dim_combobox.set("1000 x 800")


def apply_win_dim():
    dim = win_dim_combobox.get()
    if dim in window_size_options:
        splitted_dim = dim.split(" ")

        width = int(splitted_dim[0])
        height = int(splitted_dim[2])

        root.geometry(f"{width}x{height}+{int((root.winfo_screenwidth()/2)-(width/2))}+{int((root.winfo_screenheight()/2)-(height/2))}")
    else:
        pass
win_dim_apply = Button(general_frame, text="Apply", command=apply_win_dim)


win_dim_label.grid(column=0, row=0, padx=10, pady=10)
win_dim_combobox.grid(column=1, row=0, padx=10, pady=10)
win_dim_apply.grid(column=0, row=1, columnspan=2, pady=5)






root.mainloop()

