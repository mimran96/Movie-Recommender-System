import streamlit as st
import pickle
import pandas as pd

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movie_dict)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommened_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommened_movies.append(movies.iloc[i[0]].title)
    return recommened_movies


st.title("Movie Recommender System")

options = movies['title'].values
selected_movie_name = st.selectbox("Choose an Movie name", options)

if st.button('Recommend'):
    recmmdations = recommend(selected_movie_name)
    for i in recmmdations:
        st.write(i)

    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])