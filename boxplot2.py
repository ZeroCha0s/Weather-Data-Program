# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:23:49 2023

@author: Devon King
"""

#Purpose: Create box plot for period 2 data
#Name: Devon King
#Date: 02/08/23
import pandas as pd
import matplotlib.pyplot as plt
#df2 = pd.read_csv("formatdata2.csv")
#df2.boxplot(); plt.suptitle('Period 2 box plot')
#plt.show()
print(df2.info())
print(df2.describe())
print("The median is",df2.median())
