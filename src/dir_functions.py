def convert_pseudo_to_name(pseudo: str, iterator: str, i_value: str):
    name = ""
    for i in range(len(pseudo)):
        if pseudo[i] == str(iterator):
            name += str(i_value)
        else:
            name += pseudo[i]
    return name


# Create folders 





