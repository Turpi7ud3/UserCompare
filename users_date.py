import pandas as pd
import datetime

# Gets the current date for the AD Users export, and sets the ad_file variable
today = datetime.date.today()
ad_file = f"exportUsers_{today.year}-{today.month}-{today.day}"
#print(ad_file)

# Read in both CSV files as dataframes
file_a = pd.read_csv(f'{ad_file}.csv')
file_b = pd.read_csv('hyperproof.csv')

# Compare the displayNames column in both dataframes
names_not_in_file_a = file_b[~file_b['displayName'].isin(file_a['displayName'])]

# Write the result to a new CSV file
names_not_in_file_a.to_csv('inactive_users.csv', index=False)

