# Movie_Recommendation_System_Project

Welcome to the Movie Recommendation System project repository! This project aims to develop a content-based movie recommendation system utilizing data from Rotten Tomatoes. By analyzing various movie features such as audience scores, critic reviews, genres, directors, and more, the system provides personalized recommendations tailored to individual preferences.

## Project Structure

1. **Datasets/**: This directory contains the Rotten Tomatoes datasets used for the project.
   - `rotten_tomatoes_movies.csv`: Dataset containing movie information such as titles, audience scores, genres, directors, etc.
   - `rotten_tomatoes_movie_reviews.csv`: Dataset containing critic reviews for movies, including review scores, publication names, etc.
2. **Documentation/**: This directory contains the documents and reports about this project.
3. **notebooks/**: This directory contains Jupyter notebooks used for data preprocessing, exploratory data analysis (EDA), model development, and evaluation.
   - `01_data_preprocessing.ipynb`: Notebook for data cleaning and preprocessing tasks.
   - `02_eda.ipynb`: Notebook for exploratory data analysis to gain insights into the dataset.
   - `03_model_building`: Notebook for model building trial.
   - `04_Final_eda.ipynb`:  Notebook for finalised codes of preprocessing.
   - `05_Final_model.ipynb`: Notebook for finalised model
4. **static/**: This repository contains images, style files
5. **templates/**: This repository contain html file for web app
6. **README.md**: Markdown file providing an overview of the project, setup instructions, and usage guidelines.
7. **app.py**: This file contains the code for python flask web app.

## About the Project
The dataset was from rotten tomatoes website which is an american movie rating website. I have done this project as part of my Masters in Artificial inetlligence. The major challenge with this dataset is its size, so a powerful RAM is required to explore the maximum possibilities of this dataset. At the same time its wide range of possibilities (because of the large varieties of features available) any kind of recommendation system can be generated out of it. Another challenge was the data cleaning process. There were quite some challenge to clean the dataset as per the requirement. The content based model recommendtion system is build using TF-IDF cosine similarity. I have created a flask web app to demonstrate my work, but its not deployed in cloud yet. The app will recommend 10 similar movies for every input movie along with their corresponding posters for better user experience. Rotten tomatoes api was not available so I have used tmdb api for the poster retrievals. Since this project is under evaluation, the complete notebook files will be available after the evaluataion.


## Web app Demo
![web app 1.png](https://github.com/Arshapjoy/Movie_Recommendation_System_Project/blob/1ac9f4bb91da0b6f5470abcd39c40dede4fd09ff/static/web%20app%201.png)
![web app 2.png](https://github.com/Arshapjoy/Movie_Recommendation_System_Project/blob/b4ea8bd466095ab281d852eda5f6642db0c1a703/static/web%20app%202.png)
![web app 3.png](https://github.com/Arshapjoy/Movie_Recommendation_System_Project/blob/8870172970b4abcee53fea139e35705116f0f351/static/web%20app%203.png)
![web app 4.png](https://github.com/Arshapjoy/Movie_Recommendation_System_Project/blob/8870172970b4abcee53fea139e35705116f0f351/static/web%20app%204.png)

## How to run the project?

1. Clone or download this repository to your local machine.
2. Get your API key from [https://www.themoviedb.org/](https://developer.themoviedb.org/).
3. Replace YOUR_API_KEY in  `app.py` file and hit save.
4. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `python app.py`.
5. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
6. That's it! Now explore the recommendations.

## Contributing

Contributions to the project are welcome! If you encounter any issues, have suggestions for improvements, or want to add new features, feel free to submit a pull request or open an issue.

Thank you for your interest in the Movie Recommendation System project! Happy movie watching! 🍿🎬


