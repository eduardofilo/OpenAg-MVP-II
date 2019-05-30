import pygal
import requests
import json
import pytz
import datetime
from datetime import timezone

#Use a view in CouchDB to get the data
#use the first key for attribute type
#order descending so when limit the results will get the latest at the top

def getYellowTempChart():
    r = requests.get('http://127.0.0.1:5984/mvp_sensor_data/_design/doc/_view/attribute_value?startkey=["temp_yellow",{}]&endkey=["temp_yellow"]&descending=true&limit=144')
    #print r

    v_lst = [float(x['value']['value']) for x in r.json()['rows']]
    ts_lst = [x['value']['timestamp'] for x in r.json()['rows']]
    local_tz = pytz.timezone('Europe/Madrid')

    line_chart = pygal.Line()
    line_chart.title = 'Temperature'
    line_chart.y_title="Degrees C"
    line_chart.x_title="Timestamp (hover over to display date)"
    #need to reverse order to go from earliest to latest
    ts_lst.reverse()
    line_chart.x_labels = map(lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc).astimezone(local_tz).strftime('%Y-%m-%d %H:%M:%S'), ts_lst)
    #need to reverse order to go from earliest to latest
    v_lst.reverse()
    line_chart.add('Yellow Tank Temp', v_lst)
    line_chart.render_to_file('/home/pi/MVP/web/temp_yellow_chart.svg')

getYellowTempChart()
