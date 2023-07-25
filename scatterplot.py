# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:11:16 2023

@author: Devon King
"""

#Purpose: Create scatter plot of humidity for period 1. Can replace df1 to df2 to display second period data
#Name: Devon King
#Date: 02/08/23
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values,df1['Humidity']); plt.suptitle('Humidity')
plt.show()
