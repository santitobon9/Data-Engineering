import pandas as pd
import numpy as np

def readfile(filename):
    df = pd.read_csv(filename)
    return df

crash_df = readfile('Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv')

assert_crash_id = crash_df['Crash ID'].notnull().values.any() # Asserts Every record has a Crash ID
print("Every record has a Crash ID:", assert_crash_id)
assert_record_type = crash_df['Record Type'].notnull().values.any() # Asserts Every record has a Record Type
print("Every record has a Record Type:", assert_record_type)
month_range = range(1, 12)
assert_crash_month = crash_df['Crash Month'].values.any() in month_range # Asserts The Crash Month field should be between 1-12
print("The Crash Month field should be between 1-12:", assert_crash_month)
day_range = range(1, 31)
assert_crash_day = crash_df['Crash Day'].values.any() in day_range # Asserts The Crash Day field should be between 1-31
print("The Crash Day field should be between 1-31:", assert_crash_day)
assert_vehicle_id = ((crash_df['Vehicle ID'].values > 3000000)).all() # Asserts Vehicle ID has to be greater than 3000000 or Null
print("Vehicle ID has to be greater than 3000000:", assert_vehicle_id)
participant_IDs = crash_df.loc[crash_df['Participant ID'].notnull()]
assert_participant_seq = participant_IDs['Participant Display Seq#'].notnull().values.any() # Asserts Every Participant ID has a Participant Display Seq #
print("Every Participant ID has a Participant Display Seq #:", assert_participant_seq)
vehicle_IDs = crash_df.loc[crash_df['Vehicle ID'].notnull()]
assert_vehicle_seq = vehicle_IDs['Vehicle Coded Seq#'].notnull().values.any() # Asserts Every Vehicle ID has a Vehicle Coded Seq #
print("Every Vehicle ID has a Vehicle Coded Seq #:", assert_vehicle_seq)
record_types = crash_df.loc[crash_df['Record Type'] > 1]
assert_record_types = record_types['Vehicle ID'].notnull().values.any() # Asserts Every record type 2 or 3 has a Vehicle ID
print("Every record type 2 or 3 has a Vehicle ID:", assert_record_types)
record_type1 = crash_df.loc[crash_df['Record Type'] == 1]
assert_serial = record_type1['Serial #'].notnull().values.any() # Asserts Every entry with record type 1 has a serial #
print("Every entry with record type 1 has a serial #:", assert_serial)
