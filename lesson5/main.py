# =========================
# Task 1 — temperature.py
# =========================

def convert_cel_to_far(c):
    return c * 9/5 + 32


def convert_far_to_cel(f):
    return (f - 32) * 5/9


print("=== Temperature Converter ===")

f_temp = float(input("Enter a temperature in degrees F: "))
c_result = round(convert_far_to_cel(f_temp), 2)
print(f"{f_temp} degrees F = {c_result} degrees C")

c_temp = float(input("\nEnter a temperature in degrees C: "))
f_result = round(convert_cel_to_far(c_temp), 2)
print(f"{c_temp} degrees C = {f_result} degrees F")


# =========================
# Task 2 — invest.py
# =========================

print("\n=== Investment Calculator ===")

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")


principal = float(input("Enter initial investment amount: "))
annual_rate = float(input("Enter annual rate (e.g. 0.05 for 5%): "))
years = int(input("Enter number of years: "))

invest(principal, annual_rate, years)


# =========================
# Task 3 — factors.py
# =========================

print("\n=== Factors Finder ===")

number = int(input("Enter a positive integer: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")


# =========================
# Task 4 — University stats
# =========================

print("\n=== University Statistics ===")

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(data):
    students = []
    tuition = []
    for uni in data:
        students.append(uni[1])
        tuition.append(uni[2])
    return students, tuition


def mean(values):
    return sum(values) / len(values)


def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)

    if n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        mid1 = sorted_vals[n // 2]
        mid2 = sorted_vals[n // 2 - 1]
        return (mid1 + mid2) / 2


students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)

print("\n******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")

print(f"\nStudent mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,.0f}")

print(f"\nTuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,.0f}")
print("******************************")


# =========================
# Task 5 — Prime checker
# =========================

print("\n=== Prime Number Checker ===")

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a positive number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
