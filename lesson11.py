import sqlite3

# =========================
# TASK 1 — ROSTER DATABASE
# =========================

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 1. Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster(
Name TEXT,
Species TEXT,
Age INTEGER
)
""")

# 2. Insert Data
cursor.execute("DELETE FROM Roster")

cursor.execute("INSERT INTO Roster VALUES('Benjamin Sisko','Human',40)")
cursor.execute("INSERT INTO Roster VALUES('Jadzia Dax','Trill',300)")
cursor.execute("INSERT INTO Roster VALUES('Kira Nerys','Bajoran',29)")

# 3. Update Data
cursor.execute("""
UPDATE Roster
SET Name='Ezri Dax'
WHERE Name='Jadzia Dax'
""")

# 4. Query Bajoran
print("Bajoran Characters:")
cursor.execute("""
SELECT Name,Age FROM Roster
WHERE Species='Bajoran'
""")

for row in cursor.fetchall():
    print(row)

# 5. Delete Age > 100
cursor.execute("""
DELETE FROM Roster
WHERE Age>100
""")

# 6. Bonus Column Rank
cursor.execute("""
ALTER TABLE Roster
ADD COLUMN Rank TEXT
""")

cursor.execute("""
UPDATE Roster
SET Rank='Captain'
WHERE Name='Benjamin Sisko'
""")

cursor.execute("""
UPDATE Roster
SET Rank='Lieutenant'
WHERE Name='Ezri Dax'
""")

cursor.execute("""
UPDATE Roster
SET Rank='Major'
WHERE Name='Kira Nerys'
""")

# 7. Advanced Query
print("\nSorted by Age DESC:")
cursor.execute("""
SELECT * FROM Roster
ORDER BY Age DESC
""")

for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()



# =========================
# TASK 2 — LIBRARY DATABASE
# =========================

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# 1. Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
Title TEXT,
Author TEXT,
Year_Published INTEGER,
Genre TEXT
)
""")

# 2. Insert Data
cursor.execute("DELETE FROM Books")

cursor.execute("""
INSERT INTO Books VALUES
('To Kill a Mockingbird','Harper Lee',1960,'Fiction')
""")

cursor.execute("""
INSERT INTO Books VALUES
('1984','George Orwell',1949,'Dystopian')
""")

cursor.execute("""
INSERT INTO Books VALUES
('The Great Gatsby','F. Scott Fitzgerald',1925,'Classic')
""")

# 3. Update Year
cursor.execute("""
UPDATE Books
SET Year_Published=1950
WHERE Title='1984'
""")

# 4. Query Dystopian
print("\nDystopian Books:")
cursor.execute("""
SELECT Title,Author FROM Books
WHERE Genre='Dystopian'
""")

for row in cursor.fetchall():
    print(row)

# 5. Delete before 1950
cursor.execute("""
DELETE FROM Books
WHERE Year_Published<1950
""")

# 6. Bonus Rating Column
cursor.execute("""
ALTER TABLE Books
ADD COLUMN Rating REAL
""")

cursor.execute("""
UPDATE Books
SET Rating=4.8
WHERE Title='To Kill a Mockingbird'
""")

cursor.execute("""
UPDATE Books
SET Rating=4.7
WHERE Title='1984'
""")

cursor.execute("""
UPDATE Books
SET Rating=4.5
WHERE Title='The Great Gatsby'
""")

# 7. Advanced Query
print("\nBooks sorted by Year ASC:")
cursor.execute("""
SELECT * FROM Books
ORDER BY Year_Published ASC
""")

for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()