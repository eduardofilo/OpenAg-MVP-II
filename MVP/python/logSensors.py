#Check sensors and log to file
from si7021 import *
from logData import logData
from getWaterTemp import YELLOW_DEVICE, WHITE_DEVICE, get_temp_sens

si=si7021()

try:
    temp = si.getTempC()
    if temp > 0:
        logData("si7921_top", "Success", "temperature", "{:10.1f}".format(temp), '')
    else:
        logData("si7921_top", "Failure (temp < 0)", "temperature", '', str(e))
except Exception as e:
        logData("si7921_top", "Failure", "temperature", '', str(e))

try:
    humid = si.getHumidity()
    logData("si7921_top", "Success", "humidity", "{:10.1f}".format(humid), '')
except Exception as e:
        logData("si7921_top", "Failure", "humidity", '', str(e))


# Reading water temp

## Yellow probe
try:
    yellowTemp = get_temp_sens(YELLOW_DEVICE)
    logData("ds18b20_yellow", "Success", "temp_yellow", "{:10.1f}".format(yellowTemp), '')
except Exception as e:
    logData("ds18b20_yellow", "Failure", "temp_yellow", '', str(e))

## White probe
try:
    whiteTemp = get_temp_sens(WHITE_DEVICE)
    logData("ds18b20_white", "Success", "temp_white", "{:10.1f}".format(whiteTemp), '')
except Exception as e:
    logData("ds18b20_white", "Failure", "temp_white", '', str(e))
