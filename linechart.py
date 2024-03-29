# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:02:05 2023

@author: Devon King
"""

#Purpose: Create Celsius plot comparing period 1 and period 2
#Name: Devon King
#Date: 02/08/2023
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv") #baseline data is period 1 (older)
df2 = pd.read_csv("formatdata2.csv") #data for period 2 (more recent)
plt.figure(); df1.Humidity.plot(label = 'period 1'); df2.Humidity.plot(label = 'period 2'); plt.legend(loc='best'); plt.suptitle('Humidity')
plt.show()
