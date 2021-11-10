

# This is used in custom directory paths. 
def replace_multiple_char_to_string(main_string, to_be_replaced, new_string):
    for elem in to_be_replaced:
        if elem in main_string:
            main_string = main_string.replace(elem, new_string)
    return main_string
