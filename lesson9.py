# =====================================================
# TASK 1 — LIBRARY MANAGEMENT (Custom Exceptions)
# =====================================================

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"



class Member:

    LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} | Books: {len(self.borrowed_books)}"



class Library:

    def __init__(self):
        self.books = []
        self.members = []


    def add_book(self, title, author):
        self.books.append(Book(title, author))


    def add_member(self, name):
        self.members.append(Member(name))


    def find_book(self, title):

        for b in self.books:
            if b.title == title:
                return b

        raise BookNotFoundException("Book not found")


    def borrow_book(self, member_name, title):

        book = self.find_book(title)

        member = None

        for m in self.members:
            if m.name == member_name:
                member = m

        if member is None:
            print("Member not found")
            return

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book already borrowed")

        if len(member.borrowed_books) >= Member.LIMIT:
            raise MemberLimitExceededException("Borrow limit exceeded")

        book.is_borrowed = True
        member.borrowed_books.append(book)

        print("Book borrowed successfully")


    def return_book(self, member_name, title):

        book = self.find_book(title)

        for m in self.members:

            if m.name == member_name:

                if book in m.borrowed_books:

                    book.is_borrowed = False
                    m.borrowed_books.remove(book)

                    print("Book returned")
                    return

        print("Return failed")



def library_demo():

    lib = Library()

    lib.add_book("Python", "John")
    lib.add_book("Math", "Smith")
    lib.add_book("Physics", "Brown")

    lib.add_member("Ali")


    try:
        lib.borrow_book("Ali","Python")
        lib.borrow_book("Ali","Math")
        lib.borrow_book("Ali","Physics")

        lib.borrow_book("Ali","Unknown")

    except Exception as e:
        print("Error:",e)



# =====================================================
# TASK 2 — CSV GRADES
# =====================================================

import csv


def grades_system():

    try:

        data=[]

        with open("grades.csv") as f:

            reader=csv.DictReader(f)

            for row in reader:
                data.append(row)


        subjects={}

        for r in data:

            subject=r["Subject"]
            grade=float(r["Grade"])

            if subject not in subjects:
                subjects[subject]=[]

            subjects[subject].append(grade)


        averages={}

        for s in subjects:

            avg=sum(subjects[s])/len(subjects[s])

            averages[s]=round(avg,2)


        with open("average_grades.csv","w",newline="") as f:

            writer=csv.writer(f)

            writer.writerow(["Subject","Average Grade"])

            for s,a in averages.items():
                writer.writerow([s,a])


        print("Average grades saved")

    except FileNotFoundError:
        print("grades.csv not found")



# =====================================================
# TASK 3 — JSON TASK MANAGER
# =====================================================

import json



def load_tasks():

    with open("tasks.json") as f:

        tasks=json.load(f)

    return tasks



def show_tasks(tasks):

    print("\nTASK LIST")

    for t in tasks:

        print(
            t["id"],
            t["task"],
            t["completed"],
            t["priority"]
        )



def stats(tasks):

    total=len(tasks)

    completed=sum(1 for t in tasks if t["completed"])

    pending=total-completed

    avg=sum(t["priority"] for t in tasks)/total

    print("\nStatistics")

    print("Total:",total)
    print("Completed:",completed)
    print("Pending:",pending)
    print("Average priority:",round(avg,2))



def save_tasks(tasks):

    with open("tasks.json","w") as f:

        json.dump(tasks,f,indent=4)



def json_to_csv(tasks):

    with open("tasks.csv","w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow(["ID","Task","Completed","Priority"])

        for t in tasks:

            writer.writerow([
                t["id"],
                t["task"],
                t["completed"],
                t["priority"]
            ])

    print("Converted to tasks.csv")



def json_demo():

    try:

        tasks=load_tasks()

        show_tasks(tasks)

        stats(tasks)

        json_to_csv(tasks)

        save_tasks(tasks)

    except FileNotFoundError:
        print("tasks.json not found")



# =====================================================
# MAIN MENU
# =====================================================

print("\nSelect Task")

print("1 Library System")
print("2 Grades CSV")
print("3 JSON Tasks")

choice=input("Choice: ")


if choice=="1":
    library_demo()

elif choice=="2":
    grades_system()

elif choice=="3":
    json_demo()

else:
    print("Exit")