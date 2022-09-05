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
data_df["Month"] = data_df["date_1"].dt.month_name()
print(data_df)
#
# data_df["Month"] = data_df["Month"].map(
#     {"January": "Jan", "February": "Feb", "March": "Mar", "Aril": "Apr", "May": "May",
#      "June": "Jun", "July": "Jul", "August": "Aug", "September": "Sep",
#      "October": "Oct",
#      "November": "Nov", "December": "Dec"})
print(data_df["Month"])

# # Subplots
weather_1 = data_df[data_df["weather"] == 1]
# # print(weather_1)
weather_2 = data_df[data_df["weather"] == 2]
weather_3 = data_df[data_df["weather"] == 3]
weather_4 = data_df[data_df["weather"] == 4]
print(weather_4)
#
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True,
                                             sharey=True)  ## sharex and sharey are True x axis and y axis are share for all subplot.
ax1.plot(weather_1["Month"], weather_1["count"], "b+",alpha=0.3)
ax1.set_title("weather_1(clear)")

ax2.plot(weather_2["Month"], weather_2["count"], "b+",alpha=0.3)
ax2.set_title("weather_2(Mist)")

ax3.plot(weather_3["Month"], weather_3["count"], "b+",alpha=0.3)
ax3.set_title("weather_3(light rain)")

ax4.plot(weather_4["Month"], weather_4["count"], "b+",alpha=0.3)
ax4.set_title("weather_4(heavy rain)")

fig.supxlabel("Month")  # here we use fig.sup for giving common xlabel
fig.supylabel("number of total rentals (in 2 years)")
fig.suptitle("number of total rentals Vs Months with weathers")
plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\subplots_weather_Vs_month")
