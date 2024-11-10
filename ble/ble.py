import asyncio
import os, time
os.environ["RUUVI_BLE_ADAPTER"] = "bleak"
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
import ruuvitag_sensor.log

ruuvitag_sensor.log.enable_console()

def find_sensors():
    RuuviTagSensor.find_ruuvitags()

async def read_data_from_tags(macs:list, jono:asyncio.Queue, rounds:int=0):

    if rounds>0:
        datacounter = 1

    async for found_data in RuuviTagSensor.get_data_async(macs):
        if rounds>0:
            if datacounter > rounds:
                jono.put_nowait(None)
                break

        # Stick measurements to the queue
        try:
            found_data[1]['epoch_second'] = int(time.time())
            jono.put_nowait(found_data)
        except asyncio.QueueFull:
            print('Queue full.')

        if rounds>0:
            datacounter += 1