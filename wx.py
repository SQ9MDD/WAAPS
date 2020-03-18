#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WX ARDUINO APRX PYTHON SCRIPT (WAAPS)
# SQ9MDD@2020 released under GPL.v.2
# http://sq9mdd.qrz.pl
#
# ramka pogodowa bez pozycji z czasem
# _mm dd gg mm                temp hum  baro
# _03 29 06 58 c025 s009 g008 t030 r000 p000 P000 h00 b10218
#
# ramka pogodowa z pozycja bez czasu
#                        _                temp hum  baro
# ! 5215.01N / 02055.58E _ ... / ... g... t030 r000 p000 P000 h00 b10218
#
# temp z sieci APRSjest w fahrenheit przeliczanie na C =(F-32)/9*5
# temp w celsjusz do sieci APRS trzeba wyslac jako fahrenheit F = (C*9/5)+32
# model      returns
# WAAPS300 - WAAPS300*20.00*1010.10*99

################################### CONFIGURATION #######################################################
#                                                                                                   	#
wx_lat      	        = '5215.01N'                     	# coordinates APRS format           	#
wx_lon      	        = '02055.58E'                    	# coordinates APRS format           	#
wx_comment  	        = 'WAAPS300 WX station on tests'   	# beacon comment		        #
wx_err_comment 	        = 'No WX data'				# comment when no data avaiable		#
ardu_wx_modell          = 'WAAPS300'                        	# WAAPS300 - basic modell Temp.Rh.Baro  #
ardu_wx_seriall         = '/dev/ttyUSB0'                        # Where your WX is connected to         #
ardu_wx_speed           = 9600                              	# Serial port speed                     #
#										      	                #
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
    return(humi)

def baro():
    baro = int(round(data_baro))
    if(baro < 10000):
        zero = '0'
    else:
        zero = ''
    return('b' + zero + str(baro))

# make WX data
def wx_data():
    outside_temp_label = outside_temp()
    return('!' + str(wx_lat) + '/' + str(wx_lon) + '_' + str(wind_direction()) + '/' + str(wind_speed()) + str(wind_gust()) + str(outside_temp()) + str(rain_1h()) + str(rain_24h()) + str(rain_midnight()) + str(humi()) + str(baro()) + ' ' + str(wx_comment))

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
