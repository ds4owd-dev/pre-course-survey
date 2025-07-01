# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when
working with this Google Form to KoboToolbox conversion project.

## Project Overview

This repository contains a complete Google Forms to KoboToolbox XLSForm
conversion project for the DS4OWD pre-course survey. The project
demonstrates best practices for content extraction, format conversion,
and platform compatibility resolution.

## Key Deliverables

1. **XLSForm** - `forms/ds4owd_precourse_survey.xlsx` for KoboToolbox
   deployment
2. **Quarto Document** - `forms/survey-content.qmd` for collaborative
   review
3. **CSV Components** - Modular files in `data/` for XLSForm generation
4. **Documentation** - Complete process documentation and lessons
   learned

## Critical Success Factors

### Content Completeness Verification
- **ALWAYS verify initial extraction completeness** - First attempts
  often miss 30-50% of content
- Use intermediate formats (.qmd) to systematically compare with source
- Cross-reference every section, choice list, and example
- Pay special attention to detailed examples and platform-specific
  instructions

### Prompt History Management
- All prompts must be stored in `prompt-history.md`
- Include only the date and time of the prompt, not responses
- Format: `YYYY-MM-DD HH:MM:SS - [Prompt text]`
- Track decision points and iterative improvements

### Text Formatting Standards
- All markdown content must be wrapped at 72 characters
- Preserve exact text from source materials without modification
- Handle special characters (commas, quotes) with proper CSV escaping
- Convert multiline content to single-line for XLSForm compatibility

## XLSForm Development Best Practices

#### KoboToolbox Compatibility Requirements
- Use `begin group` and `end group` (with spaces) not underscores
- Avoid unsupported question types like `acknowledge`
- Use `select_one yes_only` for agreement questions
- Keep XPath expressions simple - avoid complex calculations
- Test multiline content by converting to single-line format
- Ensure CSV column counts match between header and data rows

#### Common Pitfalls and Solutions
1. **CSV Parsing Errors**
   - Quote all text containing commas, quotes, or line breaks
   - Add dummy columns if data rows exceed header column count
   - Use proper escape sequences for special characters

2. **Question Type Compatibility**
   - Replace `acknowledge` with `select_one yes_only`
   - Use supported constraint formats: `regex(., 'pattern')`
   - Test all question types in KoboToolbox before final deployment

3. **XPath Expression Issues**
   - Use simple field references: `/data/field_name`
   - Avoid complex concatenations in instance names
   - Test expressions with KoboToolbox validation

### Development Workflow

#### Phase 1: Content Extraction
1. Extract initial structure from Google Form
2. Create comprehensive .qmd file for review
3. Generate baseline CSV files
4. **Critical:** Verify completeness against original

#### Phase 2: Content Enhancement
1. Add missing sections and detailed examples
2. Expand choice lists with proper labels
3. Include platform-specific instructions
4. Preserve all original formatting and examples

#### Phase 3: XLSForm Generation
1. Create Python script for CSV-to-Excel conversion
2. Handle CSV formatting and special characters
3. Test XLSForm structure and syntax
4. Debug compatibility issues systematically

#### Phase 4: Validation and Deployment
1. Upload to KoboToolbox for validation
2. Fix ODK validation errors iteratively
3. Test deployment and form functionality
4. Document all solutions for future reference

### File Organization
```
pre-course-survey/
├── README.md                          # Complete process documentation
├── CLAUDE.md                          # This file
├── pre-course-survey.Rproj            # R project config
├── forms/                             # Final survey forms
│   ├── ds4owd_precourse_survey.xlsx   # Final XLSForm
│   └── survey-content.qmd             # Content review document
├── data/                              # Source data and configuration
│   ├── survey-questions.csv           # Survey structure
│   ├── survey-choices.csv             # Choice lists
│   ├── survey-settings.csv            # Form metadata
│   └── countries-iso3c.csv            # Country reference
├── scripts/                           # Development tools
│   └── create_xlsform.py              # Generation script
└── docs/                              # Process documentation
    └── prompt-history.md              # Prompt tracking
```

### Quality Assurance Checklist

#### Content Verification
- [ ] All original sections included
- [ ] Choice lists complete with examples
- [ ] Platform-specific instructions preserved
- [ ] Original description and instructions intact

#### Technical Validation
- [ ] CSV files parse correctly
- [ ] XLSForm uploads to KoboToolbox successfully
- [ ] Form deploys without ODK validation errors
- [ ] All question types render properly

#### Documentation Standards
- [ ] README.md documents complete process
- [ ] Commit messages describe specific changes
- [ ] Prompt history tracks all interactions
- [ ] CLAUDE.md updated with lessons learned

### Lessons Learned from This Project

1. **Content extraction is iterative** - First attempts often miss
   significant portions
2. **Platform compatibility is complex** - Each system has specific
   requirements
3. **CSV formatting is critical** - Small errors cause major failures
4. **Systematic verification is essential** - Manual cross-checking
   prevents data loss
5. **Documentation prevents repetition** - Good docs save time on
   similar projects

### Emergency Debugging Commands
```bash
# Check CSV structure
python3 -c "import pandas as pd; print(pd.read_csv('data/survey-questions.csv').shape)"

# Validate column consistency
grep -o ',' data/survey-questions.csv | wc -l

# Test XLSForm generation
python3 scripts/create_xlsform.py

# Check for problematic characters
grep -P '[^\x00-\x7F]' data/survey-*.csv
```