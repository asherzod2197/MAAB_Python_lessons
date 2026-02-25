# =========================
# TASK 1 — WEATHER SCRAPING
# =========================

from bs4 import BeautifulSoup

# Load HTML file
with open("weather.html","r",encoding="utf-8") as file:
    soup = BeautifulSoup(file,"html.parser")

rows = soup.find_all("tr")[1:]

temperatures = []
sunny_days = []

print("Weather Forecast:\n")

for row in rows:
    cols = row.find_all("td")

    day = cols[0].text
    temp = cols[1].text
    condition = cols[2].text

    print(day,temp,condition)

    t = int(temp.replace("°C",""))
    temperatures.append((day,t))

    if condition=="Sunny":
        sunny_days.append(day)


# Highest temperature
highest = max(temperatures,key=lambda x:x[1])

print("\nHighest Temperature:")
print(highest[0],highest[1],"°C")


# Sunny days
print("\nSunny Days:")
for d in sunny_days:
    print(d)


# Average temperature
avg = sum(t[1] for t in temperatures)/len(temperatures)

print("\nAverage Temperature:",avg,"°C")



# =========================
# TASK 2 — JOB SCRAPER
# =========================

import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs"

r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

jobs=soup.find_all("div",class_="card-content")


conn=sqlite3.connect("jobs.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs(
title TEXT,
company TEXT,
location TEXT,
description TEXT,
link TEXT,
UNIQUE(title,company,location)
)
""")


for job in jobs:

    title=job.find("h2").text.strip()
    company=job.find("h3").text.strip()
    location=job.find("p",class_="location").text.strip()
    description=job.find_all("p")[1].text.strip()

    link=job.find("a")["href"]


    cursor.execute("""
    SELECT description,link FROM jobs
    WHERE title=? AND company=? AND location=?
    """,(title,company,location))

    data=cursor.fetchone()


    if data is None:

        cursor.execute("""
        INSERT INTO jobs VALUES(?,?,?,?,?)
        """,(title,company,location,description,link))

    else:

        if data[0]!=description or data[1]!=link:

            cursor.execute("""
            UPDATE jobs
            SET description=?,link=?
            WHERE title=? AND company=? AND location=?
            """,(description,link,title,company,location))


conn.commit()


# Filter function

def filter_jobs(location=None,company=None):

    query="SELECT * FROM jobs WHERE 1=1"
    params=[]

    if location:
        query+=" AND location=?"
        params.append(location)

    if company:
        query+=" AND company=?"
        params.append(company)

    cursor.execute(query,params)

    return cursor.fetchall()



# Export CSV

def export_csv(data):

    with open("filtered_jobs.csv","w",newline="",encoding="utf-8") as f:

        writer=csv.writer(f)

        writer.writerow(["Title","Company","Location","Description","Link"])

        writer.writerows(data)


data=filter_jobs(location="Remote")

export_csv(data)


conn.close()




# =========================
# TASK 3 — LAPTOP SCRAPER
# =========================

import json
import time

laptops=[]

base="https://www.demoblaze.com"

for page in range(2):

    r=requests.get(base)
    soup=BeautifulSoup(r.text,"html.parser")

    items=soup.find_all("div",class_="card-block")

    for item in items:

        name=item.find("h4").text
        price=item.find("h5").text

        link=item.find("a")["href"]

        r2=requests.get(base+"/"+link)

        soup2=BeautifulSoup(r2.text,"html.parser")

        desc=soup2.find("p").text


        laptops.append({
            "name":name,
            "price":price,
            "description":desc
        })


    time.sleep(2)


with open("laptops.json","w",encoding="utf-8") as f:

    json.dump(laptops,f,indent=4)


print("\nSaved laptops.json")