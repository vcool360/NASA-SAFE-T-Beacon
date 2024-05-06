import asyncio
from bleak import BleakClient, BleakScanner


#the scanning process to confirm the heart monitor is detectable
async def BLEscan():
    print(f"BLEscan()")
    address = "D7:C6:FC:E2:57:6F"       #the MAC address of the PolarH10 monitor (replace as needed)
    print(f"Scanning...")
    device = await BleakScanner.find_device_by_address(address)     #search ONLY for the known heart monitor by its address
    if device == "None":        #if the heart monitor is not detected, retry
            asyncio.run(BLEscan())
    else:
            print(device)           #the device's naming information from discovery process
            print(f"Connected to heart monitor")



#the connection & data acquisition process
async def BLEconnect(address):
         async with BleakClient(address) as client:
                HEART_UUID = "00002a37-0000-1000-8000-00805f9b34fb"     #GATT UUID for BLE heart rate service
                print(f"BLEconnect()...")
                x = await client.is_connected()
                print(f"BleakClient initiated with {address}")
                svcs = await client.get_services()      #likely not necessary, but ensures that the device's services are gathered
                print(f"Services acquired...")

                #data acquisition loop
                while(True):
                        print(f"Data collection...")
                        await client.start_notify(HEART_UUID, notification_handler)     #heart rate information is NOTIFY only, so must subscribe to notifications
                        await asyncio.sleep(1.0)        #sleep statements just to allow plenty of time for BLE connection to finish processes between tasks
                        await client.stop_notify(HEART_UUID)
                        await asyncio.sleep(5.0)
                        print(f"\n\n")


#callback function to access the heart rate notification data array (index 1 is the heart rate)     //other indexes also accessible
def notification_handler(sender, data):
        print(f"Heart Rate: {data[1]}")


#the usage of the heart rate monitor is entirely possible (and indeed done so in the main program) without this function
#this function's purpose is to ensure a stable connection to the heart rate monitor without worrying about interoperability to the PyQt5 QEventLoop multithreading services
#this also allows for an easily documented method for testing the correct functionality of a heart rate monitor
def getHeartRate():
        address = "D7:C6:FC:E2:57:6F"
        #scan until Polar H10 found
        print(f"getHeartRate()")
        loop = asyncio.get_event_loop()     #async threading setup being taken care of for us
        print(f"event loop obtained")
        loop.run_until_complete(BLEscan())      #keep scanning for the heart rate monitor until successfully detected

        # loop heart rate collection
        while True:
                try:
                        loop = asyncio.get_event_loop()         #async threading handler (mumbo jumbo taken care of for us)
                        loop.run_until_complete(BLEconnect(address))        #keep running until complete (which is an infinite loop anyways)
                except Exception as e:      #debugging for any exceptions that may otherwise break the process
                        print(e)
                        pass


#Run this program test file with async threading taken care of for us
asyncio.run(getHeartRate())
