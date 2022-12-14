def convert_pseudo_to_name(pseudo: str, iterator: str, i_value: str):
    name = ""
    for i in range(len(pseudo)):
        if pseudo[i] == str(iterator):
            name += str(i_value)
        else:
            name += pseudo[i]
    return name


# Create folders 

def verify_field_filled(radio_option):
    pass


def error_box(error_message: str):
    pass

def success_box(success_message: str):
    pass

def create_folder_with_i():
    pass

def create_folder_without_i():
    pass



def create_folder(radio_option):
    if radio_option == 0:
        create_folder_without_i()
    else:
        create_folder_with_i()





