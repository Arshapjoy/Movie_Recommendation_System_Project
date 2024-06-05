from flask import Flask, request, render_template
import pickle
import os
import requests

app = Flask(__name__)

# Loading the pickled files
path = 'E:/MCAproject/Movie_Recommendation_System_Project/notebooks/'

with open(os.path.join(path, 'tfidf_vectorizer.pkl'), 'rb') as file:
    tfidf_vectorizer = pickle.load(file)
with open(os.path.join(path, 'cosine_sim.pkl'), 'rb') as file:
    cosine_sim = pickle.load(file)
with open(os.path.join(path, 'subset_df.pkl'), 'rb') as file:
    subset_df = pickle.load(file)

# TMDb API key
YOUR_API_KEY = 'd23da6dcf1ea9800335aba342a81139e'

def content_based_recommendations(title, cosine_sim=cosine_sim, df=subset_df, num_recommendations=10):
    title = title.strip()
    idx = df[df['title'].str.strip().str.lower() == title.lower()].index
    if len(idx) == 0:
        return []
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:]]
    recommended_movies = df['title'].iloc[movie_indices].drop_duplicates()
    unique_recommendations = recommended_movies[recommended_movies != title]
    additional_recommendations_needed = num_recommendations - len(unique_recommendations)
    if additional_recommendations_needed > 0:
        additional_recommendations = df[~df['title'].isin(unique_recommendations) & (df['title'] != title)]['title'].head(additional_recommendations_needed)
        unique_recommendations = unique_recommendations.append(additional_recommendations)
    
    # Fetching poster URLs only for recommended movies
    recommendations = []
    for movie in unique_recommendations[:num_recommendations]:  # Limiting to num_recommendations
        poster_url = get_tmdb_movie_poster(movie, tmdb_api_key)
        if poster_url:
            recommendations.append((movie, poster_url))
    
    return recommendations

def get_tmdb_movie_poster(movie_title, api_key):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(search_url)
    data = response.json()
    
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return poster_url
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    input_title = ""
    input_movie_poster = ""
    recommendations = []
    if request.method == 'POST':
        input_title = request.form['title']
        input_movie_poster = get_tmdb_movie_poster(input_title, tmdb_api_key)
        recommendations = content_based_recommendations(input_title)
    return render_template('index.html', input_title=input_title, input_movie_poster=input_movie_poster, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
