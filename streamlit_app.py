import streamlit as st
import pandas as pd
import json

# Function to load JSON data
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load data from JSON files
reduced_data = load_json('reduced_datas.json')
mapped_data = load_json('mapped_datas.json')

# Convert JSON data to DataFrames
reduced_df = pd.DataFrame(reduced_data)
mapped_df = pd.DataFrame(mapped_data)

# Streamlit app
st.title('YouTube Comments Data')

# Display reduced datas
st.subheader('Reduced Data')
st.write(reduced_df)

# Display mapped datas
st.subheader('Mapped Data')
st.write(mapped_df)
