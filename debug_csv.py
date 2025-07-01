#!/usr/bin/env python3
"""
Debug CSV structure issues
"""

import csv

# Read CSV manually to debug
def debug_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"Header has {len(header)} columns")
        
        for i, row in enumerate(reader):
            if len(row) != len(header):
                print(f"Row {i+1} has {len(row)} columns (expected {len(header)})")
                print(f"Row content: {row[:5]}...")  # First 5 fields
                
                if len(row) > len(header):
                    print(f"Extra fields: {row[len(header):]}")
                
                if i > 10:  # Only check first 10 problematic rows
                    break
        
        print("Checking complete.")

debug_csv('survey-questions.csv')