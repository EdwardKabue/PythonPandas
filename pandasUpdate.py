import pandas as pd

people = {
  "firstName": ["Henry", "Ford"],
  "lastName": ["Mustang", "Toyoda"],
  "DOB": [1964, 1963]
}

def update_name(name):
  return name.upper()

def element_length(element):
  if(isinstance(element, int)):
    return len(str(element))
  else:
    return len(element)

#Creating your own dataframe
people_df = pd.DataFrame(people)

df = pd.read_csv("data/survey_results_public.csv", index_col="Respondent") #Create dataframe. Set Respondent column as index.

# people_df.columns = ["first", "last", "dob"] #Change column names.

# print(people_df)

# people_df.columns = [x.upper() for x in people_df.columns] #use comprehension to format the column names

# print(people_df)

# people_df.columns = people_df.columns.str.replace("Name", "") #String replacement in column names.

# print(people_df)

people_df.rename(columns={"firstName":"fName", "lastName":"lName"}, inplace=True)

print(people_df)

people_df.loc[1] = ["John", "Smith", 1989] #Updating the second row.

print(people_df)

people_df.loc[1, ["fName", "lName"]] = ["Jane", "Doe"] #Update the columns fName and lName on the second row.

print(people_df)

people_df.loc[0, "DOB"] = 2000 #Update the column DOB in the first row.

print(people_df)

#Using at method
people_df.at[1, "fName"] = "Peter" #Update the column fName in the second row.

print(people_df)

#Using a filter
filt = (people_df['fName']=="Peter")
people_df.loc[filt, "DOB"] = 1800 #Update the field DOB based on the filter 'filt'

print(people_df)

#Change all values in a column at once.
# people_df["fName"] = people_df["fName"].str.lower()

# print(people_df)

#Apply a function to all values in a series using the method 'apply'
print(people_df["lName"].apply(len))

print(people_df['fName'].apply(update_name)) #Applying a custom method 'update_name'.

#'apply' can also be used to update all values in a column at once.
people_df['fName'] = people_df['fName'].apply(update_name)

print(people_df)

#apply lambda function
people_df['fName'] = people_df['fName'].apply(lambda x: x.lower())

print(people_df)

#get number of values in all columns for a dataframe using 'apply' and 'len'
print(people_df.apply(len))

#get number of values in a column for a dataframe using 'len'
print(len(people_df['fName']))

#get all fields across rows in a dataframe
print(people_df.apply(len, axis='columns'))

#get minimum value for each field in a dataframe
print(people_df.apply(pd.Series.min))

#apply lambda function to all series in a dataframe
print(people_df.apply(lambda x: x.min()))

#apply function to each individual element in the dataframe.
print(people_df.applymap(element_length))

#using the method 'map'.
print(people_df['fName'].map({"henry": "Louis", "peter":"Enzo"}))

#Use 'replace' to replace only the fields of interest and others remain untouched.
print(people_df['fName'].replace({"henry": "Louis"}))

print(df.rename(columns={'ConvertedComp': 'SalaryUSD'}))

df["Hobbyist"] = df["Hobbyist"].map({'Yes':True, 'No':False})