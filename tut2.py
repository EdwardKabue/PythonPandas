import pandas as pd

people = {
  "firstName": ["Henry", "Ford"],
  "lastName": ["Mustang", "Toyoda"],
  "DOB": [1964, 1963]
}

#Creating your own dataframe
people_df = pd.DataFrame(people)

#A series (I.e. rows of a single column.) is a list of data with some functionality.

#print(people_df["DOB"]) #Print out a series.

# print(people_df[["firstName", "lastName"]]) #Print out a desired set of columns. Not a series because has multiple columns.

# print(people_df.columns) #print out the columns.


#selecting row based on integer value.
# print(people_df.iloc[0]) #prints first row using integer index.
# print(people_df.iloc[[0, 1]]) #prints first and second rows using integer index.
# print(people_df.iloc[[0, 1], 2]) #prints the third column for the first and second rows using integer index.
print(people_df.loc[0]) #print out the first row using the integer index as label.
print(people_df.loc[[0, 1]]) #Print multiple rows using the integer index as label.
print(people_df.loc[[0, 1], 'DOB']) #Print out the DOB column.
print(people_df.loc[[0, 1], ["lastName", "DOB"]]) #Print out the a list of columns.