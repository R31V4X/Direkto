from tkinter import *
from tkinter.ttk import *

# Setup
root = Tk()

WIN_WIDTH, WIN_HEIGHT = 1000, 800

root.geometry(F"{WIN_WIDTH}x{WIN_HEIGHT}+{int((root.winfo_screenwidth()/2)-(WIN_WIDTH/2))}+{int((root.winfo_screenheight()/2)-(WIN_HEIGHT/2))}")
root.title("DIREKTO")
root.resizable(False, False)


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

#   Add sequence of directories
#
#
#
#


add_seq_dir_frame = LabelFrame(tab1, text="Add Sequence of Directories", width=200, height=200)
add_seq_dir_frame.grid(column=0, row=0, padx=20, pady=20)




# Settings tab3

general_frame = LabelFrame(tab3, text="General")
customize_graph_frame = LabelFrame(tab3, text="Customize Appearance")


win_dim_label = Label(general_frame, text="Change windows dimension : ")


general_frame.pack(pady=15)
customize_graph_frame.pack(pady=15)




root.mainloop()

