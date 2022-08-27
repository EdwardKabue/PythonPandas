import pandas as pd

people = {
  "firstName": ["Henry", "Ford"],
  "lastName": ["Mustang", "Toyoda"],
  "DOB": [1964, 1963]
}

df = pd.read_csv("data/survey_results_public.csv", index_col="Respondent") #Create dataframe. Set Respondent column as index.
#Dataframes are simply rows and columns. 

# print(df.shape) #Print out the colmns and rows
# print(df.info()) #Print out the information on the columns such as data type and name.

schema_df = pd.read_csv("data/survey_results_schema.csv", index_col="Column")

pd.set_option("display.max_columns", 85) #Set display option for rows.
pd.set_option("display.max_rows", 85) #Set display option for rows.

#Creating your own dataframe
people_df = pd.DataFrame(people)

#print( people_df.set_index("DOB") ) #Set one of the columns as an index. Does not change the original dataframe.
# people_df.set_index("DOB", inplace=True)  #Set one of the columns as an index. Changes the original dataframe.
# print(people_df)
# print(people_df.index) #Get the index values.
# print(people_df.loc[1964, "lastName"]) #Get a row based on the new index value.

# print(people_df.iloc[0]) #The integer index can still be used with iloc.

# people_df.reset_index(inplace=True) #Reset to the original index.
# print(people_df)

#print( df.head() )
print (schema_df.loc["MgrIdiot", "QuestionText"])
print( schema_df.sort_index() ) #Sort by index alphabetically.

