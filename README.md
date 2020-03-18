# WAAPS

WX ARDUINO APRX PYTHON SCRIPT

WAAPS is a simple weather station project for APRX

# v.1.0
First release.

## HARDWARE
1. Arduino Nano
2. BME280
3. will see later...

## Instruction
1. Load waaps.ino file to arduino nano
2. Connect BME280 to 3,3V GND and SCL -> A5, SDA -> A4
3. Connect arduino using USB to the raspberry Pi
4. Upload wx.py to /home/pi directory
5. Set wx.py executable (sudo chmod +x wx.py)
6. Edit and setup wx.py (lat,lon,com port)
7. Setup beacon exec on APRX config file
