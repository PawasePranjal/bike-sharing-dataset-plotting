import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


train_df = pd.read_csv("C:/Users/admin/Downloads/train.csv")
print(train_df)
# print(type(train_df))
train_df['holiday'] = train_df['holiday'].replace({0: 'not holiday',1: 'holiday'})
train_df['workingday'] = train_df['workingday'].replace({0: 'either weekend or holiday',1: 'workingday'})
train_df['season'] = train_df['season'].map({1: 'Spring',
                                             2: 'Summer',
                                             3: 'Fall',
                                             4: 'Winter'})

train_df['weather'] = train_df['weather'].map({1: 'Clear',
                                               2: 'Mist',
                                               3: 'Light Snow, Rain',
                                               4: 'Heavy Rain, Snow, Fog'})
# print(train_df['weather'])
##dataframe is convert numpy array
# train = train_df.to_numpy()
# print(train)

# plt.bar(train_df["weather"], train_df["count"])
plt.xlabel("weather")
plt.ylabel("number of total rentals (in 2 years)")
plt.title("number of total rentals vs weather")
plt.show()


##Quest 2



# ##Quest 3
# plt.bar(train_df[3],train_df[12])
# plt.xlabel("holidays")
# plt.ylabel("number of total rentals")
# plt.title("number of total rentals vs holiday")
# # plt.show()
# #
# plt.bar(train_df[4],train_df[12])
# plt.xlabel("workingdays")
# plt.ylabel("number of total rentals")
# plt.title('number of total rental vs workingdays')
# plt.show()

# fig,ax=plt.subplots()
# plt.plot(season,count)
# plt.plot(holiday,count)
# plt.show()

