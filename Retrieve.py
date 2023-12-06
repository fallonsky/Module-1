import urllib.parse
import urllib.request
import json
import csv
import time
import matplotlib.pyplot as plt
import pandas as pd

#constants
API_KEY="NCF8XJDWE767RMKB22MN36U9Q"
UNIT_GROUP="us"


# method returns raw forcast data
def getWeatherForecast(loc, date):
         requestUrl = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + urllib.parse.quote_plus(loc)
         requestUrl = requestUrl+date+"?key="+API_KEY+"&unitGroup="+UNIT_GROUP+"&include=days";
         try:
                 req = urllib.request.urlopen(requestUrl)
         except:
                 print("Could not read from:"+requestUrl)
                 return []
         rawForecastData = req.read()
         req.close()
         return json.loads(rawForecastData)

# this checks to see if this entry already exists in the csv file
def hasData(date_clean):
    with open('Data_Appended.csv', 'r+', newline='') as f:
        line = csv.reader(f)

        try:   
            for i in line:
                if str(date_clean) == str(i[0]):
                    print("found record")
                    return True
        except:
            print("csv is empty")
            return False
    print("record not found")
    return False

# function to write a line into the csv
def write_line(data):
    with open('Data_Appended.csv', 'a', newline='') as f:
        file = csv.writer(f)
        file.writerow(data)


with open('Data.csv', 'rt') as f:
    line = csv.reader(f)
    for i in line:
        # for ease of use
        date = i[0]
        areacode = i[1]
        
        if not hasData(date):
            location= "Maryland," + str(areacode)    
            weatherForecast = getWeatherForecast(location, date)
            days = weatherForecast['days']
            for day in days:
                data = [i[0], i[1], day["tempmin"]]
                write_line(data)
                
print("done")










