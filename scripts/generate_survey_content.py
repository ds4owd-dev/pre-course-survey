#!/usr/bin/env python3
"""Generate survey-content.qmd from Excel survey data."""

import pandas as pd
import textwrap

def wrap_text(text, width=72):
    """Wrap text to specified width."""
    if pd.isna(text):
        return ""
    return "\n".join(textwrap.wrap(str(text), width=width))

def get_question_type_description(row):
    """Convert XLSForm type to human-readable description."""
    q_type = row['type']
    
    if pd.isna(q_type):
        return "Unknown"
    
    # Handle note types
    if 'note' in q_type:
        return "Informational Note"
    
    # Handle text types
    if q_type == 'text':
        if pd.notna(row.get('constraint')) and 'regex' in str(row['constraint']):
            return "Short Text (with validation)"
        return "Short Text"
    
    # Handle select types
    if q_type.startswith('select_one'):
        list_name = q_type.split()[1] if len(q_type.split()) > 1 else ""
        if 'likert' in list_name:
            return "Grid/Matrix"
        return "Multiple Choice"
    
    if q_type.startswith('select_multiple'):
        return "Multiple Select (Checkboxes)"
    
    # Map other types
    type_map = {
        'integer': 'Number',
        'decimal': 'Decimal Number',
        'date': 'Date',
        'time': 'Time',
        'datetime': 'Date and Time',
        'geopoint': 'Location',
        'image': 'Image Upload',
        'audio': 'Audio Recording',
        'video': 'Video Recording',
        'file': 'File Upload',
        'calculate': 'Calculated Field'
    }
    
    for key, value in type_map.items():
        if key in q_type:
            return value
    
    # Groups
    if 'begin' in q_type:
        return "Section Start"
    if 'end' in q_type:
        return "Section End"
    
    return q_type

def extract_list_name(q_type):
    """Extract list name from select_one or select_multiple type."""
    if pd.isna(q_type):
        return None
    parts = str(q_type).split()
    if len(parts) > 1 and parts[0] in ['select_one', 'select_multiple']:
        return parts[1]
    return None

def format_choices(list_name, choices_df):
    """Format choices for a given list."""
    if not list_name:
        return []
    
    list_choices = choices_df[choices_df['list_name'] == list_name]
    return [f"- {row['label']}" for _, row in list_choices.iterrows()]

def generate_content():
    """Generate survey content in Quarto markdown format."""
    # Read data
    survey_df = pd.read_csv('/Users/lschoebitz/Documents/gitrepos/context-ds4owd/gh-org-ds4owd-dev/pre-course-survey/data/survey-questions.csv')
    choices_df = pd.read_csv('/Users/lschoebitz/Documents/gitrepos/context-ds4owd/gh-org-ds4owd-dev/pre-course-survey/data/survey-choices.csv')
    settings_df = pd.read_csv('/Users/lschoebitz/Documents/gitrepos/context-ds4owd/gh-org-ds4owd-dev/pre-course-survey/data/survey-settings.csv')
    
    # Start content
    content = []
    
    # Add header
    content.append("---")
    content.append(f"title: \"{settings_df.iloc[0]['form_title']}\"")
    content.append("format: ")
    content.append("  docx:")
    content.append("    toc: true")
    content.append("    toc-depth: 2")
    content.append("---")
    content.append("")
    
    # Add survey overview
    content.append("# Survey Overview")
    content.append("")
    content.append("This document contains the complete content extracted from the")
    content.append("pre-course survey for data science for openwashdata 002. Each section")
    content.append("and question is presented exactly as it appears in the original form.")
    content.append("")
    
    current_section = None
    current_subsection = None
    in_matrix = False
    matrix_questions = []
    matrix_list_name = None
    
    for idx, row in survey_df.iterrows():
        q_type = row['type']
        
        # Skip empty rows
        if pd.isna(q_type):
            continue
            
        # Handle groups
        if 'begin group' in str(q_type):
            # Check if it's a matrix group
            next_rows = survey_df.iloc[idx+1:idx+10]
            if any('likert' in str(r.get('type', '')) for _, r in next_rows.iterrows()):
                in_matrix = True
                matrix_questions = []
                continue
            
            section_name = row['label'] if pd.notna(row['label']) else row['name']
            if current_section is None:
                content.append(f"\n# {section_name}")
                current_section = section_name
            else:
                content.append(f"\n## {section_name}")
                current_subsection = section_name
            continue
            
        if 'end group' in str(q_type):
            if in_matrix and matrix_questions:
                # Output the matrix question
                content.append("")
                content.append("**Question Type:** Grid/Matrix  ")
                content.append("**Required:** No")
                content.append("")
                
                # Get the rating scale from choices
                if matrix_list_name:
                    content.append("**Rating Scale:**")
                    content.append("")
                    scale_choices = format_choices(matrix_list_name, choices_df)
                    for choice in scale_choices:
                        content.append(choice)
                    content.append("")
                
                # List items to rate
                content.append("**Tasks to rate:**")
                content.append("")
                for q in matrix_questions:
                    content.append(f"- {q}")
                
                in_matrix = False
                matrix_questions = []
                matrix_list_name = None
            continue
            
        # Handle notes
        if 'note' in str(q_type):
            note_text = row['label'] if pd.notna(row['label']) else ""
            wrapped = wrap_text(note_text)
            if wrapped:
                content.append("")
                content.append(wrapped)
            continue
            
        # Handle matrix questions
        if in_matrix and 'select_one' in str(q_type) and 'likert' in str(q_type):
            matrix_questions.append(row['label'])
            if not matrix_list_name:
                matrix_list_name = extract_list_name(q_type)
            continue
            
        # Handle regular questions
        if pd.notna(row['label']) and 'select' in str(q_type):
            question_label = row['label']
            
            # Add question header if it's substantial
            if len(question_label) > 50 or '\n' in str(question_label):
                content.append(f"\n## {row['name'].replace('_', ' ').title()}")
                content.append("")
            else:
                content.append(f"\n## {question_label}")
                content.append("")
            
            # Question details
            content.append(f"**Question Type:** {get_question_type_description(row)}  ")
            content.append(f"**Required:** {'Yes' if row.get('required') == 'yes' else 'No'}  ")
            
            # Add question text
            question_text = question_label
            if pd.notna(row.get('required_message')):
                question_text += " *"
            content.append(f"**Text:** {question_text}")
            
            # Add hint if present
            if pd.notna(row.get('hint')):
                content.append(f"**Hint:** {row['hint']}")
            
            # Add choices if applicable
            list_name = extract_list_name(q_type)
            if list_name:
                choices = format_choices(list_name, choices_df)
                if choices:
                    content.append("**Options:**")
                    content.append("")
                    for choice in choices:
                        content.append(choice)
                    
        elif pd.notna(row['label']) and q_type == 'text':
            # Handle text questions
            content.append(f"\n## {row['label']}")
            content.append("")
            content.append(f"**Question Type:** {get_question_type_description(row)}  ")
            content.append(f"**Required:** {'Yes' if row.get('required') == 'yes' else 'No'}  ")
            content.append(f"**Text:** {row['label']} {'*' if row.get('required') == 'yes' else ''}")
    
    # Add form submission section
    content.append("\n# Form Submission")
    content.append("")
    content.append("**Submit Button Text:** Submit")
    
    return "\n".join(content)

if __name__ == "__main__":
    # Generate content
    content = generate_content()
    
    # Write to file
    output_path = '/Users/lschoebitz/Documents/gitrepos/context-ds4owd/gh-org-ds4owd-dev/pre-course-survey/forms/survey-content.qmd'
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Generated {output_path}")