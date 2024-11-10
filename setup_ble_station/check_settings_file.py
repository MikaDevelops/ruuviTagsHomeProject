import os

def file_present(settings_file:str)->bool:
    return os.path.isfile(f'./{settings_file}')

def settings_valid(settings:dict)->bool:
    if "database" and "ruuviTags" and "azureIotHub" in settings:
        return True
    else:
        return False