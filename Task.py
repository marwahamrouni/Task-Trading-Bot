#!/usr/bin/python
# -*- coding: utf-8 -*-

# In[10]:

import pandas as pd  # data processing

df = pd.read_csv('TSLA.csv')  # converting our csv file to a dataframe

# In[9]:

price = df['Close'].values  # the array 'price' holds the daily close price of a stock


def maxProfit(price):
    """
    Takes as input the array price,
    keeps track of the minimum price 
    while computing the difference between the minimum price
    and the prices that appear after it
    and returns the indices of the best buying and selling 
    days in our data as well as the maximum 
    profit earned by buying and selling on these days.
    """

    price_size = len(price)
    max_profit = price[1] - price[0]
    min_price = price[0]
    sell_index = 0
    buy_index = 0

    if price_size < 2:
        return 0
    else:
        for i in range(1, price_size):
            if price[i] - min_price > max_profit:
                max_profit = price[i] - min_price
                sell_index = i
            if price[i] < min_price:
                min_price = price[i]
                buy_index = i

    return (buy_index, sell_index, max_profit)




(buy_index, sell_index, profit) = maxProfit(price) # calling the above function
buying_price = df.loc[buy_index, 'Close'].astype('float') # computing the buying price
profit_percentage = profit / buying_price * 100 #  computing the profit percentage

print('Best day to buy stocks:  ' + str(df.loc[buy_index, 'Date']))
print('Best day to sell stocks: ' + str(df.loc[sell_index, 'Date']))
print('Percentage Profit: {}%'.format(round(profit_percentage, 2)))

# In[ ]:
