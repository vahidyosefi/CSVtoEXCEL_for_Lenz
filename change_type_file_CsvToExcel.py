# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:18:36 2022

@author:vahid 
  
 goal 1: change type lenz from csv to excel
 goal 2: remove null row and remove Avg
"""

import pandas as pd
import datetime
import xlsxwriter

import numpy as np


##### input data
# df1 = pd.read_excel(r'D:\operator\AIO\1401_01_07\Aio_1401_01_07.xlsx')
df1 = pd.read_csv(r'C:\Users\PC\Downloads\Lenz_14010103.csv', header=None)

df2 = df1.copy()
df1.columns = ["Channel ID", "Channel Name", "Program Name", "Begin Time","End Time","Total duration(Hour)","Total Access times","Recorded times",'re']
df1.head()

print('remove end column')
df1.pop("re")

aa = len(df1)
print('total row',aa)

print('remove null row and remove Avg')

df1 = df1.dropna(axis=0, subset=['Channel ID'])	

df1.drop(df1[df1['Channel ID'] == 'Avg'].index, inplace = True)

aaa = len(df1)
print('total row after remove row null and Avg',aaa)
# bb =aaa-aa
print('calculate number remove row : ', aaa-aa)


# df1.to_excel(r'D:\python\EPG_vahid\input\source\source_per_month\Esfand_1400\lenz_1400_12.xlsx', index=False)


df1.to_excel(r'C:\Users\PC\Downloads\lenz_1401_01_03.xlsx', index=False)
