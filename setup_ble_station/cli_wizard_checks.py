import re, os

def directory_valid(directory:str)->bool:
    
    if len(directory)<1:
        return False
    
    space_in_name = re.search("\s", directory)
    if space_in_name:
        return False
    
    special_char_in_name = re.search("[^a-zA-Z0-9_-]", directory)
    if special_char_in_name:
        return False
    
    return True

def directory_exists(directory:str)->bool:
    return os.path.isdir(directory)