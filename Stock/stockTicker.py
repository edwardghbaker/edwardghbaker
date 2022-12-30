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

fig,ax=plt.subplots(1,1,figsize=(6,8))
FTSE100 = yf.download(tickers='^FTSE',period='35y',interval='1d')
SP500 = yf.download(tickers='^GSPC',period='35y',interval='1d')

ax.plot(FTSE100['Open'],label='FTSE100')
ax.plot(SP500['Open']*6.91381165608,label='SP500')
ax.legend()