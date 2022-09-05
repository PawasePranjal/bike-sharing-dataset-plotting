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
data_df["time_split"] = data_df["time"].str.split(':').str[0]

data_df['time_1'] = pd.to_numeric(data_df['time_split'])  ##here in time_1 coloumn contain all hour values.
# print(data_df.dtypes)  # here type is integer
print(data_df)

data_df['holiday'] = data_df['holiday'].replace({0: 'holiday', 1: 'not holiday'})
# data_df['weather'] = data_df['weather'].map({1: 'Clear',
#                                           2: 'Mist',
#                                           3: 'Light Snow,Rain',
#                                           4: 'Heavy Rain,Snow,Fog'})

# colour_map = {1: "red",
#               2: "green",
#               3: "blue",
#               4: "black"}
#
# colours = data_df["weather"].apply(lambda x: colour_map[x])
# print(colours)
#
# plt.xlabel("time (in hours)")
# plt.ylabel("number of total rentals (in 2 years)")
# plt.title("number of total rentals Vs Time")
# plt.scatter(data_df["time_1"], data_df["count"], marker="+", c=colours, alpha=0.3)
# # plt.show()
# plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\weather_Vs_hours")


#Subplots of weatherwise.
# weather_1 = data_df[data_df["weather"] == 1]
# # # print(weather_1)
# weather_2 = data_df[data_df["weather"] == 2]
# weather_3 = data_df[data_df["weather"] == 3]
# weather_4 = data_df[data_df["weather"] == 4]
# print(weather_4)
#
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True,
#        sharey=True)  ## sharex and sharey are True x axis and y axis are share for all subplot.
# ax1.plot(weather_1["time_1"], weather_1["count"], "g+")
# ax2.plot(weather_2["time_1"], weather_2["count"], "g+")
# ax3.plot(weather_3["time_1"], weather_3["count"], "g+")
# ax4.plot(weather_4["time_1"], weather_4["count"], "g+")
# fig.supxlabel("time (in hours)")  # here we use fig.sup for giving common xlabel# fig.suptitle("number of total rentals Vs Time with weather")
# fig.supylabel("number of total rentals (in 2 years)")
# fig.suptitle("number of total rentals Vs Time with weather")
# plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\subplot_weather_Vs_hours")

#Subplots of workingdays.
# weekend = data_df[data_df["workingday"] == 1]
# workingday = data_df[data_df["workingday"] == 0]
# fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
# ax1.plot(weekend["time_1"], weekend["count"], "g+")
# ax1.set_title("weekend")
# ax2.plot(workingday["time_1"], workingday["count"], "r+")
# ax2.set_title("workingday")
# fig.supxlabel("time (in hours)")  # here we use fig.sup for giving common xlabel
# fig.supylabel("number of total rentals (in 2 years)")
# fig.suptitle("number of total rentals Vs Time with workingday")
# plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\subplot_workingday_Vs_hours")



# #plots of workingday with weekend.
# weekend = data_df[data_df["workingday"] == 1]
# print(weekend["workingday"])
# workingday = data_df[data_df["workingday"] == 0]
# plt.plot(weekend["time_1"], weekend["count"], "g+")
# plt.plot(workingday["time_1"], workingday["count"], "r+")
# plt.xlabel("time (in hours)")
# plt.ylabel("number of total rentals (in 2 years)")
# plt.title("number of total rental Vs time with holiday and weekend")
# plt.savefig(r"D:\code\Bike_sharing_dataset_plotting\workingday_Vs_hours")
