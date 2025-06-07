import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import duckdb

conn = duckdb.connect('/workspace/netflix-dbt-project/database/netflix_db.duckdb')

st.title("Netflix Movie Dashboard")

# Movie Type
st.subheader('Movie Type')
st.markdown("Displays the most common types (genres) of movies available on Netflix. It shows how content is categorized, helping identify viewer preferences and genre dominance.")
query = "SELECT * FROM movie_type"
movie_type = conn.execute(query).fetchdf()
st.bar_chart(movie_type.set_index('listed_in')['total'])

# Content By Country
st.subheader('Content By Country')
st.markdown("Shows the number of Netflix movies produced or attributed to each country. It helps us understand which countries contribute the most content to the Netflix library.")
query = "SELECT * FROM content_by_country"
content_by_country = conn.execute(query).fetchdf()
st.bar_chart(content_by_country.set_index('country')['content_count'])

# Content Strategy Shift Over The Years
st.subheader('Content Strategy Shift Over The Years')
st.markdown("Illustrates how Netflix's content strategy has evolved over time, comparing the number of movies and TV shows added each year.")
query = "SELECT * FROM content_strategy_shift_over_the_years"
content_strategy_shift_over_the_years = conn.execute(query).fetchdf()
pivot_df = content_strategy_shift_over_the_years.pivot(index='year_added', columns='type', values='count').fillna(0)
st.line_chart(pivot_df)

# Frequent Director
st.subheader('Frequent Director')
st.markdown("Displays the directors who have the most content listed on Netflix. It reflects both popularity and production frequency of directors in the platform's catalog.")
query = "SELECT * FROM frequent_director"
frequent_director = conn.execute(query).fetchdf()
st.bar_chart(frequent_director.set_index('director')['count'])

# Frequent Movie Type
st.subheader('Frequent Movie Type')
st.markdown("Shows the distribution of movie types (genres) that appear most frequently on Netflix, giving a quick visual breakdown of genre prevalence.")
query = "SELECT * FROM frequent_movie_type"
frequent_movie_type = conn.execute(query).fetchdf()
fig = px.pie(
    frequent_movie_type,
    names='type',
    values='count',
)
st.plotly_chart(fig)
