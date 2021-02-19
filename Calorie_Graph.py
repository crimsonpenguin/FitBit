#!/usr/bin/python3

access_token = "ACCESS-TOKEN-GENERATED-FOR-USER"

import requests
import json 
from matplotlib import pyplot as plt, ticker
from datetime import datetime as dt, timedelta

endDate = (dt.now()-(timedelta(weeks=12))).strftime("%Y-%m-%d")
yesterday = (dt.now()-(timedelta(days=1))).strftime("%Y-%m-%d")

base_url = "https://api.fitbit.com/1/user/-/"
food = "foods/log/caloriesIn/date/"+yesterday+"/"+endDate+".json"
url = base_url+food
headers = {'Authorization' : 'Bearer {}'.format(access_token)} 
response = requests.get(url,headers=headers).json()

xAxis,yAxis = [],[]
for i in response["foods-log-caloriesIn"]:
	xAxis.append(i["dateTime"])
	yAxis.append(int(i["value"]))

fig, ax = plt.subplots()
ax.plot(xAxis,yAxis)
myLocator = ticker.MultipleLocator(5)
ax.xaxis.set_major_locator(myLocator)
fig.autofmt_xdate()
plt.xlabel("Date")
plt.ylabel("Calories")
plt.title('Calories Consumed per day between '+endDate+" & "+yesterday)
plt.show()
	
