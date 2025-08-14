import streamlit as st
import pandas as pd
import numpy as np
import json

# Import modules
from similarity import get_embedding, cosine_similarity
from plotting import create_similarities_plot

# ---------- Helper Functions ----------

def load_data(file_path):
    with open(file_path, 'r', errors='replace') as f:
        return pd.read_csv(f)

def get_display_data(data):
    data['upper_title'] = data['Title'].apply(str.upper)
    return data

def safe_eval(embedding_str):
    try:
        return json.loads(embedding_str.replace('...', ''))
    except json.JSONDecodeError:
        return None

def filter_data(query, data):
    return data[data['upper_title'].str.contains(query, case=False, na=False)]

# ---------- Load and Prepare Data ----------
data = load_data('wikiLex/wikip_ai_glossary.csv')
data = get_display_data(data)
data['High_dimensional_embeddings'] = data['High_dimensional_embeddings'].apply(safe_eval)
data = data.dropna(subset=['High_dimensional_embeddings'])
data_embeddings = np.vstack(data['High_dimensional_embeddings'].values)

# ---------- UI Components ----------
st.header('📖 AI Glossary Explorer')
# st.title('🧠 AI Glossary Explorer')
st.markdown("""<div style='font-size: 20px; line-height: 1.6; margin: 1rem; color: #f5dcdc;'>This model will help you find expliantions and examples of coding terms and also be learning from your queries. And it will also provide related links or terms, to help you understand more your query.</div>""", unsafe_allow_html=True)
user_query = st.text_input('🔍 Enter your query:')

# ---------- Main Logic ----------
if user_query.strip():
    filtered = filter_data(user_query, data)
    query_embedding = get_embedding(user_query)

    if not filtered.empty:
        st.success("🔍 Exact or partial title match found!")
        st.subheader(f"📈 Related Terms based on: '{user_query.upper()}'")

        matched_titles = filtered['Title'].tolist()
        matched_links = filtered['Link'].tolist()
        
        # Compute actual similarity scores for each matched item
        matched_embeddings = np.vstack(filtered['High_dimensional_embeddings'].values)
        raw_similarities = [cosine_similarity(np.array(query_embedding).reshape(1, -1), np.array(emb).reshape(1, -1))[0][0] for emb in matched_embeddings]
        


        # Keep all results and sort them
        scored_results = [(title, link, sim) for title, link, sim in zip(matched_titles, matched_links, raw_similarities)]
        scored_results.sort(key=lambda x: x[2], reverse=True)
        top_results = scored_results[:5]
        top_titles, top_links, top_similarities = zip(*top_results)
        similarities_percentages = np.array(top_similarities) * 100

        if len(top_titles) == 1:
            st.info("This match was found in the glossary.")
            st.markdown(f"- [{top_titles[0]}]({top_links[0]}) — **{top_similarities[0] * 100:.2f}% match**")
        elif len(top_titles) == 2:
            st.info("This match was found in the glossary.")
            st.markdown(f"- [{top_titles[0]}]({top_links[0]}) — **{top_similarities[0] * 100:.2f}% match**")
            st.markdown(f"- [{top_titles[1]}]({top_links[1]}) — **{top_similarities[1] * 100:.2f}% match**")
        else:
            fig = create_similarities_plot(top_titles, similarities_percentages, top_links, user_query)
            st.plotly_chart(fig, use_container_width=True)
        

        st.markdown(f"### 🔗 Related Terms for: '{user_query.upper()}'")
        for title, link, sim in zip(top_titles, top_links, top_similarities):
            sim_score = sim * 100
            st.markdown(f"- [{title}]({link}) — **{sim_score:.2f}% match**")

            if st.checkbox(f"View Description for {title}", key=title):
                description = filtered[filtered['Title'] == title]['Wikipedia_page_description'].values[0]
                st.write(description)

    else:
        st.warning("No matching terms found. Try a different query.")

# ---------- Sidebar ----------
with st.sidebar:
    st.title("📖 Browse All Titles")
    st.markdown('<style>.stRadio {overflow-y: auto; height: 600px;}</style>', unsafe_allow_html=True)
    selection = st.radio('Select a title:', ['Select a title...'] + data['upper_title'].tolist())

if selection and selection != 'Select a title...':
    selected_data = data[data['upper_title'] == selection].iloc[0]
    st.header("📌 Selected Glossary Entry")
    st.write(f"**{selected_data['Title']}**")
    st.write(selected_data['Link'])
    if st.checkbox('View Description'):
        st.write(selected_data['Wikipedia_page_description'])
