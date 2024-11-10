import asyncio
import time
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from ruuvitag_sensor.adapters import get_ble_adapter, throw_if_not_async_adapter
from multiprocessing import Manager

ble = get_ble_adapter()
seconds_to_scan = 180

async def find_ruuvitags_async(bt_device: str = ""):
        """
        CLI helper function.

        Find all RuuviTags. Function will print the MAC and the state of the sensors when found.
        Function will execute as long as it is stopped. Stop execution with Ctrl+C.

        Returns:
            dict: MAC and state of found sensors
        """
        throw_if_not_async_adapter(ble)

        print("Finding RuuviTags. Will listen BLE messages for few minutes.")

        data = {}
        mac_blacklist = Manager().list()
        data_iter = ble.get_data(mac_blacklist, bt_device)

        start_time = int(time.time())
        time_to_end = start_time + seconds_to_scan


        async for new_data in data_iter:
            if int(time.time()) > time_to_end: break
            if new_data[0] in data:
                continue

            parsed_data = RuuviTagSensor._parse_data(new_data, mac_blacklist)
            if parsed_data:
                data[new_data[0]] = parsed_data
                print(new_data[0])
                print(parsed_data)


        return data

if __name__ == '__main__':
     daatta = asyncio.get_event_loop().run_until_complete(find_ruuvitags_async())
     print(daatta)