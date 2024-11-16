from setup_ble_station.settings_load import settings_from_file
from tags import macs
from db.Sqlite_handler import Sqlite_handler

settings = settings_from_file("./settings.json")
macs_from_file: list = settings["ruuviTags"]["macs"]

addition = ""
macsLength = len(macs_from_file)
i = 0
for macF in macs_from_file:
    macFlower = macF.lower()
    macFlowerWithoutColons = macFlower.replace(":", "")
    name_of_ruuvi = macs[macFlowerWithoutColons]
    addition += f"('{macF}', '{macFlowerWithoutColons}', '{name_of_ruuvi}', 1)"
    i+=1
    if (i < macsLength):
        addition +=", "
sql_string: str = "INSERT INTO macs(mac, mac_lower_case, nimi, recorded) VALUES " + addition

db = Sqlite_handler()
conn = db.get_connection()
cursor = conn.cursor()
cursor.execute(sql_string)
conn.commit()