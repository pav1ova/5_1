import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import matplotlib.dates
from matplotlib.ticker import MaxNLocator


url = 'https://mfd.ru/currency/?currency=USD'
r = requests.get(url)
#print(r.text)
soup = BeautifulSoup(r.text, 'lxml')

table= soup.find(class_='mfd-content-container').find('table')
headers=[]
for i in table.find_all('tr'):
    data=i.text
    headers.append(data)
df = pd.DataFrame( columns = headers)
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(df)
    #print(row)

    x_list = (row[1])
    y_list = row[0]
    key = y_list.replace('с ', '')
    value = x_list
    list1 = [key, value]
    #print(list1)
    value_list = []
    value_list = float(value)
key_list = int(key)

x = []
y = []
for i in key:
    x.append(float(key_list[i]))
for d in value_list:
    y.append(value_list[d])
flg, ax = plt.subplots()

ax.plot(x,y);
ax.set(title='Курс доллара к рублю', xlabel='Дата', ylabel='Курс')
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.grid(True)
plt.show()



       