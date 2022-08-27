import pandas as pd

people = {
  "firstName": ["Henry", "Ford"],
  "lastName": ["Mustang", "Toyoda"],
  "DOB": [1964, 1963]
}

#Creating your own dataframe
people_df = pd.DataFrame(people)

df = pd.read_csv("data/survey_results_public.csv") #Create dataframe

pd.set_option("display.max_columns", 85) #Set display option for rows.
pd.set_option("display.max_rows", 85) #Set display option for rows.

#print(people_df["lastName"] == "Mustang") #Print a series of booleans showing if a row meets the filter condition 

filt = (people_df["lastName"] == "Mustang") #Variable to store the filter mask

#print(people_df[filt]) #Print out the filtered dataframe.

# print(people_df.loc[filt]) #Can be used with loc.

# print(people_df.loc[filt, 'firstName']) #Can be used with loc to get specific columns.

# filt = (people_df["lastName"] == "Mustang") & (people_df["DOB"] == 1964) #use AND operator (&) for multiple conditions

# print(people_df.loc[filt, 'firstName']) #Can be used with loc to get specific columns.

# filt = (people_df["lastName"] == "Mustang") | (people_df["DOB"] == 1963) #use OR operator (|) for multiple conditions

# print(people_df.loc[filt, 'firstName']) #Can be used with loc to get specific columns.

# print(people_df.loc[~filt, 'firstName']) #Use ~ to negate the condition.

# high_salary = (df["ConvertedComp"] > 70000)

# print(df.loc[high_salary, ["Country", "LanguageWorkedWith", "ConvertedComp"]])

# countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]
# filt = df["Country"].isin(countries) #Filter based on a list of values.

# print(df.loc[filt, ["Country", "LanguageWorkedWith"]])

filt = df["LanguageWorkedWith"].str.contains("Python", na=False) #Filter based on a string being in a value among others.

print(df.loc[filt, "LanguageWorkedWith"])