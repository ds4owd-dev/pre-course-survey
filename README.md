# Pre-course Survey for DS4OWD 002

This repository contains the pre-course survey materials for the Data
Science for OpenWashData (DS4OWD) course, iteration 002.

## Files Overview

### Survey Content
- `survey-content.qmd` - Quarto document with complete survey content
  for review (can be rendered to DOCX format)

### KoboToolbox Files
- `ds4owd_precourse_survey.xlsx` - Ready-to-upload XLSForm for
  KoboToolbox
- `survey-questions.csv` - Survey structure and questions
- `survey-choices.csv` - Choice lists for multiple choice questions
- `survey-settings.csv` - Form settings and metadata
- `countries-iso3c.csv` - Reference list of all countries with ISO3c
  codes

### Utilities
- `create_xlsform.py` - Python script to generate XLSForm from CSV
  files

## Deploying to KoboToolbox

1. Go to [KoboToolbox](https://www.kobotoolbox.org/)
2. Log in or create an account
3. Click "New Project"
4. Select "Upload an XLSForm"
5. Upload `ds4owd_precourse_survey.xlsx`
6. Review and deploy the form

## Survey Structure

The survey contains the following sections:

1. **Personal Information**
   - GitHub username
   - ORCID iD
   - Email address
   - Name
   - Country of residence

2. **Education and Employment**
   - Education level
   - Employment situation
   - Organisation details

3. **Barriers to Participation**
   - Time availability
   - Supervisor interests
   - Technical access (internet, electricity, computer, screen)

4. **Technical Experience**
   - Programming experience (general, R, Python)
   - Other programming languages
   - Git/GitHub experience
   - Data storage formats
   - Document writing approaches
   - IDE usage
   - Command-line interface proficiency
   - Large Language Model usage

5. **Project and Course Participation**
   - Learning goals
   - Data availability for capstone project
   - Mentorship programme interest

6. **Agreements and Consent**
   - Code of Conduct acknowledgment
   - Data privacy consent

## Modifying the Survey

To modify the survey:

1. Edit the appropriate CSV files:
   - `survey-questions.csv` for questions
   - `survey-choices.csv` for answer options
   - `survey-settings.csv` for form settings

2. Regenerate the XLSForm:
   ```bash
   python3 create_xlsform.py
   ```

3. Upload the new `ds4owd_precourse_survey.xlsx` to KoboToolbox

## Important Notes

- All text containing commas must be enclosed in double quotes in CSV
  files
- The ORCID iD field includes regex validation
- Email field includes format validation
- Country list includes all UN-recognized countries with ISO3c codes
- Code of Conduct URL: https://ds4owd-002.github.io/website/code_of_conduct.html

## Data Privacy

Survey responses will be:
- Used for course administration and management
- Accessed only by instructors
- Securely stored
- Not shared with third parties
- Anonymized for reporting (ORCID iD and GitHub username removed)
- Potentially used for future research to improve the course