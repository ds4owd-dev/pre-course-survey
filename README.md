# Google Form to KoboToolbox XLSForm Conversion

This project documents the complete process of extracting content from a
Google Form and converting it into a fully functional XLSForm for
KoboToolbox deployment.

## Project Overview

**Original Source:** Google Forms pre-course survey for Data Science for
OpenWashData (DS4OWD) course iteration 002  
**Target Output:** KoboToolbox-compatible XLSForm with complete content
preservation  
**Duration:** Approximately 1 hour 6 minutes (14:36-15:42)  
**Total Commits:** 11 (8 by Claude, 3 by user)

## Process Summary

### Phase 1: Initial Content Extraction (14:36-14:40)
- Extracted basic survey structure from Google Form
- Created initial Quarto document for review
- Generated baseline CSV files for KoboToolbox
- Created project documentation (CLAUDE.md, prompt-history.md)

### Phase 2: Content Verification and Enhancement (14:40-15:00)
- **Critical Discovery:** Initial extraction missed significant content
- Added complete technical skills questions (programming languages, Git,
  IDEs, LLMs)
- Expanded choice lists from 23 to 34 LLM tools
- Added detailed programming experience questions
- Enhanced IDE options from 5 to 12 environments

### Phase 3: XLSForm Generation and Debugging (15:00-15:20)
- Created Python script to generate Excel files from CSV
- **Major Challenge:** CSV formatting issues with commas in text fields
- Fixed column count mismatches (21 header vs 22 data columns)
- Resolved group syntax issues (begin_group → "begin group")
- Changed acknowledge question type to select_one with yes_only choices

### Phase 4: Complete Content Integration (15:20-15:34)
- Added full Google Form description (course details, signup steps)
- Integrated all response examples from detailed .qmd analysis
- Enhanced education level choices with specific examples
- Added platform-specific CLI descriptions
- Included detailed LLM task examples with real use cases

### Phase 5: KoboToolbox Compatibility Fixes (15:34-15:42)
- Resolved multiline text formatting issues
- Fixed XPath expression errors in instance naming
- Eliminated deployment validation errors
- Final compatibility testing and verification

## Key Challenges and Solutions

### 1. Content Completeness Verification
**Challenge:** Initial extraction missed substantial content including
detailed examples and technical question categories.

**Solution:** Implemented iterative verification process comparing Google
Form content with generated files. Created intermediate .qmd file to
capture all content for systematic review.

### 2. CSV Format Compatibility
**Challenge:** Text fields containing commas, quotes, and special
characters broke CSV parsing.

**Solution:** Implemented proper CSV quoting standards, escaped special
characters, and added column count validation to prevent structure
mismatches.

### 3. XLSForm Syntax Requirements
**Challenge:** KoboToolbox has strict requirements for group syntax,
question types, and XPath expressions.

**Solution:** 
- Changed `begin_group`/`end_group` to `begin group`/`end group`
- Replaced unsupported `acknowledge` type with `select_one yes_only`
- Simplified instance naming to avoid XPath validation errors

### 4. Multiline Content Handling
**Challenge:** Questions with multiline descriptions (e.g., CLI usage)
caused parsing errors in KoboToolbox.

**Solution:** Converted multiline content to single-line format while
preserving all information about platform-specific differences.

## File Organization

### Project Structure
```
pre-course-survey/
├── README.md                    # This file - complete documentation
├── CLAUDE.md                    # Development guidelines and lessons learned
├── pre-course-survey.Rproj      # R project configuration
├── forms/                       # Final survey forms and review documents
│   ├── ds4owd_precourse_survey.xlsx   # **Final XLSForm for KoboToolbox**
│   └── survey-content.qmd             # Human-readable content for review
├── data/                        # Source data and configuration files
│   ├── survey-questions.csv           # Survey structure and questions
│   ├── survey-choices.csv             # All choice lists with examples
│   ├── survey-settings.csv            # Form metadata and description
│   └── countries-iso3c.csv            # Complete country reference
├── scripts/                     # Development and build tools
│   └── create_xlsform.py              # Python script to generate XLSForm
└── docs/                        # Process documentation
    └── prompt-history.md              # Complete prompt tracking log
```

