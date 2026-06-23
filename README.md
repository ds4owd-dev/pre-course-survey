# Pre-course survey: Data Science for openwashdata

A KoboToolbox [XLSForm](https://xlsform.org/) for the pre-course survey of the
Data Science for openwashdata (DS4OWD) course. It is published as a reusable
open educational resource so that it can be adapted for other courses.

## What the survey collects

The form gathers participant background before the course starts:

- Personal information (name, email, country, GitHub username, ORCID)
- Education and employment
- Barriers to participation
- Technical experience (programming languages, Git, IDEs, LLM tools)
- Learning goals and interest in mentorship
- Consent and acknowledgments

## Repository contents

```
pre-course-survey/
├── forms/
│   └── ds4owd-precourse-survey.xlsx   # The XLSForm (survey, choices, settings)
├── CITATION.cff                        # Citation metadata
└── README.md                           # This file
```

The `.xlsx` file is a standard XLSForm with three sheets:

- `survey` — questions, types, labels, and grouping
- `choices` — choice lists (countries, programming languages, IDEs, LLM tools, education levels)
- `settings` — form title, ID, and metadata

## How to use it

### Deploy on KoboToolbox

1. Sign in to [KoboToolbox](https://www.kobotoolbox.org/).
2. Create a new project and choose to import an XLSForm.
3. Upload `forms/ds4owd-precourse-survey.xlsx`.
4. Review and deploy the form.

### Adapt for your own course

1. Open `forms/ds4owd-precourse-survey.xlsx` in a spreadsheet editor.
2. Edit the `survey`, `choices`, and `settings` sheets to fit your needs.
3. Update the form title and ID on the `settings` sheet.
4. Re-upload to KoboToolbox.

For the XLSForm syntax reference, see [xlsform.org](https://xlsform.org/).

## License

The survey is released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
You are free to reuse and adapt it with attribution.

## Citation

If you reuse this survey, please cite it. See [`CITATION.cff`](CITATION.cff)
for full metadata.

## Course context

This survey is part of the Data Science for openwashdata course. For more about
the course, see the [course website](https://ds4owd-002.github.io/website/).
