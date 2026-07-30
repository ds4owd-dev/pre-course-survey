# Package setup ---------------------------------------------------------------

# Install required packages:
# install.packages("surveydown")

# Load packages
library(surveydown)

# Database setup --------------------------------------------------------------
#
# Details at: https://surveydown.org/docs/storing-data
#
# surveydown stores data on any PostgreSQL database. We recommend
# https://supabase.com/ for a free and easy to use service.
#
# Once you have your database ready, run the following function to store your
# database configuration parameters in a local .env file:
#
# sd_db_config()
#
# This survey currently runs in preview mode (set via `mode: preview` in the
# survey.qmd YAML header), which saves responses locally to preview_data.csv
# instead of a database. To collect real responses, run sd_db_config() to
# store your database credentials, then change `mode` to `database` in the
# survey.qmd YAML header.

db <- sd_db_connect()

# UI setup --------------------------------------------------------------------

ui <- sd_ui()

# Server setup ----------------------------------------------------------------

server <- function(input, output, session) {
  # Conditional display logic, converted from the `relevant` column of the
  # original XLSForm (forms/ds4owd-precourse-survey.xlsx)
  sd_show_if(
    # Show self-description field if gender is "Prefer to self-describe"
    input$gender == "self_describe" ~ "gender_self_describe",

    # Show specification field if accessibility needs is "Yes"
    input$accessibility_needs == "yes" ~ "accessibility_specify",

    # Show organisation questions if employed or self-employed
    input$employment_situation %in%
      c("employed_fulltime", "employed_parttime", "self_employed") ~
      "organisation_name",
    input$employment_situation %in%
      c("employed_fulltime", "employed_parttime", "self_employed") ~
      "org_type",

    # Show LLM usage frequency matrix unless "None of the above" is selected
    # among the LLM tools/platforms
    !("none" %in% input$llm_platforms) ~ "llm",

    # Show browser specification field if browser is "Other"
    input$web_browser == "other" ~ "web_browser_other",

    # Show note-taking tool field if a note-taking tool is used
    input$use_note_taking_tool == "yes" ~ "note_taking_tool_specify"
  )

  # Run surveydown server and define database
  sd_server(db = db)
}

# Launch the app
shiny::shinyApp(ui = ui, server = server)
