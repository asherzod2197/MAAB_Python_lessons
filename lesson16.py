import pandas as pd
import sqlite3


# ---------------- PART 1 : READING FILES ----------------

# 1 chinook.db
conn = sqlite3.connect("chinook.db")
customers = pd.read_sql_query("SELECT * FROM customers", conn)
print("First 10 rows of customers:")
print(customers.head(10))


# 2 iris.json
iris = pd.read_json("iris.json")
print("\nIris dataset shape:")
print(iris.shape)

print("\nIris columns:")
print(iris.columns)


# 3 titanic.xlsx
titanic = pd.read_excel("titanic.xlsx")
print("\nTitanic first 5 rows:")
print(titanic.head())


# 4 flights parquet
flights = pd.read_parquet("flights.parquet")
print("\nFlights info:")
print(flights.info())


# 5 movie.csv
movies = pd.read_csv("movie.csv")
print("\nRandom 10 movies:")
print(movies.sample(10))


# ---------------- PART 2 : EXPLORING DATAFRAMES ----------------

# iris.json
iris.columns = iris.columns.str.lower()

iris_selected = iris[["sepal_length", "sepal_width"]]
print("\nSelected columns from iris:")
print(iris_selected.head())


# titanic.xlsx
age_above_30 = titanic[titanic["age"] > 30]
print("\nPassengers age > 30:")
print(age_above_30.head())

print("\nGender counts:")
print(titanic["sex"].value_counts())


# flights parquet
selected_flights = flights[["origin", "dest", "carrier"]]
print("\nSelected flight columns:")
print(selected_flights.head())

print("\nUnique destinations:")
print(flights["dest"].nunique())


# movie.csv
long_movies = movies[movies["duration"] > 120]

sorted_movies = long_movies.sort_values(
    by="director_facebook_likes",
    ascending=False
)

print("\nLong movies sorted by director facebook likes:")
print(sorted_movies.head())


# ---------------- PART 3 : CHALLENGES ----------------

# iris statistics
print("\nIris statistics:")
print("Mean:\n", iris.mean(numeric_only=True))
print("Median:\n", iris.median(numeric_only=True))
print("Std:\n", iris.std(numeric_only=True))


# titanic age stats
print("\nTitanic age statistics:")
print("Min:", titanic["age"].min())
print("Max:", titanic["age"].max())
print("Sum:", titanic["age"].sum())


# movie.csv analysis

# director with highest total facebook likes
director_likes = movies.groupby("director_name")["director_facebook_likes"].sum()
top_director = director_likes.idxmax()

print("\nDirector with highest total facebook likes:")
print(top_director)


# 5 longest movies
longest_movies = movies.sort_values(by="duration", ascending=False)

print("\nTop 5 longest movies:")
print(longest_movies[["movie_title", "director_name", "duration"]].head(5))


# flights missing values
print("\nMissing values in flights dataset:")
print(flights.isnull().sum())


# fill missing numeric column with mean
flights_filled = flights.fillna(flights.mean(numeric_only=True))

print("\nMissing values after filling:")
print(flights_filled.isnull().sum())