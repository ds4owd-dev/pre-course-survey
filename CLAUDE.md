# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when
working with code in this repository.

## Project Overview

This repository contains a pre-course survey project that involves
extracting Google Forms content and converting it into multiple formats
for data collection and collaboration.

## Key Deliverables

1. **Quarto Markdown Document** - A collaborative review document with
   DOCX output containing the complete survey content
2. **XLSForm** - Excel format for KoboToolbox survey import
3. **CSV Format** - Machine-readable format for KoboToolbox
4. **Country Lists** - Global country list with ISO3c codes for
   dropdown questions

## Important Guidelines

### Prompt History Management
- All prompts must be stored in `prompt-history.md`
- Include only the date and time of the prompt
- Do NOT include the response content
- Format: `YYYY-MM-DD HH:MM:SS - [Prompt text]`

### Text Formatting Standards
- All content in markdown and Quarto markdown must be wrapped at 72
  characters
- Use consistent line breaks for readability
- Preserve exact text from source materials without modification

### KoboToolbox Best Practices

#### Survey Structure
- Use clear, unique names for each question
- Follow naming conventions: lowercase, no spaces, use underscores
- Include question types explicitly in the XLSForm
- Mark required questions appropriately

#### Question Types
- `text` - Open-ended text responses
- `select_one` - Single choice from list
- `select_multiple` - Multiple choices allowed
- `integer` - Numeric whole numbers
- `decimal` - Numeric with decimals
- `date` - Date selection
- `time` - Time selection
- `datetime` - Combined date and time

#### Choice Lists
- Define choices in separate sheet
- Use consistent list naming
- Include both label and name for each choice
- For countries: include country name and ISO3c code

#### Validation Rules
- Add constraints where appropriate
- Include helpful constraint messages
- Test all skip logic thoroughly

#### Best Practices for Data Quality
- Use relevant questions to show/hide based on previous answers
- Add hints to clarify complex questions
- Include "other" options where appropriate
- Set reasonable character limits for text fields

### File Organization
```
pre-course-survey/
├── CLAUDE.md                 # This file
├── prompt-history.md         # Prompt tracking
├── survey-content.qmd        # Quarto document
├── survey-xlsform.xlsx       # KoboToolbox XLSForm
├── survey-choices.csv        # Choice lists
├── survey-questions.csv      # Question definitions
└── countries-iso3c.csv       # Country reference list
```

### Country Data Standards
- Use official country names
- Include all UN-recognized countries
- Add ISO 3166-1 alpha-3 codes
- Sort alphabetically by country name
- Handle special cases (territories, disputed regions) consistently

### Version Control
- Commit survey versions with clear messages
- Tag major revisions
- Document changes in commit messages
- Keep original form content unchanged