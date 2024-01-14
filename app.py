import pandas as pd
import streamlit as st
import pickle
import requests
import utils


utils.set_background(r"C:\\Users\\yash mohite\\OneDrive\Desktop\\movie recommender system\\Netflix.jpg")

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=cc761486d13444714cc8b56941279ebf".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id


        # fetch poster from API
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters


movie_dict = pickle.load(open("C:\\Users\\yash mohite\\OneDrive\\Desktop\\movie recommender system\\notebook\\movie_dict.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("C:\\Users\\yash mohite\\OneDrive\\Desktop\\movie recommender system\\notebook\\similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
"Which movie you want to watch",
(movies["title"].values))

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2 , col3 ,col4, col5, col6 = st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col6:
        st.text(names[5])
        st.image(posters[5])


