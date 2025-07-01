#!/usr/bin/env python3
"""
Check the Excel file structure
"""

import pandas as pd

# Read the Excel file back
xl = pd.ExcelFile('ds4owd_precourse_survey.xlsx')
print("Sheet names:", xl.sheet_names)

# Check survey sheet
survey_sheet = pd.read_excel('ds4owd_precourse_survey.xlsx', sheet_name='survey')
print("\nSurvey sheet first 5 rows:")
print(survey_sheet.head())
print(f"\nSurvey sheet columns: {survey_sheet.columns.tolist()}")

# Check if the first row has proper data
print(f"\nFirst data row:")
print(f"Type: '{survey_sheet.iloc[0]['type']}'")
print(f"Name: '{survey_sheet.iloc[0]['name']}'")
print(f"Label: '{survey_sheet.iloc[0]['label']}'")

# Look for personal_info specifically
personal_info_rows = survey_sheet[survey_sheet['name'] == 'personal_info']
print(f"\nRows with name='personal_info':")
print(personal_info_rows[['type', 'name', 'label']])