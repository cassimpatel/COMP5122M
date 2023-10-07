# -*- coding: utf-8 -*-
"""
Created on 26 Sep 2018

How to print the number of distinct values, value counts (the number of records that have each value) and percentiles of a numerical variable

@author: Roy Ruddle
"""

import pandas as pd

input_filename = 'teaching value distributions.csv'
df = pd.read_csv(input_filename)

print(df) # Print the DataFrame
print() # Print a blank line
print("{v: <8}   {n: ^25}".format(v='Variable', n='Number of distinct values')) # Print a header

for variable in df.columns: # Print a row for each variable
    print("{v: <8}   {n: ^25}".format(v=variable, n=len(df[variable].value_counts())))

print() # Print a blank line
print('Value counts for Gender')
print()
sorted_value_counts = df['Gender'].value_counts().sort_index()
print("{v: <6}   {n: ^5}".format(v='Value', n='Count'))

for value, count in sorted_value_counts.items():
    print("{v: <6}   {n: ^5}".format(v=value, n=count))


print() # Print a blank line
print('Percentiles for Mark')
print()
quantiles = df['Mark'].dropna().quantile([0.0, 0.25, 0.5, 0.75, 1.0])
print("{i: <10}   {v: ^5}".format(i='Percentile', v='Value'))

for ind, val in quantiles.items():
    print("{i: <10}   {v: ^5}".format(i=ind, v=val))
