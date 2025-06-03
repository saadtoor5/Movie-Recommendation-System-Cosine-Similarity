# 🎬 Movie Recommendation System using Cosine Similarity

A simple content-based recommender that suggests similar movies based on genre similarity using TF-IDF and cosine similarity.

---

## 🧠 About the Project

This project demonstrates how to build a **content-based movie recommendation system** using **TF-IDF Vectorization** and **Cosine Similarity**. The model recommends the most similar movies to a given title based on genre descriptions. Now with improved **case-insensitive title matching** and **clearer user feedback**!

---

## 🚀 Features

* 🧾 Genre-based movie similarity detection
* 🔍 TF-IDF vectorization for text representation
* 📐 Cosine similarity to measure closeness
* ✅ Case-insensitive movie search
* ❌ User feedback for unmatched titles
* 🎯 Easy user input for recommendations

---

## 🛠️ Tech Stack

* Python 3.x
* pandas
* scikit-learn

---

## 📁 Project Structure

```
movie-recommendation-system/
├── movie_recommender.py        # Main script
├── movie_recommender.ipynb     # Main script
├── movie_genre_dataset.csv     # Sample dataset
├── README.md                   # Project overview
├── LICENSE                     # MIT License
├── requirements.txt            # Required libraries
└── images/
    └── output_sample.png       # Screenshot of results (optional)
```

---

## 💻 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/saadtoor5/movie-recommendation-system.git
cd movie-recommendation-system
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Script**

```bash
python movie_recommender.py
```

4. **Input a Movie Title** when prompted to get 2 genre-similar recommendations.

---

## 📷 Sample Output

```
Enter a Movie title: The Little Mermaid

🎬 Movies recommended for 'The Little Mermaid':
 - Moana
 - Finding Nemo
```

If the movie isn't found:

```
Enter a Movie title: Unknown Movie

❌ No movie found with the title 'unknown movie' in the dataset.
```

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Made with ❤️ by [@saadtoor5](https://github.com/saadtoor5)

Feel free to fork, explore, or contribute!
