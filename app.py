import streamlit as st
import pandas as pd
import pickle

st.title("MOVIE RECOMMENDER SYSTEM")

name= st.text_input(
    "ENTER YOUR NAME",
    placeholder= "your name"
)

movie_dict= pickle.load(open('movies_dict.pkl', 'rb'))

movies= pd.DataFrame(movie_dict) 


movie_name= st.selectbox(
    f"HELLO {name}, WHAT MOVIES WOULD YOU LIKE US TO RECOMMEND",
    movies['title'].values
)

similarity= pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    mov_idx= movies[movies['title']== movie].index[0]
    dist= similarity[mov_idx]
    mov_lst= sorted(list(enumerate(dist)), reverse=True, key= lambda x: x[1])[1:6]

    recommended_movies= []
    for i in mov_lst:
        mov_id= i[0]

        ## fetch poster by id ny using api
        recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies

if st.button("RECOMMEND"):
    recommended= recommend(movie_name)
    for i in recommended:
        st.write(i)