# Prompt-to-SQL App

This is a simple Streamlit app that converts natural language questions into SQL queries using the Google Gemini language model and retrieves data from an SQLite database. The app is deployed on Hugging Face Spaces.

## Features
- Convert natural language questions into SQL queries.
- Query an SQLite database (`student.db`) with columns such as `NAME`, `CLASS`, and `SECTION`.
- Display the results in a table format using Streamlit.

## Live Demo

You can try the live demo hosted on Hugging Face Spaces:

[![Hugging Face Spaces](https://img.shields.io/badge/HuggingFace-Spaces-yellow)](https://huggingface.co/spaces/PR-HARIHARAN/Prompt_TO_Sql)

## Installation

To run the app locally, you'll need to have Python installed on your machine. Follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/PR-HARIHARAN/Prompt_To_Sql.git
   cd Prompt_To_Sql
