# -*- coding: utf-8 -*-

YELLOW_DEVICE = "/sys/bus/w1/devices/28-02129177fa36/w1_slave"
WHITE_DEVICE = "/sys/bus/w1/devices/28-020d9177c739/w1_slave"

def get_temp_sens(device):
        tfile = open(device)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return float(temperature)

#Uncomment to test this function
#print(str(get_temp_sens(YELLOW_DEVICE)) + " ºC")
