# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 00:38:38 2022

@author: Jony
"""

import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
# Creation of pandas DataFrame for data analysis.
df = pd.read_csv('2017.csv', parse_dates=['inputdate', 'tradedate'], 
                 infer_datetime_format=True)
# ===============================TASK 1=======================================
# Aggregation of columns to count number of transactions by exchange in file.
# As most transactions in file are off exchange transactions, I only consider
# the first companyName that has a name.
# ============================================================================
exchange_transactions = df.groupby('exchange')['transactionID'].count()
exchange_most_transactions = exchange_transactions.sort_values(
                                              ascending=False).head(2)
print(f'TASK 1: The exchange with most transactions (besides off \
exchange transactions) in the file is {exchange_most_transactions.index[1]}.')

# ===============================TASK 2=======================================
# Filters dataframe's data from 2017-08 only to get which companyName had the 
# highest combined valueEUR.
# ============================================================================
august2017 = df[df.tradedate.dt.to_period('M') == '2017-08']
# Transform data from long to wide format to simplify analysis and sum.
companyEUR = august2017.pivot_table(index='companyName', values='valueEUR', 
                                    aggfunc='sum') 
companyEUR.sort_values(by='valueEUR', ascending=False, inplace=True)
print(f'TASK 2: The companyName that had in August 2017 the highest combined \
valueEUR is {companyEUR.iloc[0].name}.')
# ===============================TASK 3=======================================
# Filters dataframe's data from 2017 only to get percentage of transactions per
# month with tradeSignificance 3.
# ============================================================================
df2017 = df[df.tradedate.dt.to_period('Y') == '2017']
df2017['month'] = df2017.tradedate.dt.month_name()
tradeSignificance3 = df2017.pivot_table(index='month', 
                                        columns='tradeSignificance', 
                                        values='transactionID', 
                                        aggfunc='count')
tradeSignificance3['Percent'] = (tradeSignificance3[3] / 
                                 tradeSignificance3[3].sum())*100
new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
             'August', 'September', 'October', 'November', 'December']
tradeSignificance3 = tradeSignificance3.reindex(new_order, axis=0)
print(f"TASK 3: Percentages of tradeSignificance3 transactions per \
{tradeSignificance3['Percent'].to_string()}")
