import pandas as pd
import sqlite3

# ---------------- MERGING AND JOINING ----------------

# 1 Inner Join on Chinook Database
conn = sqlite3.connect("chinook.db")

customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)

inner_join = pd.merge(customers, invoices, on="CustomerId", how="inner")

invoice_count = inner_join.groupby("CustomerId")["InvoiceId"].count()

print("Invoices per customer:")
print(invoice_count)


# 2 Outer Join on Movie Data

movies = pd.read_csv("movie.csv")

df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]

left_join = pd.merge(df1, df2, on="director_name", how="left")
outer_join = pd.merge(df1, df2, on="director_name", how="outer")

print("\nLeft Join rows:", len(left_join))
print("Outer Join rows:", len(outer_join))


# ---------------- GROUPING AND AGGREGATING ----------------

# 1 Titanic Grouping

titanic = pd.read_excel("titanic.xlsx")

titanic_grouped = titanic.groupby("Pclass").agg(
    Average_Age=("Age", "mean"),
    Total_Fare=("Fare", "sum"),
    Passenger_Count=("PassengerId", "count")
)

print("\nTitanic grouped data:")
print(titanic_grouped)


# 2 Movie Multi-level Grouping

movie_group = movies.groupby(["color", "director_name"]).agg(
    Total_Critic_Reviews=("num_critic_for_reviews", "sum"),
    Avg_Duration=("duration", "mean")
)

print("\nMovie grouped data:")
print(movie_group.head())


# 3 Flights Nested Grouping

flights = pd.read_parquet("flights.parquet")

flights_group = flights.groupby(["Year", "Month"]).agg(
    Total_Flights=("Year", "count"),
    Avg_ArrDelay=("ArrDelay", "mean"),
    Max_DepDelay=("DepDelay", "max")
)

print("\nFlights grouped data:")
print(flights_group.head())


# ---------------- APPLYING FUNCTIONS ----------------

# 1 Titanic Age Group

def age_group(age):
    if age < 18:
        return "Child"
    else:
        return "Adult"

titanic["Age_Group"] = titanic["Age"].apply(age_group)

print("\nTitanic Age Group:")
print(titanic[["Age", "Age_Group"]].head())


# 2 Normalize Employee Salaries

employees = pd.read_csv("employee.csv")

employees["Normalized_Salary"] = employees.groupby("department")["salary"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print("\nNormalized salaries:")
print(employees.head())


# 3 Movie Duration Classification

def movie_length(duration):

    if duration < 60:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"

movies["Length_Category"] = movies["duration"].apply(movie_length)

print("\nMovie length categories:")
print(movies[["movie_title", "duration", "Length_Category"]].head())


# ---------------- USING PIPE ----------------

# 1 Titanic Pipeline

titanic_pipe = (
    titanic
    .pipe(lambda df: df[df["Survived"] == 1])
    .pipe(lambda df: df.assign(Age=df["Age"].fillna(df["Age"].mean())))
    .pipe(lambda df: df.assign(Fare_Per_Age=df["Fare"] / df["Age"]))
)

print("\nTitanic pipeline result:")
print(titanic_pipe.head())


# 2 Flights Pipeline

flights_pipe = (
    flights
    .pipe(lambda df: df[df["DepDelay"] > 30])
    .pipe(lambda df: df.assign(
        Delay_Per_Hour=df["DepDelay"] / df["AirTime"]
    ))
)

print("\nFlights pipeline result:")
print(flights_pipe.head())