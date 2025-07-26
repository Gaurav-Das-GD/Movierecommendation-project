# main.py
import streamlit as st
from movies_.main import movie_list
from recommend import recommend_movies

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

if st.button("Recommend"):
    st.subheader("Recommended Movies:")
    recommendations = recommend_movies(selected_movie)
    for movie in recommendations:
        st.write(movie)
