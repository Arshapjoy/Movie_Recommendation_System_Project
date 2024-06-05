## Datasets

[Gdrive](https://drive.google.com/drive/folders/1cFFnOok6n-Fu6N3otubXEud0w9jH7-9S?usp=drive_link) or [kaggle](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-rev)



### Rotten Tomatoes Movies Dataset: rotten_tomatoes_movies.csv

id: Unique identifier for each movie

title: The title of the movie

audienceScore: The average score given by regular viewers

tomatoMeter: The percentage of positive reviews from professional critics

rating: The movie's age-based classification (e.g., G, PG, PG-13, R)

ratingContents: Content leading to the rating classification

releaseDateTheatres: The date the movie was released in theaters

releaseDateStreaming: The date the movie became available for streaming

runtimeMinutes: The duration of the movie in minutes

genre: The movie's genre(s)

originalLanguage: The original language of the movie

director: The movie's director

writer: The writer(s) responsible for the movie's screenplay

boxOffice: The movie's total box office revenue

distributor: The company responsible for distributing the movie

soundMix: The audio format(s) used in the movie



### Rotten Tomatoes Movie Reviews Dataset: rotten_tomatoes_movie_reviews.csv

id: Unique identifier for each movie (matches the id in rotten_tomatoes_movies.csv)

reviewId: Unique identifier for each critic review

creationDate: The date the review was published

criticName: The name of the critic who wrote the review

isTopCritic: A boolean value indicating if the critic is considered a top critic

originalScore: The score provided by the critic

reviewState: The status of the review (e.g., fresh, rotten)

publicatioName: The name of the publication where the review was published

reviewText: The full text of the critic review

scoreSentiment: The sentiment of the critic's score (e.g., positive, negative, neutral)

reviewUrl: The URL of the original review on Rotten Tomatoes
