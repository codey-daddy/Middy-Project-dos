import pandas as pd
import pandas_datareader.data as pdr
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader.famafrench import get_available_datasets


df = pd.read_excel ('companies.xlsx')
col = df[df["Full Name"] == "Nicolas Consens"]
pd.set_option('display.max_columns', None)
col = col.values.tolist()[0][3:28]

tickers = col
#print(tickers)

start_date = '2005-01-01'
end_date = '2020-12-31'

# After running these two lines below once, you can comment them out so that it runs faster
panel_data_fund = pdr.DataReader(tickers, 'yahoo', start_date, end_date)
panel_data_fund.to_hdf('panel_data_fund.h5', 'key')

panel_data_fund = pd.read_hdf('panel_data_fund.h5', 'key')

Price_Daily = panel_data_fund['Close']
Adj_Price_Daily = panel_data_fund['Adj Close']
Volume_Daily = panel_data_fund['Volume']

#output = pd.ExcelWriter("Output.xlsx", engine = 'xlsxwriter')
#Price_Daily.to_excel(output, sheet_name='Close Price Daily')
#Adj_Price_Daily.to_excel(output, sheet_name='Adj Close Price Daily')
#Volume_Daily.to_excel(output, sheet_name='Volume Daily')


#panel_data_SnP = pdr.DataReader('^GSPC', 'yahoo', start_date, end_date)
#SnP_Price_Daily = panel_data_SnP['Close']
#SnP_Price_Daily.to_excel(output, sheet_name='S&P 500')


#ds_3factor= pdr.DataReader('North_America_3_Factors' ,'famafrench',start= start_date,end=end_date)
#ds_3factor = ds_3factor[0]
#Risk_Free_Returns= ds_3factor['RF']
#Market_Excess = ds_3factor['Mkt-RF']
#df_ffFactor = pd.merge(Market_Excess, Risk_Free_Returns, on='Date')
#print(df_ffFactor)
#df_ffFactor.to_excel(output, sheet_name='FF_Factors')
#output.save()

dx = pd.read_excel ('companies.xlsx', sheet_name = "S&P 500 Constituents")
shareout = dx.ShareOutstanding
shareouttic = dx.ticker
shareout = shareouttic.to_frame().merge(shareout, right_on = None, left_index=True, right_index=True)


tickersdf = pd.DataFrame (tickers, columns = ['ticker'])

mytickers = tickersdf.merge(shareout, on = 'ticker')

# get the last closing price of each ticker for each year and multiply by the oustanding shares
Price_Monthly = Price_Daily.resample("1m").ffill()
Price_Yearly = Price_Daily.resample("1y").ffill()


print(mytickers)
print(Price_Yearly["TJX"])

print("-----------------------------------------------------------------")
Market_Cap = Price_Yearly.copy()
for index, row in mytickers.iterrows():
    Market_Cap[row["ticker"]] = row["ShareOutstanding"] * Price_Yearly[row["ticker"]]

print("-----------------------------------------------------------------")
print(Market_Cap)    
