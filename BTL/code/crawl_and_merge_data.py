import yfinance as yf
import pandas as pd

# Download data for S&P 500, Oil, Gold, and Dollar Index
df1 = yf.download('^GSPC', start="2010-1-1",end="2024-10-27", interval="1d", keepna=True)
df2 = yf.download('CL=F', start="2010-1-1",end="2024-10-27", interval="1d", keepna=True)
df3 = yf.download('GC=F', start="2010-1-1",end="2024-10-27", interval="1d", keepna=True)
df4 = yf.download('DX=F', start="2010-1-1",end="2024-10-27", interval="1d", keepna=True)

# Reset index to make Date a column
df1.reset_index(inplace=True)
df2.reset_index(inplace=True)
df3.reset_index(inplace=True)
df4.reset_index(inplace=True)

# Select only the Date and Close columns for merging
df1_close = df1[["Date", "Close"]]
df2_close = df2[["Date", "Close"]]
df4_close = df4[["Date", "Close"]]



# Forward fill missing values
df1_filled = df1_close.ffill(axis=0)
df2_filled = df2_close.ffill(axis=0)
df3_filled = df3.ffill(axis=0)
df4_filled = df4_close.ffill(axis=0)

# Merge all dataframes on Date
df_merge = pd.merge(df3_filled, df1_filled, on="Date", suffixes=('_Gold', '_SP500'))
df_merge = pd.merge(df_merge, df2_filled, on="Date", suffixes=('', '_Oil'))
df_merge = pd.merge(df_merge, df4_filled, on="Date", suffixes=('', '_DollarIndex'))

df_merge = df_merge.round(2)
# Save to CSV
df_merge.to_csv("Data_gold_oil_dollar_sp500.csv", index=False)