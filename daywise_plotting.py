import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\admin\Downloads\train_1.csv")
print(df)
print(df.dtypes)
df1 = df.copy()
df2 = df1.datetime.str.split(expand=True)
df2.columns = ["date", "time"]
df2.index = df1.index
data_df = pd.concat([df2, df1], axis=1)
data_df.drop('datetime', inplace=True, axis=1)
print(type(data_df))  # here type of data_df["date"] is string
data_df["date_1"] = pd.to_datetime(data_df["date"])  ##so it is converted into date time formate
data_df["Day"] = data_df["date_1"].dt.day_name()
print(data_df)

data_df["Day"] = data_df["Day"].map({"Sunday": "Sun", "Monday": "Mon", "Tuesday": "Tue", "Wednesday": "Wed",
                                     "Thursday": "Thur", "Friday": "Fri", "Saturday": "Sat"})
print(data_df["Day"])

# Subplots of weather
weather_1 = data_df[data_df["weather"] == 1]
# print(weather_1)
weather_2 = data_df[data_df["weather"] == 2]
# print(weather_2)
weather_3 = data_df[data_df["weather"] == 3]
# print(weather_3)
weather_4 = data_df[data_df["weather"] == 4]
# print(weather_4)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True,sharey=True)  ## sharex and sharey are True x axis and y axis are share for all subplot.
ax1.plot(weather_1["Day"], weather_1["count"], "b+", alpha=0.3,label="clear")
ax1.set_title("weather_1(clear)")
# #
ax2.plot(weather_2["Day"], weather_2["count"], "b+", alpha=0.3,label="Mist")
ax2.set_title("weather_2(Mist)")
# #
ax3.plot(weather_3["Day"], weather_3["count"], "b+", alpha=0.3,label="light rain")
ax3.set_title("weather_3(light rain,snow)")
# #
ax4.plot(weather_4["Day"], weather_4["count"], "b+", alpha=0.3,label="heavy rain")
ax4.set_title("weather_4(heavy rain)")
fig.supxlabel("Days")  # here we use fig.sup for giving common xlabel
fig.supylabel("number of total rentals (in 2 years)")
fig.suptitle("number of to/tal rentals Vs Days with weathers")
# plt.legend(handles=[ax1,ax2,ax3,ax4],loc="upper right")
plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\subplots_weather_Vs_Days")

## subplots of weather with holiday

weather_1 = data_df[data_df["weather"] == 1]  ## here weather_1 is dataframe
# print(weather_1)
weather_2 = data_df[data_df["weather"] == 2]
weather_3 = data_df[data_df["weather"] == 3]
weather_4 = data_df[data_df["weather"] == 4]
# print(weather_4)
colour_map = {0: "blue",
              1: "red"}

colours_1 = weather_1["holiday"].apply(lambda x: colour_map[x])
colours_2 = weather_2["holiday"].apply(lambda x: colour_map[x])
colours_3 = weather_3["holiday"].apply(lambda x: colour_map[x])
colours_4 = weather_4["holiday"].apply(lambda x: colour_map[x])

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True,
                                             sharey=True)  ## sharex and sharey are True x axis and y axis are share for all subplot.

ax1.scatter(weather_1["Day"], weather_1["count"], marker="+", c=colours_1, alpha=0.3)
ax1.set_title("weather_1(clear) & holiday")

ax2.scatter(weather_2["Day"], weather_2["count"], marker="+", c=colours_2, alpha=0.3)
ax2.set_title("weather_2(Mist)& holiday")

ax3.scatter(weather_3["Day"], weather_3["count"], marker="+", c=colours_3, alpha=0.3)
ax3.set_title("weather_3(light rain) & holiday")

ax4.scatter(weather_4["Day"], weather_4["count"], marker="+", c=colours,alpha=0.3)
ax4.set_title("weather_4(heavy rain) & holiday")

fig.supxlabel("Days")  # here we use fig.sup for giving common xlabel
fig.supylabel("number of total rentals (in 2 years)")
fig.suptitle("number of total rentals Vs Days with weather and holiday")
plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\subplot_weather_Vs_Days_with_holiday")
