import os, sys, re
import setup_ble_station.cli_wizard_checks as check

def make_settings_file(settings_file_paht:str):
    
    print("There were no settings.json found. Let's make one for the system.")
    print("Please answer few questions.")
    
    database_directory_path = "./data"
    while True:
        directory_input = input("Directory where database file will be created [default: data] (hit enter if default is fine): ")
        if len(directory_input)<1: break

        if check.directory_valid(directory_input):
            database_directory_path = directory_input
            break
        else:
            print('not valid directory name')
            continue

    if not re.search("^./", database_directory_path): database_directory_path = "./" + database_directory_path

    if not(check.directory_exists(database_directory_path)):
        os.mkdir(database_directory_path)
        if check.directory_exists(database_directory_path):
            print(f"Directory {database_directory_path} was created successfully.")
        else:
            print('Could not create db-directory!')
            sys.exit(1)
    else: print("Directory already exists. No action taken.")

    db_file = "ble_station.db"
    while True:
        db_file_input = input("Give a name for database file [default=ble_station]: ")
        if len(db_file_input)<1: break

        if check.directory_valid(db_file_input):
            db_file = db_file_input
            break
        else:
            print('Not valid file name!')
            continue
    if not re.search(".db$", db_file): db_file = db_file + ".db"

    # TODO: ruuviTag macs

    

if __name__=='__main__':
    make_settings_file('./settings.json')