### File Categories

#### **Forms** (`forms/`)
- **Production Files:** Ready-to-deploy survey forms
- **Review Documents:** Human-readable content for collaboration

#### **Data** (`data/`)
- **Source Files:** CSV components for XLSForm generation
- **Reference Data:** Supporting data like country codes

#### **Scripts** (`scripts/`)
- **Build Tools:** Automation scripts for form generation
- **Utilities:** Development and validation helpers

#### **Documentation** (`docs/`)
- **Process Records:** Detailed development history
- **Reference Materials:** Supporting documentation

## Survey Content Statistics

### Question Categories
- **Personal Information:** 6 questions (GitHub, ORCID, email, name,
  country)
- **Education & Employment:** 4 questions with detailed examples
- **Barriers to Participation:** 6 barrier assessment questions
- **Technical Experience:** 15 questions covering programming, tools,
  and platforms
- **Project Participation:** 3 questions about goals and mentorship
- **Agreements:** 2 consent/acknowledgment questions

### Choice Lists
- **Countries:** 196 countries with ISO3c codes
- **Programming Languages:** 23 languages and tools
- **LLM Platforms:** 34 AI tools and platforms
- **IDE Options:** 12 development environments
- **Education Levels:** 8 levels with detailed examples

### Content Preservation
- **Complete Description:** Full course information, meeting schedule,
  signup instructions
- **Detailed Examples:** Every choice includes relevant examples (e.g.,
  "Bachelor's degree (e.g. BA, BSc, BEng)")
- **Platform Specifics:** OS-specific instructions for CLI usage
- **Use Case Examples:** Real examples for each LLM task category

## Deployment Instructions

### For KoboToolbox
1. Go to [KoboToolbox](https://www.kobotoolbox.org/)
2. Create new project
3. Upload `forms/ds4owd_precourse_survey.xlsx`
4. Deploy form

### For Local Development
```bash
# Regenerate XLSForm from CSV files
python3 scripts/create_xlsform.py

# Render survey content for review
quarto render forms/survey-content.qmd
```

## Lessons Learned

### Content Extraction Best Practices
1. **Always verify completeness** - Initial extraction often misses
   nuanced content
2. **Use intermediate formats** - .qmd files help verify content
   preservation
3. **Cross-reference systematically** - Compare original with generated
   files section by section

### XLSForm Development Guidelines
1. **Test early and often** - KoboToolbox validation catches issues not
   visible in Excel
2. **Handle special characters carefully** - Proper CSV quoting is
   essential
3. **Keep XPath expressions simple** - Complex expressions often fail
   validation
4. **Use supported question types** - Stick to documented KoboToolbox
   question types

### Project Management Insights
1. **Document every iteration** - Prompt history proved invaluable for
   debugging
2. **Commit frequently** - Small, focused commits make debugging easier
3. **Version control everything** - Including intermediate files during
   development

## Technical Specifications

**Source Format:** Google Forms  
**Intermediate Format:** Quarto Markdown (.qmd) + CSV files  
**Target Format:** XLSForm (.xlsx)  
**Validation:** KoboToolbox ODK Validate  
**Dependencies:** Python 3, pandas, openpyxl

## Project Statistics

- **Development Time:** ~66 minutes
- **Total Commits:** 11
- **Claude Commits:** 8 (automated development)
- **User Commits:** 3 (manual verification and guidance)
- **Files Generated:** 10+ including documentation
- **Questions Captured:** 36 across 6 categories
- **Choice Options:** 300+ with detailed examples

This project demonstrates the complexity of accurately preserving survey
content while adapting to different platform requirements, highlighting
the importance of systematic verification and iterative refinement in
form migration projects.