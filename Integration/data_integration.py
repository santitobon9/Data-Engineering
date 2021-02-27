import pandas as pd
import numpy as np


def read_files(filename1, filename2): # Reads in files and stores them in dataframes
    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename2)
    return df1, df2

def clean_census(census_df):
    for ind, row in census_df.iterrows():
        #not_valid = validate_census_row(row)
        if(validate_census_row(row) == True):
            print(row['TractId'], "row dropped")
            census_df.drop([ind])
    census_df = clean_county(census_df)
    

def validate_census_row(row):
    #if (row['TractId'] == 1003011602):
        #print(row)
    assert_row = row.isnull().values.any()
        #print(assert_row)
    return assert_row

def clean_county(df):
    for ind, row in df.iterrows():
        df.at[ind, 'County'] = ' '.join(row['County'].split(' ')[:-1])      
    #print(df['County'])
    return df

def aggregate_census(df):

    return

def main():
    covid_df, census_df = read_files("COVID_county_data.csv", "acs2017_census_tract_data.csv")
    clean_census(census_df)
    census_df.to_csv("test_census.csv", index=False)

main()