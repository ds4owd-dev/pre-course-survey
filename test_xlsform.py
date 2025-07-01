#!/usr/bin/env python3
"""
Test XLSForm creation with proper validation
"""

import pandas as pd
import os

# Test reading the CSV files
print("Testing CSV file reading...")

try:
    # Read with explicit quoting settings
    survey_df = pd.read_csv('survey-questions.csv', quoting=1, escapechar='\\')
    print(f"Survey CSV loaded successfully: {len(survey_df)} rows")
    print("First few rows:")
    print(survey_df.head(3))
    print("\nColumn names:")
    print(survey_df.columns.tolist())
    
    # Check for any problematic data
    print("\nChecking for issues...")
    for idx, row in survey_df.iterrows():
        if pd.isna(row['type']) or row['type'].strip() == '':
            print(f"Row {idx}: Empty type")
        elif len(str(row['type']).split(',')) > 1:
            print(f"Row {idx}: Type contains comma: {row['type']}")
            
except Exception as e:
    print(f"Error reading survey CSV: {e}")
    
try:
    choices_df = pd.read_csv('survey-choices.csv', quoting=1)
    print(f"Choices CSV loaded successfully: {len(choices_df)} rows")
except Exception as e:
    print(f"Error reading choices CSV: {e}")
    
try:
    settings_df = pd.read_csv('survey-settings.csv')
    print(f"Settings CSV loaded successfully: {len(settings_df)} rows")
except Exception as e:
    print(f"Error reading settings CSV: {e}")