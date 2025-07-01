#!/usr/bin/env python3
"""
Create XLSForm with careful CSV handling
"""

import pandas as pd
import csv

# Read CSV manually to debug
def read_csv_manual(filename):
    rows = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows

# Check the survey CSV structure
survey_rows = read_csv_manual('survey-questions.csv')
print("First 3 rows from manual reading:")
for i, row in enumerate(survey_rows[:3]):
    print(f"Row {i}: {row[:3]}...")  # Show first 3 columns
    
print(f"\nTotal columns in header: {len(survey_rows[0])}")
print(f"Header: {survey_rows[0][:5]}...")

# Now create DataFrame properly
header = survey_rows[0]
data_rows = survey_rows[1:]

survey_df = pd.DataFrame(data_rows, columns=header)
print(f"\nDataFrame shape: {survey_df.shape}")
print("First few rows of proper DataFrame:")
print(survey_df[['type', 'name', 'label']].head())

# Create the Excel file
choices_df = pd.read_csv('survey-choices.csv')
settings_df = pd.read_csv('survey-settings.csv')

with pd.ExcelWriter('ds4owd_precourse_survey_fixed.xlsx', engine='openpyxl') as writer:
    survey_df.to_excel(writer, sheet_name='survey', index=False)
    choices_df.to_excel(writer, sheet_name='choices', index=False)
    settings_df.to_excel(writer, sheet_name='settings', index=False)

print("Fixed XLSForm created: ds4owd_precourse_survey_fixed.xlsx")