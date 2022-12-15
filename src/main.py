from tkinter import *
from tkinter.ttk import *
from settings import *
from dir_functions import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, showinfo
import os

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

notebook.add(tab1, text="Folder Management")
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

##################
#Tab1
#
#   
#
#####################

# Add sequence of directories
# frame
add_seq_dir_frame = LabelFrame(tab1, text="Add Sequence of Folders")
add_seq_dir_frame.grid(column=0, row=0, padx=15, pady=15, ipadx=10)

with_i_frame = LabelFrame(add_seq_dir_frame, text="With iterator")
without_i_frame = LabelFrame(add_seq_dir_frame, text="Without iterator")

# Widget
parent_folder1_label = Label(add_seq_dir_frame, text="Parent folder : ")
parent_folder1_entry = Entry(add_seq_dir_frame, width=38)

def parent_folder1_search():
    path = askdirectory()
    parent_folder1_entry.delete(0, END)
    parent_folder1_entry.insert(END, str(path))

parent_folder1_browse = Button(add_seq_dir_frame, text="Browse", command=parent_folder1_search)

i_bool = IntVar()
def change_i_bool():
    if i_bool.get() == 0:
        name_folder_with_i_label.config(state=DISABLED)
        name_folder_with_i_entry.config(state=DISABLED)
        iterator_char_label.config(state=DISABLED)
        iterator_char_entry.config(state=DISABLED)
        start_num_label.config(state=DISABLED)
        start_num_spin.config(state=DISABLED)
        end_num_label.config(state=DISABLED)
        end_num_spin.config(state=DISABLED)
        incrementation_num_label.config(state=DISABLED)
        incrementation_num_spin.config(state=DISABLED)

        num_folder_label.config(state=NORMAL)
        num_folder_spin.config(state=NORMAL)
        name_folder_without_i_label.config(state=NORMAL)
        name_folder_without_i_entry.config(state=NORMAL)

    elif i_bool.get() == 1:
        name_folder_with_i_label.config(state=NORMAL)
        name_folder_with_i_entry.config(state=NORMAL)
        iterator_char_label.config(state=NORMAL)
        iterator_char_entry.config(state=NORMAL)
        start_num_label.config(state=NORMAL)
        start_num_spin.config(state=NORMAL)
        end_num_label.config(state=NORMAL)
        end_num_spin.config(state=NORMAL)
        incrementation_num_label.config(state=NORMAL)
        incrementation_num_spin.config(state=NORMAL)

        num_folder_label.config(state=DISABLED)
        num_folder_spin.config(state=DISABLED)
        name_folder_without_i_label.config(state=DISABLED)
        name_folder_without_i_entry.config(state=DISABLED)
without_i_radio = Radiobutton(add_seq_dir_frame, text="Without iterator", variable=i_bool, value=0, command=change_i_bool)
with_i_radio = Radiobutton(add_seq_dir_frame, text="With iterator", variable=i_bool, value=1, command=change_i_bool)


parent_folder1_label.grid(column=0, row=0, padx=10, pady=10)
parent_folder1_entry.grid(column=1, row=0, padx=10, pady=10)
parent_folder1_browse.grid(column=2, row=0, pady=10)

without_i_radio.grid(column=0, row=1, padx=10, pady=10)
# Without i frame
without_i_frame.grid(column=0, columnspan=2, row=2, padx=10, pady=10)
num_folder_label = Label(without_i_frame, text="Number of folders to create : ", state=NORMAL)
num_folder_spin = Spinbox(without_i_frame, from_=0, to=99, state=NORMAL )
name_folder_without_i_label = Label(without_i_frame, text="Name of folder to create : ", state=NORMAL)
name_folder_without_i_entry = Entry(without_i_frame, state=NORMAL)

