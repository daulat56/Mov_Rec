import streamlit as st
import pickle
import pandas as pd
import requests

def get_posters(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0c007a20b54f63bd3427ff10d0ad1248".format(movie_id))
    properties=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ properties['poster_path']


# to recommend the movie we need to write the func similar to earlier one
def recommend_movie(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6] #it will give the tuple of required movies relation with other movies as movie_name and similarity
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movies_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        # to fetch poster of each of the recommended movie we need the movie id        
        recommended_movies_posters.append(get_posters(movies_id))
    return recommended_movies, recommended_movies_posters
    
    

# to import from the jupyter to vs code
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

# to add the selectbox
selected_movie=st.selectbox('What movie would u like to see?',movies['title'].values)

# to add the button to get the selected movie

if st.button('Recommend'):
    movie_to_watch, posters=recommend_movie(selected_movie)
    col1, col2, col3, col4 , col5 = st.columns(5)

    with col1:
        st.text(movie_to_watch[0])
        st.image(posters[0])

    with col2:
        st.text(movie_to_watch[1])
        st.image(posters[1])

    with col3:
        st.text(movie_to_watch[2])
        st.image(posters[2])

    with col4:
        st.text(movie_to_watch[3])
        st.image(posters[3])

    with col5:
        st.text(movie_to_watch[4])
        st.image(posters[4])

 