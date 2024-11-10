# ruuviTagsHomeProject
Raspberry Pi BLE station for RuuviTags

This is a personal spin off project. Goal is a smoothly running service for Raspberry Pi computer that records RuuviTag measurement data send via Bluetooth Low Energy advertisement packages. To easily fetch data another goal is a simple REST API to use for data downloading from the database.

## Tech stack

Raspbian, Python 3.11, SQLite3, REST API, JSON, ruuvitag-sensor, flask, (bleak in linux)

## Requirements

To satisfy requirements you can use the requirements.txt
`pip install -r requirements.txt`

## Running the program

`python3 Main.py` or `py Main.py`

Database setup is not automated yet. You'll need to make directory named "data" in the root directory of this application. After that you will need to run Sqlite_handler.py as a script:
```
cd db
python3 Sqlite_handler.py
cd ..
```
It creates "data/ble_station.db" file. Automating setup is on the way.

### As a systemd service

In testing Raspberry Pi I have used 10 second delay before starting to make sure that the service starts. More investigation is to be done on this to find out at what target would be a good place to time the startup so that program runs correctly.