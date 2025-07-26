import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load your dataset
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\movies.csv")

# Create similarity matrix only if it doesn't already exist
similarity_file_path = "data/similarity.csv"

if not os.path.exists(similarity_file_path):
    # Use 'overview' column for text features
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'].fillna(""))

    # Compute cosine similarity matrix
    similarity = cosine_similarity(tfidf_matrix)

    # Save it to CSV
    os.makedirs("data", exist_ok=True)  # Ensure 'data' folder exists
    pd.DataFrame(similarity).to_csv(similarity_file_path, index=False, header=False)

# Load similarity matrix
similarity = pd.read_csv(similarity_file_path, header=None).values


# Movie recommendation function
def recommend_movies(title, n=5):
    if title not in df['title'].values:
        return ["Movie not found in dataset."]

    # Find index of the selected movie
    idx = df[df['title'] == title].index[0]

    # Get similarity scores for this movie with all others
    scores = list(enumerate(similarity[idx]))

    # Sort scores and get top n (excluding itself)
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n + 1]

    # Return top n recommended movie titles
    recommendations = [df.iloc[i[0]]['title'] for i in scores]
    return recommendations

