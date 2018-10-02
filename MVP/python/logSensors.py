#Check sensors and log to file
from si7021 import *
from logData import logData
from getWaterTemp import YELLOW_DEVICE, WHITE_DEVICE, get_temp_sens

si=si7021()

try:
    temp = si.getTempC()
    logData("si7921_top", "Success", "temperature", "{:10.1f}".format(temp), '')
except Exception as e:
        logData("si7921_top", "Failure", "temperature", '', str(e))

try:
    humid = si.getHumidity()
    logData("si7021_top", "Success", "humidity", "{:10.1f}".format(humid), '')
except Exception as e:
        logData("si7921_top", "Failure", "humidity", '', str(e))


# Reading water temp

## Yellow probe
try:
    yellowTemp = get_temp_sens(YELLOW_DEVICE)
    logData("yellow_probe", "Success", "temperature", "{:10.1f}".format(yellowTemp), '')
except Exception as e:
    logData("yellow_probe", "Failure", "temperature", '', str(e))

## White probe
try:
    whiteTemp = get_temp_sens(WHITE_DEVICE)
    logData("white_probe", "Success", "temperature", "{:10.1f}".format(whiteTemp), '')
except Exception as e:
    logData("white_probe", "Failure", "temperature", '', str(e))
