import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Fill missing values
df['listed_in'] = df['listed_in'].fillna('')
df['description'] = df['description'].fillna('')

# Combine important features
df['content'] = df['listed_in'] + " " + df['description']

# Convert text to vectors
vectorizer = CountVectorizer(stop_words='english')
matrix = vectorizer.fit_transform(df['content'])

# Compute similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(title):
    title = title.lower()
    indices = df[df['title'].str.lower() == title].index

    if len(indices) == 0:
        return "Title not found"

    idx = indices[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i in scores[1:6]:
        recommendations.append(df.iloc[i[0]]['title'])

    return recommendations


# Example
print("Recommendations for 'Narcos':")
print(recommend("Narcos"))
