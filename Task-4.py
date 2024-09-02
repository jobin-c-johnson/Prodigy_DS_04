import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from collections import Counter

columns={'deviceCode_deviceCode':'DeviceCode',
        'deviceCode_location_latitude':'Latitude',
        'deviceCode_location_longitude' : 'Longitude',
        'deviceCode_location_wardName':'WardName',
        'deviceCode_pyld_alarmType':'AlarmType',
        'deviceCode_pyld_speed':'Speed',
        'deviceCode_time_recordedTime_$date':'RecordedDateTime'}
df = pd.read_csv(r"C:\Users\ASUS\Downloads\bangalore-cas-alerts.csv\bangalore-cas-alerts.csv")
df.rename(columns=columns,inplace=True)
# print(df.head(30))
width=.5
plt.figure(figsize=(10,16))

#  ***Graph-1***
plt.subplot(2,2,2)
df['WardName']=df['WardName'].replace({'other':'Other'})
wards = df['WardName'].value_counts()
# print(wards)
bars = plt.barh(wards.index[1:11],wards.values[1:11],width,color='purple')
for bar in bars:
    # yval = bar.get_height()
    # plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
      xval = bar.get_width()  # Get the width of the bar
      yval = bar.get_y() + bar.get_height() / 2  # Get the y position of the bar and add half of its height
      plt.text(xval, yval, int(xval), ha='center', va='center')
# plt.xlabel("WardName")
# plt.ylabel("Accident rate")
plt.title("Most Accident Occurrence Ward in Bangalore")
# plt.xticks(rotation=70)

#  ***Graph-2***
plt.subplot(2,2,3)
bars = plt.barh(wards.index[-10:],wards.values[-10:],width,color='Purple')
for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
      xval = bar.get_width()  # Get the width of the bar
      yval = bar.get_y() + bar.get_height() / 2  # Get the y position of the bar and add half of its height
      plt.text(xval+0.3, yval, int(xval), ha='center', va='center')
# plt.xlabel("WardName")
# plt.ylabel("Accident rate")
plt.title("Least Accident Occrrence Ward in Bangalore")
# plt.xticks(rotation=70)

# df['RecordedDateTime'] = df['RecordedDateTime'].map(lambda x : pd.Timestamp(x, tz='Asia/Kolkata'))
df['RecordedDateTime'] = pd.to_datetime(df['RecordedDateTime'], errors='coerce').dt.tz_convert('Asia/Kolkata')
month = df['RecordedDateTime'].dt.month_name().tolist()

# print(Counter(month))

plt.subplot(2,2,1)
plt.pie(Counter(month).values(),labels=['July','March','April','February','June'],autopct='%1.1f%%',startangle=90)
plt.title("Most Accident Occurence Month")

plt.subplot(2,2,4)
altype= df['AlarmType'].value_counts()
# print(altype)
plt.bar(altype.index,altype.values)
plt.title('Alarm Type')
plt.show()