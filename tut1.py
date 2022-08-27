import pandas as pd

df = pd.read_csv("data/survey_results_public.csv") #Create dataframe
#Dataframes are simply rows and columns.

# print(df.shape) #Print out the colmns and rows
# print(df.info()) #Print out the information on the columns such as data type and name.

schema_df = pd.read_csv("data/survey_results_schema.csv")

pd.set_option("display.max_columns", 85) #Set display option for rows.
pd.set_option("display.max_rows", 85) #Set display option for rows.

#print(schema_df)

#print(df["Hobbyist"]) #Print out a series.
#print( df["Hobbyist"].value_counts() ) #Print out unique value number for a series.

# print(df.loc[0, "Hobbyist"])
# print(df.loc[[0, 1, 2], "Hobbyist"])
print(df.loc[0:2, "Hobbyist"]) #Use slicing to print out multiple rows.
print(df.loc[0:2, "Hobbyist":"Employment"]) #Use slicing to print out multiple rows and columns.