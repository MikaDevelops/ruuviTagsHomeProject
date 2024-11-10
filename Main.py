import asyncio
import sys

import setup_ble_station.check_settings_file as check_settings
import setup_ble_station.settings_load as settings_loader
import setup_ble_station.cli_wizard as cli_wizard
from tags import macs
from db.Sqlite_handler import Sqlite_handler
from ble.ble import read_data_from_tags

def main():
    SYSTEM_SETTINGS_FILE = './settings.json'

    # check settings file
    if check_settings.file_present(SYSTEM_SETTINGS_FILE):
        # if file found, load settings
        SYSTEM_SETTINGS = settings_loader.settings_from_file(SYSTEM_SETTINGS_FILE)
        # check that valid settings
        if not(check_settings.settings_valid(SYSTEM_SETTINGS)):
            print("settings.json is not valid. Please check the file.")
            sys.exit(1)

    # if no settings file start cli wizard
    if not check_settings.file_present(SYSTEM_SETTINGS_FILE):
        try:
            cli_wizard.make_settings_file(SYSTEM_SETTINGS_FILE)
        except Exception:
            print("Something went wrong with settings file making!")
            sys.exit(1)

    # load database path

    # load macs for filtering

    # load and decrypt conncetion string

    sqliteDB = Sqlite_handler()
    jono = asyncio.Queue()
    luuppi = asyncio.get_event_loop()
    luuppi.create_task(sqliteDB.save_from_queue(jono, luuppi))

    if len(sys.argv)>1:
        rounds = int(sys.argv[1])
        luuppi.create_task(read_data_from_tags(macs, jono, rounds))
    else:
        luuppi.create_task(read_data_from_tags(macs, jono))
    
    luuppi.run_forever()

if __name__ == '__main__':
    main()