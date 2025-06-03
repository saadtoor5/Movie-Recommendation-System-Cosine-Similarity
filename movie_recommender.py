#Importing Libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Dataset with genres 
data = pd.read_csv('movie_genre_dataset.csv')
data.head()

#Define the TF-IDF Vectorizer to transform the genre text into vectors
tfidf = TfidfVectorizer(stop_words='english')
#Fit and transform the genre column into a matrix of TF-IDF Features
tfidf_matrix = tfidf.fit_transform(data['genre'])
#Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on cosine similarity
def get_recommendations(title, cosine_sim=cosine_sim, data=data):
    # Convert movie titles to lowercase for case-insensitive match
    title = title.lower()

    # Match the input title with the dataset
    matches = data[data['title'].str.lower() == title]

    if matches.empty:
        print(f"\n❌ No movie found with the title '{title}' in the dataset.")
        return []

    # Get the index of the matched movie
    idx = matches.index[0]

    # Get pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the scores and exclude the first one (which is the movie itself)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:3]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the recommended movie titles
    return data['title'].iloc[movie_indices].tolist()


#User Input
movie_title = input("Enter a Movie title: ")
recommended_movies = get_recommendations(movie_title)

#Printing recomended movies
if recommended_movies:
    print(f"\n🎬 Movies recommended for '{movie_title}':")
    for movie in recommended_movies:
        print(f" - {movie}")