import pandas as pd
data = pd.read_csv("olimpiyatlar.csv")
data_head = data.head(15)
# data.info()

#sutun isimlerinde duzenlenme
column = data.columns
data.rename(columns = {
"ID" : "id",             
"Name" : "name",
"Sex" : "cinsiyet",
"Age" : "yas",
"Height" : "boy",
"Weight" : "kilo",
"Team" : "takim",
"NOC" : "noc",
"Games" : "oyunlar",
"Year" : "yil",
"Season" : "sezon",
"City" : "sehir",
"Sport" : "spor",
"Event" : "etkinlik",
"Medal" : "madalya"
}, inplace = True)
# print(data.head())


#gereksiz verilerin cikarilmasi
data = data.drop(["id", "oyunlar"], axis = 1)
data_duplicated = data[data.duplicated()]
# print(data_duplicated)


# ortalama ve medyan
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
plt.hist(data.boy)
plt.figure()
plt.hist(data.kilo)
# plt.show()
describe = data.describe()
# print(describe)


#boy ve kilo sutununda bulunan event ortalamasi
unique_event = pd.unique(data.etkinlik)
# print(unique_event)

data_change = data.copy() #copied data to change
height_weight_list = ["boy", "kilo"] #kayip veri olan sutunlar

for e in unique_event: #etkinlik ozelinde iterasyona baslandi
  #event filter create
  event_filter = data_change.etkinlik == e  # Corrected column name
  #filtered data to event
  data_filtered = data_change[event_filter]
  
  #height and weight average
  for s in height_weight_list:
      average = np.mean(data_filtered[s])
      
      if not np.isnan(average) == False:
          data_filtered[s] = data_filtered[s].fillna(average)
      else:
          data_average = np.mean(data[s])
          data_filtered[s] = data_filtered[s].fillna(data_average)
        
  data_change.loc[event_filter, height_weight_list] = data_filtered[height_weight_list]  # Ensure changes are applied back to data_change

data.info()
print(data.info())
  
# event_filter = data_change.etkinlik == "Athletics Women's 400 metres"  # Corrected column name
# data_filtered = data_change[event_filter]

# average = np.mean(data_filtered["boy"])
# data_filtered["boy"] = data_filtered["boy"].fillna(average)