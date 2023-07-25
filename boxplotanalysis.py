# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:25:48 2023

@author: zeroc
"""

#Purpose: Create box plot for period 2 data
#Name: Devon King
#Date: 02/08/2023
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata.csv")
df2.boxplot(); plt.suptitle('Box plot')
plt.show()
print(df2.describe())
print(df2.median())