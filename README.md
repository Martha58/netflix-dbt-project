# End-to-End dbt Project: CSV Ingestion, DuckDB Storage, Business Insights, and Streamlit Visualization

This project demonstrates a complete workflow that:

- Ingests data from a CSV file
- Preprocesses and loads the data into a DuckDB database
- Uses dbt to transform and model the data to answer business questions
- Visualizes the results in a Streamlit dashboard

---

## Step 1: Setup Development Environment

Create and activate a Python virtual environment to isolate dependencies.

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows PowerShell
```

---

## Step 2: Install Dependencies

Install all required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Step 3: Data Ingestion and Preprocessing

- Load the raw CSV file.
- Extract relevant features (e.g., extract `year` from `date_added`).
- Convert `date_added` column to proper date format to ensure compatibility with DuckDB and dbt.

> **Note:** The full data extraction and preprocessing logic is implemented in `main.py`.

---

## Step 4: Initialize DuckDB Storage

- Create a `database` directory to store your DuckDB database file.
- Write a dedicated function to load the cleaned data into the DuckDB database.

---

## Step 5: Initialize and Configure dbt Project

- Create a new dbt project by running:

```bash
dbt init project_name
```

- When prompted, select `1` to configure DuckDB as your database adapter.
- Navigate into the project directory:

```bash
cd project_name
```

- Edit the `profiles.yml` file with the DuckDB configuration. This file is typically located at `~/.dbt/profiles.yml` (create it if it doesn’t exist):

```yaml
project_name:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: ../database/your_database.duckdb
```

- Validate your configuration by running:

```bash
dbt debug
```

---

## Step 6: Build dbt Models

- Place your SQL transformation models inside the `models/` directory.
- Write SQL queries that transform raw data into business-ready datasets.
- Run dbt to apply transformations and materialize the models in DuckDB:

```bash
dbt run
```

---

## Step 7: Visualize with Streamlit

- Use Streamlit to build an interactive dashboard for your business questions.
- Connect Streamlit to your DuckDB database to query the transformed data.
- Deploy your Streamlit app locally or to a cloud platform.

---
