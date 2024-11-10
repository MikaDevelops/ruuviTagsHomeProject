import json

def settings_from_file(settings_file:str)->dict:
    with open(settings_file, 'r') as sf:
        settings = json.load(sf)
    return settings