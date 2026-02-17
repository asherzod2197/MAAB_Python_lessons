# =====================================================
# 1. Zero Check Decorator
# =====================================================

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper


@check
def div(a, b):
    return a / b


print("=== Zero Check Decorator ===")
print(div(6, 2))
print(div(6, 0))


# =====================================================
# 2. Employee Records Manager
# =====================================================

FILE_NAME = "employees.txt"

def add_employee():
    with open(FILE_NAME, "a") as file:
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added.\n")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No records found.\n")
                return
            for line in records:
                print(line.strip())
    except FileNotFoundError:
        print("No employee file found.\n")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Record found:", line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("File not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_lines = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith(emp_id + ","):
                found = True
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                updated_lines.append(f"{emp_id}, {name}, {position}, {salary}\n")
            else:
                updated_lines.append(line)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)

        if found:
            print("Employee updated.\n")
        else:
            print("Employee not found.\n")

    except FileNotFoundError:
        print("File not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_lines = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith(emp_id + ","):
                found = True
                continue
            updated_lines.append(line)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)

        if found:
            print("Employee deleted.\n")
        else:
            print("Employee not found.\n")

    except FileNotFoundError:
        print("File not found.")


def employee_menu():
    while True:
        print("\n=== Employee Records Manager ===")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search employee by ID")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")


# =====================================================
# 3. Word Frequency Counter
# =====================================================

import os
import string
from collections import Counter

def create_sample_if_missing():
    if not os.path.exists("sample.txt"):
        print("sample.txt not found. Please enter a paragraph:")
        text = input()
        with open("sample.txt", "w") as file:
            file.write(text)


def process_text():
    create_sample_if_missing()

    with open("sample.txt", "r") as file:
        text = file.read().lower()

    # remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    total_words = len(words)

    counter = Counter(words)

    top_n = input("How many top words to display? (default 5): ")
    top_n = int(top_n) if top_n.isdigit() else 5

    most_common = counter.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print("Top words:")
    for word, count in most_common:
        print(f"{word} - {count} times")

    # save report
    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top Words:\n")
        for word, count in most_common:
            report.write(f"{word} - {count}\n")

    print("\nReport saved to word_count_report.txt")


# =====================================================
# MAIN PROGRAM
# =====================================================

print("\nSelect program to run:")
print("1 - Employee Records Manager")
print("2 - Word Frequency Counter")
print("Any other key - Exit")

main_choice = input("Enter choice: ")

if main_choice == "1":
    employee_menu()
elif main_choice == "2":
    process_text()
else:
    print("Program ended.")