name_folder_without_i_label.grid(column=0, row=0, padx=5, pady=5)
name_folder_without_i_entry.grid(column=1, row=0, padx=5, pady=5)
num_folder_label.grid(column=0, row=1, padx=5, pady=5)
num_folder_spin.grid(column=1, row=1, padx=5, pady=5)

with_i_radio.grid(column=0, row=3, pady=10)
# With i frame
with_i_frame.grid(column=0, columnspan=2, row=4, padx=10, pady=10)
name_folder_with_i_label = Label(with_i_frame, text="Pseudo-name of folder to create : ", state=DISABLED)
name_folder_with_i_entry = Entry(with_i_frame, state=DISABLED)
iterator_char_label = Label(with_i_frame, text="Iterator character : ", state=DISABLED)
iterator_char_entry = Entry(with_i_frame, state=DISABLED, width=1)
start_num_label = Label(with_i_frame, state=DISABLED, text="Start value : ")
start_num_spin = Spinbox(with_i_frame, state=DISABLED, width=10)
end_num_label = Label(with_i_frame, state=DISABLED, text="End value : ")
end_num_spin = Spinbox(with_i_frame, state=DISABLED, width=10)
incrementation_num_label = Label(with_i_frame, state=DISABLED, text="Incrementation (Ex : -1, +2) : ")
incrementation_num_spin = Entry(with_i_frame, state=DISABLED, width=10)


name_folder_with_i_label.grid(column=0, row=0, padx=5, pady=5)
name_folder_with_i_entry.grid(column=1, row=0, padx=5, pady=5)
iterator_char_label.grid(column=3, row=0, padx=10, pady=5)
iterator_char_entry.grid(column=4, row=0, padx=5, pady=5)
start_num_label.grid(column=0, row=2, padx=3, pady=5, sticky=W)
start_num_spin.grid(column=0, row=2, pady=5, sticky=E)
end_num_label.grid(column=0, row=3, padx=3, pady=5, sticky=W)
end_num_spin.grid(column=0, row=3, pady=5, sticky=E)
incrementation_num_label.grid(column=0, row=4, padx=3, pady=5, sticky=W)
incrementation_num_spin.grid(column=1, row=4, pady=5, sticky=W)



# Create folders functions

def verify_field_filled(radio_option):
    if radio_option == 0:
        if len(name_folder_without_i_entry.get()) != 0 and len(num_folder_spin.get()) != 0:
            return True
        else:
            return False
    elif radio_option == 1:
        if len(name_folder_with_i_entry.get()) != 0 and len(iterator_char_entry.get()) != 0 and len(start_num_spin.get()) != 0 and len(end_num_spin.get()) != 0 and len(incrementation_num_spin.get()) != 0:
            return True
        else:
            return False
    else:
        return "Error"




def create_folder_without_i():
    # Verify if spin is number
    try:
        int(num_folder_spin.get())
    except ValueError:
        showerror("VALUE ERROR", "This entry has an invalid value : Number of folders to create\n\nMake sure to pick an integer larger than 0")
        return

    if int(num_folder_spin.get()) < 1:
        showerror("VALUE ERROR", "This entry has an invalid value : Number of folders to create\n\nMake sure to pick a number larger than 0")
        return
    else:

    
        showinfo("SUCCESS", "Folders created with success!")


def create_folder_with_i():
    showinfo("SUCCESS", "Folders created with success!")




def create_folder():
    global i_bool
    if verify_field_filled(i_bool.get()) == False:
        showerror("Field missing!", "Make sure to fill all the required fields!")
        return
    if i_bool.get() == 0:
        create_folder_without_i()
    elif i_bool.get() == 1:
        create_folder_with_i()
        showinfo("SUCCESS", "Folders created with success!")
    else:
        showerror("ERROR", "Error : Can't find option selected")
# Apply
apply_seq_folder = Button(add_seq_dir_frame, text="Create folders", command=create_folder, width=20)
apply_seq_folder.grid(column=0, columnspan=4, row=5, pady=20)





############################
# Settings tab3
#
#
########################


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

