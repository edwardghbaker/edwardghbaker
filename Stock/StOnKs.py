# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math as m
import numpy as np
import pandas as pd
import scipy.optimize as sciop
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.pyplot import figure

import mplfinance as mpf
import yfinance as yf

#%% Define functions
def Compound(initial=1,years=27,percent=7.4):
    comp = initial*((1+(percent/100))**years)
    return comp

def decimalYear(DF):
    decYear = np.array(DF.index.year+DF.index.dayofyear/365.)
    DF['decYear'] = decYear
    
#%% Modify data

Years = np.linspace(2005,2022,18)
fig,ax=plt.subplots(1,1,figsize=(6,8))

FTSE100 = yf.download(tickers='^FTSE',start='2005-01-01',end='2022-01-01',interval='1d')
decimalYear(FTSE100)

SP500 = yf.download(tickers='^GSPC',start='2005-01-01',end='2022-01-01',interval='1d')
decimalYear(SP500)

#NDAQ = yf.download(tickers='NDAQ',start='2005-01-01',end='2022-01-01',interval='1d')
#decimalYear(NDAQ)

USS = np.array(Compound(initial=FTSE100['Open'][0],years=(Years-Years[0])))


ax.plot(FTSE100['decYear'],FTSE100['Open'],label='FTSE100')
ax.plot(SP500['decYear'],SP500['Open']*(FTSE100['Open'][0]/SP500['Open'][0]),label='SP500')
#ax.plot(NDAQ['decYear'],NDAQ['Open']*(FTSE100['Open'][0]/NDAQ['Open'][0]),label='NDAQ')

ax.plot(Years,USS,label='USS - using annualised rate')
ax.legend()