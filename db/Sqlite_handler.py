import sqlite3
if __name__ != '__main__':
    import db.datamodel as dm
import json
import asyncio

class Sqlite_handler:
    def __init__(self, database_address: str = './data/ble_station.db'):
        if __name__ != '__main__':
            self.database_address = database_address
        else: 
            self.database_address = './../data/ble_station.db'
        self.previous_seq_dictionary = {}
    
    def get_connection(self):
        connection = sqlite3.connect(self.database_address)
        return connection
    
    def create_tables(self):
        datamalli = json.loads(dm.datamodel)
        sql_merkkijono = ""
        for taulu in datamalli['tables']:
            sql_merkkijono += "CREATE TABLE IF NOT EXISTS "+taulu['name'] +" ("
            colsIndex=0
            
            for cols in taulu['columns']:
                pk = ""
                if cols['primary_key'] == True: pk = " PRIMARY KEY"
                sql_merkkijono += cols['name'] + " " + cols['type'] + pk
                if (colsIndex < len(taulu['columns'])-1):
                    sql_merkkijono += ", "
                colsIndex +=1
            sql_merkkijono += "); "
        #print(sql_merkkijono)
        
        con = self.get_connection()
        cursor = con.cursor()
        cursor.execute(sql_merkkijono)
        con.commit
        con.close()

    def save_data(self, data):
        sql_string = "INSERT INTO measurements (data_format, timestamp, humidity, temperature, pressure, acceleration, acceleration_x, acceleration_y, acceleration_z, tx_power, battery, movement_counter, measurement_sequence_number, mac, rssi) VALUES ("
        accel=data[1]['acceleration']
        accelx=data[1]['acceleration_x']
        accely=data[1]['acceleration_y']
        accelz=data[1]['acceleration_z']
        pressure = data[1]['pressure']
        if accel == None: accel = 0
        if accelx == None: accelx = 0
        if accely == None: accely = 0
        if accelz == None: accelz = 0
        if pressure == None: pressure = 0
        timestamp = data[1]['epoch_second']
        sql_string += f"{data[1]['data_format']},{timestamp},{data[1]['humidity']},{data[1]['temperature']},{pressure},{accel},{accelx},{accely},{accelz},{data[1]['tx_power']},{data[1]['battery']},{data[1]['movement_counter']},{data[1]['measurement_sequence_number']},'{data[1]['mac']}',{data[1]['rssi']});"
        con = self.get_connection()
        cur = con.cursor()
        cur.execute(sql_string)
        con.commit()
        con.close()

    async def save_from_queue(self, queue, luuppi):
        while True:
            data = await queue.get()

            if data is None:
                luuppi.stop()
                print('luuppi stop')
                break

            if self.check_previous_measurement_seq(data[1]['mac'], data[1]['measurement_sequence_number']):
                continue

            self.save_data(data)
    
    def check_previous_measurement_seq(self, mac, sequence_num):
        if mac in self.previous_seq_dictionary:
            if sequence_num == self.previous_seq_dictionary[mac]:
                return True
            else:
                self.previous_seq_dictionary[mac] = sequence_num
                return False
        else:
            self.previous_seq_dictionary[mac] = sequence_num
            return False
    
if __name__ == '__main__':
    import datamodel as dm
    sqlitehandler = Sqlite_handler()
    # connection = sqlitehandler.get_connection()
    # connection.close()
    sqlitehandler.create_tables()