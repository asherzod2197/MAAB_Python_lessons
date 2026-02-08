# =============================
# NUMBER DATA TYPE QUESTIONS
# =============================

# 1. Round float to 2 decimal places
num = float(input("Enter a float number: "))
print("Rounded:", round(num, 2))

# -----------------------------
# 2. Find largest and smallest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Largest:", max(a, b, c))
print("Smallest:", min(a, b, c))

# -----------------------------
# 3. Convert kilometers to meters and centimeters

km = float(input("Enter kilometers: "))
meters = km * 1000
centimeters = km * 100000

print("Meters:", meters)
print("Centimeters:", centimeters)

# -----------------------------
# 4. Integer division and remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Integer division:", a // b)
print("Remainder:", a % b)

# -----------------------------
# 5. Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# -----------------------------
# 6. Last digit of a number

num = int(input("Enter a number: "))
print("Last digit:", num % 10)

# -----------------------------
# 7. Check if number is even

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# STRING QUESTIONS

# 1. Ask name and birth year, calculate age

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print(f"{name}, your age is {age}")

# 2. Extract car names from text

txt = 'LMaasleitbtui'
car_name = txt[1::2]
print("Car name:", car_name)

# 3. String length, upper, lower

text = input("Enter a string: ")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 4. Palindrome check

text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# 5. Count vowels and consonants

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 6. Check if one string contains another

str1 = input("Enter main string: ")
str2 = input("Enter string to search: ")

if str2 in str1:
    print("String found")
else:
    print("String not found")

# 7. Replace word in sentence

sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("Replace with: ")

print("Result:", sentence.replace(old_word, new_word))

# 8. First and last characters

text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])

# 9. Reverse string

text = input("Enter a string: ")
print("Reversed:", text[::-1])

# 10. Count words in sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))

# 11. Check if string contains digits

text = input("Enter a string: ")
if any(char.isdigit() for char in text):
    print("Contains digits")
else:
    print("No digits")

# 12. Join list of words

words = ["Python", "is", "fun"]
joined = "-".join(words)
print("Joined string:", joined)

# 13. Remove all spaces

text = input("Enter a string: ")
print("Without spaces:", text.replace(" ", ""))

# 14. Compare two strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# 15. Create acronym

sentence = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)

# 16. Remove all occurrences of a character

text = input("Enter a string: ")
char = input("Enter character to remove: ")
print("Result:", text.replace(char, ""))

# 17. Replace vowels with '*'

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

result = ""
for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char

print("Result:", result)

# 18. Check start and end words

sentence = input("Enter a sentence: ")
start_word = input("Starts with: ")
end_word = input("Ends with: ")

if sentence.startswith(start_word) and sentence.endswith(end_word):
    print("Sentence matches")
else:
    print("Sentence does not match")


# BOOLEAN DATA TYPE QUESTIONS

# 1. Username and password not empty

username = input("Enter username: ")
password = input("Enter password: ")

if username and password:
    print("Both provided")
else:
    print("Username or password is empty")

# 2. Check if two numbers are equal

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

# 3. Check if number is positive and even

num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Positive and even")
else:
    print("Condition not met")

# 4. Check if three numbers are different

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    print("All numbers are different")
else:
    print("Some numbers are the same")

# 5. Check if two strings have same length

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2):
    print("Same length")
else:
    print("Different length")

# 6. Check if number divisible by 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

# 7. Check if sum > 50

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a + b > 50:
    print("Sum is greater than 50")
else:
    print("Sum is not greater than 50")

# 8. Check if number between 10 and 20 inclusive

num = int(input("Enter a number: "))
if 10 <= num <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is outside the range")
