# Prompt History

## Format: YYYY-MM-DD HH:MM:SS - [Prompt text]

2025-01-07 10:45:00 - The following link is a Google Forms survey. https://forms.gle/r56RpC73yQyVoas19

Your task is to extract all content from this survey as an exact copy of the existing form. Do not summarize or modify any text. Identify the question type. 

Create the following files from the extracted information:

- a Quarto markdown file with docx output for sharing as a collaborative document for review
- file formats for input into KoboToolbox (XLSForm)
- the file format for KoboToolbox input as a machine-readable CSV
- for "Country of residence" questions, include all countries globally in addition to their ISO3c country code as a dropdown question.

Write a CLAUDE.md for the project and include

- that all prompts must be stored in a prompt-history.md with only the date and time of the prompt, not the response.
- all content in markdown and Quarto markdown must be wrapped at 72
- best practices for creating KoboToolbox surveys using