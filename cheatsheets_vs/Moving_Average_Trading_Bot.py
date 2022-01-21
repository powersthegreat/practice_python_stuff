#simple moving average trading stradegy to generate buy and sell signals
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#loading in the csv file for given stock
#search through python notes and find csv from excel to use


#storing the data
#input csv name in brackets
df = pd.read_csv("AAPL.csv")
#set the data as the index
df = df.set_index(pd.DatetimeIndex(df['Date'].values))
#showing the data
df 

#visually show the close price
plt.figure(figsize=(16,8))
plt.title("Close Price History", fontsize = 18)
plt.plot(df['Close'])
plt.xlabel("Date", fontsize = 18)
plt.ylabel("Close Price", fontsize = 18)

#create a function to calculate the simple moving average (SMA)
def SMA(data, period = 30, column = 'Close'):
    return data[column].rolling(window=period).mean()

#create two columns to store the 20day and 50day simple moving average
df['SMA20'] = SMA(df, 20)
df['SMA50'] = SMA(df, 50)

#get the buy and sell signals
#creating new column called signal, 1 is when SMA crosses, 0 is when it doesn't
df['Signal'] = np.where(df["SMA20"] > df["SMA50"], 1, 0)
#getting the signal from signals and finding the difference
df['Position'] = df['Signal'].diff
df['Buy'] = np.where(df['Position'] == 1, df["Close"], np.NAN)
df['Sell'] = np.where(df['Position'] == -1, df["Close"], np.NAN)

#visually show the close price with the SMAs and the buy and sell signals
plt.figure(figsize=(16,8))
plt.title("Close Price History with Signals", fontsize = 18)
plt.plot(df['Close'], alpha = 0.5, label = "Close")
plt.plot(df['SMA20'], alpha = 0.5, label = "SMA20")
plt.plot(df['SMA50'], alpha = 0.5, label = "SMA50")
plt.scatter(df.index, df["Buy"], alpha = 1, label = "Buy Signal", marker = "^", color = "green")
plt.scatter(df.index, df["Sell"], alpha = 1, label = "Sell Signal", marker = "v", color = "red")
plt.xlabel("Date", fontsize = 18)
plt.ylabel("Close Price", fontsize = 18)
