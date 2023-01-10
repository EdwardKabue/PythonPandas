import pandas as pd

d_parser = lambda x: pd.to_datetime(x, format="%Y-%m-%d %I-%p")

df = pd.read_csv("data/ETH_1h.csv", parse_dates=["Date"], date_parser=d_parser) #format date data when loading dataframe

#print(df.head())

#print(df.loc[0, "Date"])

#convert 'Date' column to datetime objects
#df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %I-%p")
#print(df["Date"])
#print(df.loc[0, "Date"].day_name()) #Print name of day

#print(df["Date"].dt.day_name()) #print out a series of the names days for each value in the 'Date' series.

df["DayOfWeek"] = df["Date"].dt.day_name() #Add new column to the dataframe that contains the days of the week.

#print(df) #print new dataframe.

#print(df["Date"].min()) #print the earliest date.

#print(df["Date"].max()) #print the most recent date.

#print(df["Date"].max() - df["Date"].min()) #print the time difference between two timestamps

# filt = (df["Date"] >= "2020") #filter for records with the date later than or equal to 2020.

# filt = (df["Date"] >= "2019") & (df["Date"] < "2020") #filter between 2019 and 2020

# filt = (df["Date"] >= pd.to_datetime("2019-01-01") ) & (df["Date"] < pd.to_datetime("2020-01-01")) #filter using datetime values

# print(df.loc[filt])

#set the date column as the index.
df.set_index("Date", inplace=True)
#print(df["2019"]) #filter using year after setting the index as date column
print(df["2020-01":"2020-02"]) #slice the dataframe based on year and month.