import pandas as pd

people = {
  "firstName": ["Henry", "Ford"],
  "lastName": ["Mustang", "Toyoda"],
  "DOB": [1964, 1963]
}

#Creating your own dataframe
people_df = pd.DataFrame(people)

#print(people_df["firstName"]+" "+" "+people_df["lastName"])

#Add two columns together and place the result in a new column.
people_df["fullName"] = people_df["firstName"]+" "+people_df["lastName"]
#print(people_df)

#Remove a column. Use 'drop' method.
people_df.drop(columns=["firstName", "lastName"], inplace=True)
print(people_df)

#Split field into list using space.
#print(people_df["fullName"].str.split(" "))

#Split field into list using space and expand.
print(people_df["fullName"].str.split(" ", expand=True))

#Split field into list using space, expand and place the result in new columns
people_df[["firstName", "lastName"]] = people_df["fullName"].str.split(" ", expand=True)
#print(people_df)

#Add a row to a dataframe.
#print(people_df.append({"firstName": "John"}, ignore_index=True))

people = {
  "firstName": ["Tony", "Rice"],
  "lastName": ["Brendan", "Pulis"],
  "DOB": [1962, 1965]
}

people_df2 = pd.DataFrame(people)

#print(people_df2)

#Append a dataframe to another.
#print(people_df.append(people_df2, ignore_index=True))
people_df = people_df.append(people_df2, ignore_index=True)
print(people_df)

#Remove a row. Use the index.
#print(people_df.drop(index=3))

#Remove based on a filter.
filt = people_df["lastName"]=="Pulis"
print(people_df.drop(index=people_df[filt].index))

