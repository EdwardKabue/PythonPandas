import pandas as pd

people = {
  "firstName": ["Henry", "Ford", "Zippy"],
  "lastName": ["Mustang", "Toyoda", "Jones"],
  "DOB": [1964, 1963, 1964]
}

#Creating your own dataframe
people_df = pd.DataFrame(people)

df = pd.read_csv("data/survey_results_public.csv", index_col="Respondent") #Create dataframe. Set Respondent column as index.
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col="Column")

pd.set_option("display.max_rows", 85) #Set display option for rows.

#Sort by lastName
#print(people_df.sort_values(by="firstName", ascending=False))

#Sort by multiple columns
#print(people_df.sort_values(by=["DOB", "firstName"], ascending=False))

#Sort by multiple columns in different orders
# people_df.sort_values(by=["DOB", "firstName"], ascending=[False, True], inplace=True)
# print(people_df)

#Sort by index. I.e. sort by the original order by which the rows were added.
# print(people_df.sort_index())

#Sort series.
# print(people_df["lastName"].sort_values())

#Print first 5 values from a series.
#print(df["Country"].head())

df.sort_values(by="Country", inplace=True)

#Print first 5 values from a series from the sorted dataframe.
print(df["Country"].head())

#Print first 50 values from multples columns from the sorted dataframe.
#print(df[["Country", "ConvertedComp"]].head(50))

df.sort_values(by=["Country", "ConvertedComp"], ascending=[True, False], inplace=True)

#Print first 50 values from multples columns from the sorted dataframe.
#print(df[["Country", "ConvertedComp"]].head(50))

#Print the nlargest values from a series.
print(df["ConvertedComp"].nlargest(10))

#Print the nlargest values from a dataframe based on a column.
print(df.nlargest(10, "ConvertedComp"))