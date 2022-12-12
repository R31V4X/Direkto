def convert_pseudo_to_name(pseudo: str, iterator: str, i_value: str):
    name = ""
    for i in range(len(pseudo)):
        if pseudo[i] == str(iterator):
            name += str(i_value)
        else:
            name += pseudo[i]
    return name


# Create folders 

def create_folder_with_i():
    pass

def create_folder_without_i():
    pass

def create_folder():
    pass




