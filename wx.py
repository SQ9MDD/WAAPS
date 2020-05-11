#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WX ARDUINO APRX PYTHON SCRIPT (WAAPS)
# SQ9MDD@2020 released under GPL.v.2
# http://sq9mdd.qrz.pl
#
# weather frame with position without time structure
# ramka pogodowa z pozycja bez czasu

#   !               - required      identifier
#   5215.01N        - required      latitude
#   /               - required      symbol table
#   02055.58E       - required      longtitude
#   _               - required      icon (must be WX)
#   ...             - required      wind direction (from 0-360) if no data set: "..."         
#   /               - required      separator
#   ...             - required      wind speed (average last 1 minute) if no data set: "..."          
#   g...            - required      wind gust (max from last 5 mins) if no data set: "g..." 
#   t030            - required      temperature in fahrenheit    
#   r000            - option        rain xxx
#   p000            - option        rain xxx
#   P000            - option        rain xxx  
#   h00             - option        relative humidity (00 means 100%Rh)     
#   b10218          - option        atmosferic pressure in hPa multiple 10  
#   Fxxxx           - option        water level above or below flood stage see: http://aprs.org/aprs12/weather-new.txt
#   V138            - option        battery volts in tenths   128 would mean 12.8 volts
#   Xxxx            - option        radiation lvl
#
# temp z sieci APRSjest w fahrenheit przeliczanie na C =(F-32)/9*5
# temp w celsjusz do sieci APRS trzeba wyslac jako fahrenheit F = (C*9/5)+32
#
# temp z sieci APRSjest w fahrenheit przeliczanie na C =(F-32)/9*5
# temp w celsjusz do sieci APRS trzeba wyslac jako fahrenheit F = (C*9/5)+32
# model      returns
# WAAPS300 - WAAPS300*20.00*1010.10*99
# TODO:
#       - wind speed, gust and direction (under developing)
#       - rain gauge

################################### CONFIGURATION #######################################################
#                                                                                                   	#
wx_lat      	        = '5215.01N'                     	# coordinates APRS format           	    #
wx_lon      	        = '02055.58E'                    	# coordinates APRS format           	    #
wx_altitude             = '125'                             # meeters above sea lvl                     #
wx_comment  	        = 'WAAPS300 WX station on tests'   	# beacon comment		                    #
wx_err_comment 	        = 'No WX data'				        # comment when no data avaiable		        #
ardu_wx_modell          = 'WAAPS300'                        # WAAPS300 - basic modell Temp.Rh.Baro      #
ardu_wx_seriall         = 'COM17'                           # Where your WX is connected to             #
ardu_wx_speed           = 9600                              # Serial port speed                         #
#										      	                                                        #
######################## DO NOTE EDIT BELLOW THIS LINE ##################################################

import serial
#from serial import Serial
ser = serial.Serial(ardu_wx_seriall, ardu_wx_speed, timeout=1)

modell = ''
tempC = 0.0
baro = 0.0
humi = 0

# wind direction currently not supported
def wind_direction():
    return('...')

# wind speed currently not supported
def wind_speed():
    return('...')

# wind gust currently not supported
def wind_gust():
    return('g...')

def outside_temp():
    temp_fahrenheit = int(round((data_tempC*9/5)+32))
    if(temp_fahrenheit < 100):
        zero = '0'
    else:
        zero = ''
    return('t' + zero + str(temp_fahrenheit))

# rain 1h period currently not supported
def rain_1h():
    return('')

# rain 24h period currently not supported
def rain_24h():
    return('')

# rain after midnight period currently not supported
def rain_midnight():
    return('')

def humi():
    humi = int(round(data_humi))
    if(humi == 100):
        humi = '00'
    return('h' + str(humi))

def baro():
    hPa_offset = float(wx_altitude) * 0.10933
    baro = int(round((data_baro + hPa_offset)*10))
    if(baro < 10000):
        zero = '0'
    else:
        zero = ''
    return('b' + zero + str(baro))

# make WX data
def wx_data():
    outside_temp_label = outside_temp()
    return('!' + str(wx_lat) + '/' + str(wx_lon) + '_' + str(wind_direction()) + '/' + str(wind_speed()) + str(wind_gust()) + str(outside_temp()) + str(rain_1h()) + str(rain_24h()) + str(rain_midnight()) + str(humi()) + str(baro()) + 'laDu' + ' ' + str(wx_comment))

while True:
    reading = ser.readline()
    if(reading):
        data = reading.split("*")
        data_modell = data[0]
        data_tempC = float(data[1])
        data_baro = float(data[2])
        data_humi = float(data[3])
        print wx_data()
        exit()
