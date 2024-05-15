import streamlit as st
import pandas as pd
import numpy as np
import json

# Importing functions from other modules
from data_processing import load_data
from similarity import get_embedding, find_most_similar_embeddings
from plotting import create_similarities_plot


# Function to load the CSV file and handle null bytes
def load_data(file_path):
    with open(file_path, 'r', errors='replace') as f:
        data = pd.read_csv(f)
    return data

# Function to process and retrive data from the dataset
def get_display_data(data):
    data['upper_title'] = data['Title'].apply(str.upper)
    return data

# Function to safely convert string embeddings to list
def safe_eval(embedding_str):
    try:
        return json.loads(embedding_str.replace('...', ''))  # Handle malformed strings
    except json.JSONDecodeError:
        return None  # Handle or log the error as needed

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# Load the dataset
data = load_data('wikiLex/wikip_ai_glossary.csv')


processed_data = get_display_data(data)

# Apply the function and filter out any None values
processed_data['High_dimensional_embeddings'] = processed_data['High_dimensional_embeddings'].apply(safe_eval)
processed_data = processed_data.dropna(subset=['High_dimensional_embeddings'])

# Ensure embeddings are precomputed and loaded
data_embeddings = np.vstack(processed_data['High_dimensional_embeddings'].values)

with features:
    st.header('Features Created from Lexicon')

with model_training:
    st.header('Model Training')
    st.write('This model will help you find expliantions and examples of coding terms and also be learning from your queries. And it will also provide related links or terms, to help you understand more your query.')




# Search for Similar Documents
st.title('Similar documents based on Query: ')
user_query = st.text_input('Enter your query: ')

if user_query:
    query_embedding = get_embedding(user_query)
    top_indices, similarities = find_most_similar_embeddings(query_embedding, data_embeddings, top_k=6)

    # Extracting titles and links for the similar documents
    titles = processed_data['Title'].iloc[top_indices].tolist()
    links = processed_data['Link'].iloc[top_indices].tolist()

    fig = create_similarities_plot(titles, similarities, links, user_query)
    st.plotly_chart(fig, use_container_width=True)

    # Display clickable top similar documents
    st.write('Click on a document to learn more about the similar documents:')
    for title, link , similarities_percentages in zip(titles, links, similarities):
        # Convert Similaritys to Percentages
        similarities_percentages = similarities_percentages * 100
        st.markdown(f"[{title}]({link}) - {similarities_percentages:.2f} %")


# Based on the user text query
def filter_data(query, data):
    return data[data['upper_title'].str.contains(query, case=False, na=False)]
 
if user_query:
    filtered_data = filter_data(user_query, processed_data)
    if not filtered_data.empty:
        st.title('Search results: ')
        for index, row in filtered_data.iterrows():
            st.write(f"{row['upper_title']}")
            st.write(f"{row['Link']}")
            if st.checkbox(f'View Description for {row["upper_title"]}'):
                st.write(f"{row['Wikipedia_page_description']}")
        
    else:
        st.write('No results found. Please try again with different keywords.')




# Sidebar for selecting titles with a scrollable radio button list
with st.sidebar:
    st.title("Browse Titles:")
     # Apply CSS through markdown to affect sidebar elements
    st.markdown('''
                <style>
                .stRadio {overflow-y: auto; !important; height: 600px}
                </style> 
                ''', unsafe_allow_html=True)
    selected_title = st.radio('Select a title: ',['Select a title...'] + processed_data['upper_title'].tolist(), key='title_radio')

# Display the selected title
if selected_title and selected_title != 'Select a title...':
    st.title('Selected Information from Sidebar') 
    selected_data = processed_data[processed_data['upper_title'] == selected_title].iloc[0]
    st.write(f"{selected_data['upper_title']}")
    st.write(f"{selected_data['Link']}")
    if st.checkbox('View Description'):
        st.write(f"****Description****: {selected_data['Wikipedia_page_description']}")




