import csv
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def write_line(data):
    with open('Data2.csv', 'a', newline='') as f:
        file = csv.writer(f)
        file.writerow(data)

size = 364
current = 0
first = True
tempList = []


df = pd.read_csv("Data_Appended.csv")
df = df.drop(df.columns[[0,1]], axis=1)



with open('Data_Appended.csv', 'rt') as f:
    line = csv.reader(f)
    for i in line:

        if first:
            first = False
            continue
        
        date = i[0]
        areacode = i[1]
        temp = i[2]

        if current < size:
            delta = df.iloc[current]['temp'] - df.iloc[current + 1]['temp']
        elif current == size:
            delta = df.iloc[current]['temp'] - df.iloc[0]['temp']

        
        current = current + 1
        if delta < 0:
            delta = delta * -1

        tempList.append(round(delta,2))
        data = [date, areacode, temp, delta]
        write_line(data)

tempList.sort()
buffer = Counter(tempList)
print(buffer)
print(type(buffer))
df2 = pd.DataFrame.from_dict(buffer, orient='index')
print(df2)
print("done")


ax = plt.gca() 
df2.plot(kind='line', 
        y=0, 
        color='green',
        ax=ax,
        legend=False) 
  
# set the title 
plt.title('') 
  
# show the plot 
plt.show() 
