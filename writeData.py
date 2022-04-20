import time
import requests

URL = "http://54.82.10.179:8080/addData"

file_name_template = 'detail-records/detail_record_2017_01_{day}_08_00_00'

# monitor table columns
columns = ['driverID', 'carPlateNumber', 'Latitude', 'Longtitude', 'Speed', \
    'Direction', 'siteName', 'Time', 'isRapidlySpeedup', 'isRapidlySlowdown', \
    'isNeutralSlide','isNeutralSlideFinished', 'neutralSlideTime', 'isOverspeed',\
    'isOverspeedFinished', 'overspeedTime', 'isFatigueDriving', 'isHthrottleStop', 'isOilLeak']

# load and send data
for i in range(2,13):
    if i < 10:
        day = "0" + str(i)
    else:
        day = str(i)
    file = open(file_name_template.format(day=day), "r", encoding="utf-8")
    for line in file:
        # format data
        line = line.strip("\n") + ","
        data = {}
        j = 0
        while len(line) > 0:
            try:
                end = line.index(',')
                data[columns[j]] = line[:end]
                line = line[end+1:]
                j+=1
            except:
                break
        # remove empty columns
        data = dict( [(k,v) for k,v in data.items() if len(v)>0])
        result = requests.post(URL, json = data)
        print(result.text)
        time.sleep(1)
        
        
