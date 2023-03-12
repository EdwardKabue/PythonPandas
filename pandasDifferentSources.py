import pandas as pd

df = pd.read_csv("data/survey_results_public.csv", index_col="Respondent") #Create dataframe. Set Respondent column as index.
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col="Column") #Create dataframe. Set Column as index.

pd.set_option("display.max_columns", 85) #Set display option for rows.
pd.set_option("display.max_rows", 85) #Set display option for rows.

filt = (df["Country"]=="India")

india_df = df.loc[filt]
#print(india_df.head())
#india_df.to_csv("data/modified.csv") #save modifed dataframe in a csv file.
#india_df.to_csv("data/modified.tsv", sep="\t") #save modifed dataframe in a tab separated .tsv file.
#india_df.to_excel("data/modified.xlsx") #save modifed dataframe in an excel file.

# test = pd.read_excel("data/modified.xlsx", index_col="Respondent") #create dataframe from excel file.
# print(test)

india_df.to_json("data/modified.json")
