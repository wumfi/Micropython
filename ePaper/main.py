from functions import *
from machine import lightsleep, sleep, RTC
sleepytime=300 * 1000
global epd
epd = Eink(rotation=270, cs_pin=36, dc_pin=14, reset_pin=8, busy_pin=9)
global wifi

def WifiConnect():
    global wifi
    
    print("In the connect routine")
    wifi = WLAN(STA_IF)
    wifi.active(False)
    sleep(1000)
    wifi.active(True)
    if not wifi.isconnected():
        print('connecting to network...')
        wifi.connect(ssid, pwd)
        while not wifi.isconnected():
            pass

while True:
    global wifi
    WifiConnect()
    settime()
    UpdateEPD(epd)
    sleep(sleepytime)

#Leaving this here for debug/testing
# ConnectToWifi()
# debug("Updating screen")
# UpdateEPD(epd)
# ShutdownWifi()