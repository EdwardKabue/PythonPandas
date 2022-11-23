import pandas as pd
import numpy as np

people = {
  "firstName": ["Henry", "Ford", "Chris", np.nan, None],
  "lastName": ["Mustang", "Toyoda", "NA", np.nan, "NA"],
  "email": ["Missing", "fto@hotmail.com", "cr@yahoo.com", None, np.nan],
  "age": ["64", "63", "86", None, "Missing"]
}

na_vals = ["NA", "Missing"] #list of custom missing values.
df = pd.read_csv("data/survey_results_public.csv", index_col="Respondent", na_values=na_vals) #Create dataframe. Set Respondent column as index.

schema_df = pd.read_csv("data/survey_results_schema.csv", index_col="Column")

pd.set_option("display.max_columns", 85) #Set display option for rows.
pd.set_option("display.max_rows", 85) #Set display option for rows.


people_df = pd.DataFrame(people)
people_df.replace("NA", np.nan, inplace=True)
people_df.replace("Missing", np.nan, inplace=True)

# print(people_df)
# #drop rows with missing values
# print(people_df.dropna())
# #drop rows missing values for a specific column.
# print(people_df.dropna(axis="index", how="any", subset=["email"]))
# #Don't drop rows that have values for any column in a list of columns.
# print(people_df.dropna(axis="index", how="all", subset=["email", "lastName"]))
# #Return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, gets mapped to True values. Everything else gets mapped to False values.
# print(people_df.isna())
# #Fill in NA values
# print(people_df.fillna(0))
# #Get data types of a column
# print(people_df.dtypes)
# #Type casting
# people_df["age"] = people_df["age"].astype(float)
# print(people_df.dtypes)
# print(people_df["age"].mean())

print(df["YearsCode"].head(10)) #Get top 10 years in experience.

df["YearsCode"].replace("Less than 1 year", 0, inplace=True)
df["YearsCode"].replace("More than 50 years", 51, inplace=True)
df["YearsCode"] = df["YearsCode"].astype(float)

print(df["YearsCode"].median())