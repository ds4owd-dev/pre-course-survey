#!/usr/bin/env python3
"""
Create XLSForm Excel file from CSV files for KoboToolbox
"""

import pandas as pd
import os

# Read CSV files with explicit settings
survey_df = pd.read_csv('survey-questions.csv', quoting=1, escapechar='\\')
choices_df = pd.read_csv('survey-choices.csv', quoting=1, escapechar='\\')
settings_df = pd.read_csv('survey-settings.csv')

# Create Excel writer
with pd.ExcelWriter('ds4owd_precourse_survey.xlsx', engine='openpyxl') as writer:
    # Write survey sheet
    survey_df.to_excel(writer, sheet_name='survey', index=False)
    
    # Write choices sheet
    choices_df.to_excel(writer, sheet_name='choices', index=False)
    
    # Write settings sheet
    settings_df.to_excel(writer, sheet_name='settings', index=False)

print("XLSForm created successfully: ds4owd_precourse_survey.xlsx")
print("\nThis file can be uploaded directly to KoboToolbox:")
print("1. Go to https://www.kobotoolbox.org/")
print("2. Create a new project")
print("3. Upload the XLSForm (ds4owd_precourse_survey.xlsx)")
print("4. Deploy the form")