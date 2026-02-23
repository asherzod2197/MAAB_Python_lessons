# ============================
# TASK 1: Weather API
# ============================

import requests
import random

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    print("\n=== Weather Information ===")
    print("City:", city)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])


# Example
get_weather("Tashkent")



# ============================
# TASK 2: Movie Recommendation
# ============================

TMDB_API_KEY = "YOUR_TMDB_API_KEY"


def get_genre_id(genre_name):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    
    response = requests.get(url)
    genres = response.json()["genres"]

    for g in genres:
        if g["name"].lower() == genre_name.lower():
            return g["id"]
    
    return None


def recommend_movie(genre_name):

    genre_id = get_genre_id(genre_name)

    if genre_id is None:
        print("Genre not found!")
        return

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre_id}"

    response = requests.get(url)
    movies = response.json()["results"]

    movie = random.choice(movies)

    print("\n=== Movie Recommendation ===")
    print("Title:", movie["title"])
    print("Release Date:", movie["release_date"])
    print("Rating:", movie["vote_average"])
    print("Overview:", movie["overview"])


genre = input("\nEnter movie genre: ")
recommend_movie(genre)