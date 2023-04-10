# Imports
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from datetime import datetime


# Alpha Vantage API Key
key = 'KROWYDQHHNH5GCMN'


# Current Date and Time
date = datetime.now()

ts = TimeSeries(key, output_format='pandas', indexing_type = "integer")

# Creates a Chart detailing a Stock's Performance over a Month
def month_chart (ticker):
    
    
    # Call Data from Alpha Vantage
    data, meta_data = ts.get_intraday(symbol= ticker, interval='30min', outputsize='full')
    
    
    # Invert Data
    data = data[::-1].reset_index(drop=True)
    
    
    # Shorten Data to Starting This Month
    data.rename(columns = {"index": "Date"}, inplace = True)
    market_open_thisMonth = str(datetime(date.year, date.month-1, date.day, 9, 30, 0))
    last_close = data[data['Date'] == market_open_thisMonth].index[0]
    month_data = data.iloc[last_close:]

    
    # Make Chart Green if There is a Net Gain and Red if There is a Net Loss
    if (month_data['4. close'].iloc[-1] > month_data['4. close'].iloc[0]):
        plt.plot(month_data['Date'], month_data['4. close'], color = 'green')
    else:
        plt.plot(month_data['Date'], month_data['4. close'], color = 'red')
    
    
    # Chart Setup
    plt.title(ticker + ' Past Month Performance')
    plt.xticks(np.arange(0, len(month_data), len(month_data)/5))
    plt.grid()
    plt.show()
    
    # Creates a Chart detailing a Stock's Performance over a Week
def week_chart (ticker):
    
    
    # Call Data from Alpha Vantage
    data, meta_data = ts.get_intraday(symbol= ticker, interval='15min', outputsize='full')
    
    
    # Invert Data
    data = data[::-1].reset_index(drop=True)
    
    
    # Shorten Data to Starting from This Week
    data.rename(columns = {"index": "Date"}, inplace = True)
    market_open_thisweek = str(datetime(date.year, date.month, date.day-7, 9, 30, 0))
    last_close = data[data['Date'] == market_open_thisweek].index[0]
    week_data = data.iloc[last_close:]
    
    
    # Make Chart Green if There is a Net Gain and Red if There is a Net Loss
    if (week_data['4. close'].iloc[-1] > week_data['4. close'].iloc[0]):
        plt.plot(week_data['Date'], week_data['4. close'], color = 'green')
    else:
        plt.plot(week_data['Date'], week_data['4. close'], color = 'red')
    

    # Chart Setup
    plt.title(ticker + ' Past Week Performance')
    plt.xticks(np.arange(0, len(week_data), len(week_data)/5))
    plt.grid()
    plt.show()
    
    # Creates a Chart detailing a Stock's Performance over a Day
def date_chart(ticker):
    
    
    # Call Data from Alpha Vantage
    data, meta_data = ts.get_intraday(symbol= ticker, interval='1min', outputsize='full')
    
    
    # Invert Data
    data = data[::-1].reset_index(drop=True)
    
    
    # Shorten Data to Starting from Today
    data.rename(columns = {"index": "Date"}, inplace = True)
    market_open_today = str(datetime(date.year, date.month, date.day, 9, 30, 0))
    last_close = data[data['Date'] == market_open_today].index[0]
    day_data = data.iloc[last_close:]

    
        
    
        
    # Make Chart Green if There is a Net Gain and Red if There is a Net Loss    
    if (day_data['4. close'].iloc[-1] > day_data['4. close'].iloc[0]):
        plt.plot(day_data['Date'], day_data['4. close'], color = 'green')     
    else:
        plt.plot(day_data['Date'], day_data['4. close'], color = 'red')
        
    
    # Chart Setup
    plt.title(ticker + ' Past Day Performance')
    plt.xticks(np.arange(0, len(day_data), len(day_data)/5))
    plt.grid()
    plt.show()
    
    # Displays Day, Week, and Month Charts
def all_charts(ticker):
    plt.figure(figsize = (25, 10))
    month_chart(ticker)
    plt.figure(figsize = (25, 10))
    week_chart(ticker)
    plt.figure(figsize = (25, 10))
    date_chart(ticker)
    
    
all_charts('TSLA')