import pandas as pd
import duckdb

def extract_data_from_csv():
    try:
        df = pd.read_csv('netflix_titles.csv')
        print("Data extracted succesfully")
    except Exception as e:
        print("Unable to load data because of {e}")

    df['year_added'] = df['date_added'].str.split(',').str.get(1)
    df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
    return df
data = extract_data_from_csv()

def load_to_db(data):
    try:
        df = data.where(pd.notnull(data), None) # Clean NaNs 
        data = list(df.itertuples(index=False, name=None))  # Convert to list of tuples
    except Exception as e:
        print(f"Error {e}")
        return  
    
    try:
        conn = duckdb.connect('/workspace/netflix-dbt-project/database/netflix_db.duckdb')
        conn.sql('''
            CREATE TABLE IF NOT EXISTS netflix_table(
                show_id VARCHAR,
                type VARCHAR,
                title VARCHAR,
                director VARCHAR,
                "cast" VARCHAR,
                country VARCHAR,
                date_added DATE,
                release_year INT,
                rating VARCHAR,
                duration VARCHAR,
                listed_in VARCHAR,
                description VARCHAR,
                year_added INT
            )
        ''')
        conn.executemany(
            '''INSERT INTO netflix_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            data
        )
        conn.commit()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
load_to_db(data)