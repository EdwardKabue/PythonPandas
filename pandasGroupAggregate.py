import pandas as pd

df = pd.read_csv("data/survey_results_public.csv", index_col="Respondent") #Create dataframe. Set Respondent column as index.
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col="Column")

#Print the median value
# print(df["ConvertedComp"].median())

#Print median from different fields
# print(df.median())

#Print different stats
#print(df.describe())

#Print count of non-empty records for a field(E.g. "ConvertedComp")
#print(df["ConvertedComp"].count())

#Print counts of different entries for a column(E.g. "Hobbyist")
#print(df["Hobbyist"].value_counts())

#Print value based on defined index "Column".
#print(schema_df.loc["SocialMedia"])

#Print the counts as percentages
#print(df["SocialMedia"].value_counts(normalize=True))

#Define a group by object and store it in a variable.
country_grp = df.groupby(["Country"])

#Print dataframe based on a group value.
#print(country_grp.get_group("United States"))

#Get value counts for a column based on a filter.
# filt = df["Country"] == "India"

# print(df.loc[filt]["SocialMedia"].value_counts())

#Get value counts based per group.
#print(country_grp["SocialMedia"].value_counts())

#Get value counts for a single group.
#print(country_grp["SocialMedia"].value_counts().loc["India"])

#Get value counts for a single group as percentages.
#print(country_grp["SocialMedia"].value_counts(normalize=True).loc["India"])

#print median for groups.
#print(country_grp["ConvertedComp"].median());

#print median for a single group.
#print(country_grp["ConvertedComp"].median().loc["Afghanistan"])

#Use multiple aggregate functions on groups.
#print(country_grp["ConvertedComp"].agg(["median", "mean"]))

#Use multiple aggregate functions on a single group.
#print(country_grp["ConvertedComp"].agg(["median", "mean"]).loc["Albania"])

#Get grouping count within a single group.
# filt = df["Country"] == "India"
# print(df.loc[filt]["LanguageWorkedWith"].str.contains("Python").sum())

#Use 'apply' method to get grouping count within multiple groups.
#print(country_grp["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum()))

#Concatenate two series
country_respondents = df["Country"].value_counts()
#print(country_respondents)
country_uses_python = country_grp["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum())
#print(country_uses_python)
python_df = pd.concat([country_respondents, country_uses_python], axis="columns", sort=False)
python_df.rename(columns={"Country":"NumRespondents", "LanguageWorkedWith":"NumKnowsPython"}, inplace=True)
print(python_df)
python_df["PctKnowsPython"] = (python_df["NumKnowsPython"]/python_df["NumRespondents"]) * 100
print(python_df)
python_df.sort_values(by="PctKnowsPython", ascending=False, inplace=True)
print(python_df)