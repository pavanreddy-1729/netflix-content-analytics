🎬 Netflix Content Analytics & Recommendation System




📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on Netflix movies and TV shows and builds a Content-Based Recommendation System using Python.

The goal is to analyze trends in Netflix content and recommend similar titles based on metadata such as genre, cast, and description.

This project demonstrates data analysis, visualization, and machine learning skills commonly used in real-world data science workflows.

📊 Dataset

Dataset contains information about Netflix titles including:

Title

Type (Movie / TV Show)

Director

Cast

Country

Release Year

Rating

Duration

Genre

Description

📈 Exploratory Data Analysis

The following insights were generated during analysis:

✔ Movies vs TV Shows distribution
✔ Content growth over the years
✔ Most common genres on Netflix
✔ Country-wise content production
✔ Trend analysis of Netflix releases

📊 Sample Visualization

Example visualization generated in the project:

Movies vs TV Shows Distribution

Movies  █████████████████████████████
TV Shows ███████████

Saved in:

visualizations/movies_vs_tvshows.png
🤖 Recommendation System

A content-based recommendation system was built using:

CountVectorizer

Cosine Similarity

Feature engineering on content metadata

The system recommends similar shows based on content features.

Example

Input:

Narcos

Output:

Narcos: Mexico
El Chapo
Ganglands
Sin senos no hay paraíso
The Eagle of El-Se'eed
🛠 Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

📂 Project Structure

netflix-content-analytics
│

├── data
│   └── netflix_titles.csv

├── notebooks
│   └── netflix_analysis.ipynb

├── visualizations
│   └── movies_vs_tvshows.png

├── recommendation
│   └── recommendation_system.py
│
└── README.md

⚙️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/pavanreddy-1729/netflix-content-analytics.git

2️⃣ Navigate to project folder
cd netflix-content-analytics

3️⃣ Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

4️⃣ Run the recommendation system
python recommendation/recommendation_system.py

🚀 Future Improvements

Deploy recommendation system using Streamlit

Build interactive Power BI dashboard

Add NLP-based recommendation system

Integrate with real-time movie APIs

👨‍💻 Author

Pavan Kumar

GitHub:
https://github.com/pavanreddy-1729

⭐ Support

If you like this project, please ⭐ the repository on GitHub.
