# -*- coding: utf-8 -*-
"""
Created on 26 Sep 2018

How to print the data types and the number of missing values of each variable in a dataset, and correct the data type of specific variables.

@author: Roy Ruddle
"""

import pandas as pd

input_filename = 'teaching data type.csv'
df = pd.read_csv(input_filename)

print(df) # Print the DataFrame
print() # Print a blank line
print("{v: <18}   {dt: <14}   {n: ^24}".format(v='Variable', dt='Data type', n='Number of missing values')) # Print a header

for variable in df.columns: # Print a row for each variable
    print("{v: <18}   {dt: <14}   {n: ^24}".format(v=variable, dt=str(df[variable].dtype), n=df[variable].isnull().sum()))

print() # Print a blank line

df['Gender'] = df['Gender'].astype(object)
df['Date of birth'] = pd.to_datetime(df['Date of birth'], dayfirst=True, yearfirst=False)

print() # Print a blank line
print('Data type (corrected for Gender and Date of birth)')
print() # Print a blank line
print("{v: <18}   {dt: <14}".format(v='Variable', dt='Data type')) # Print a header

for variable in df.columns: # Print a row for each variable
    print("{v: <18}   {dt: <14}".format(v=variable, dt=str(df[variable].dtype)))
