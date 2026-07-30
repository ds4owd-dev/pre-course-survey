# Pre-course survey: Data Science for openwashdata

The pre-course survey of the Data Science for openwashdata (DS4OWD) course,
available in two formats:

- A [surveydown](https://surveydown.org) survey (`survey.qmd` + `app.R`), an
  open-source, markdown-based survey platform built on R, Quarto, and Shiny
- A KoboToolbox [XLSForm](https://xlsform.org/) (`forms/ds4owd-precourse-survey.xlsx`),
  the original source form

It is published as a reusable open educational resource so that it can be
adapted for other courses.

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
├── survey.qmd                          # surveydown survey (pages, questions, settings)
├── app.R                               # Shiny app: database + conditional display logic
├── choices.R                           # Choice lists generated from the XLSForm
├── forms/
│   └── ds4owd-precourse-survey.xlsx    # The original XLSForm (survey, choices, settings)
├── CITATION.cff                        # Citation metadata
└── README.md                           # This file
```

## Run the surveydown survey

1. Install [R](https://cran.r-project.org/) and [Quarto](https://quarto.org/).
2. Install the surveydown package:

   ```r
   install.packages("surveydown")
   ```

3. Open the project and run the app:

   ```r
   shiny::runApp("app.R")
   ```

By default the survey runs in **preview mode** (`mode: preview` in the
`survey.qmd` YAML header) and stores responses locally in `preview_data.csv`.
To collect real responses, connect a PostgreSQL database (e.g. a free
[Supabase](https://supabase.com/) project):

1. Run `surveydown::sd_db_config()` once to store your database credentials in
   a local `.env` file (git-ignored).
2. Change `mode: preview` to `mode: database` in the `survey.qmd` YAML header.

To deploy the survey online, see the
[surveydown deployment docs](https://surveydown.org/docs/deployment).

### How the XLSForm maps to surveydown

- Each XLSForm `begin_group`/`end_group` block is one survey page.
- Question `name`s are kept as surveydown question `id`s, and choice `name`s
  are kept as stored values, so collected data stays comparable across both
  platforms. The barrier and LLM-frequency question blocks are rendered as
  matrix questions; their rows store to the same column names as the original
  individual questions (e.g. `barrier_time`, `llm_summarization`).
- The `relevant` column (skip logic) is implemented with `sd_show_if()` in
  `app.R`.
- The `required` column is implemented via the `required` list in the
  `survey.qmd` YAML header.
- Not ported (not natively supported by surveydown): the regex `constraint`s
  on the ORCID iD and email fields, and the constraint preventing "None of
  the above" from being combined with other options in multiple-select
  questions.

## Use the original XLSForm on KoboToolbox

1. Sign in to [KoboToolbox](https://www.kobotoolbox.org/).
2. Create a new project and choose to import an XLSForm.
3. Upload `forms/ds4owd-precourse-survey.xlsx`.
4. Review and deploy the form.

For the XLSForm syntax reference, see [xlsform.org](https://xlsform.org/).

## Adapt for your own course

1. Edit the pages and questions in `survey.qmd`.
2. Edit the choice lists in `choices.R`.
3. Adjust the conditional display logic in `app.R`.

## License

The survey is released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
You are free to reuse and adapt it with attribution.

## Citation

If you reuse this survey, please cite it. See [`CITATION.cff`](CITATION.cff)
for full metadata.

## Course context

This survey is part of the Data Science for openwashdata course. For more about
the course, see the [course website](https://ds4owd-002.github.io/website/).
