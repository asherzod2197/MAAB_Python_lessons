# ==============================
# LOOPS THEORY QUESTIONS
# ==============================

# 2. Difference between continue and break
# continue -> skips current iteration and moves to next loop cycle
# break -> stops the loop completely

# Example:
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print("continue/break example:", i)


# 3. Difference between for loop and while loop
# for -> used when number of iterations is known
# while -> used when condition-based looping is needed

# for example
for i in range(3):
    print("for loop:", i)

j = 0
while j < 3:
    print("while loop:", j)
    j += 1


# 4. Nested for loop example
# printing multiplication table 1–3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()


# ==============================
# HOMEWORK 1: Uncommon elements of lists
# ==============================

def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for x in list2:
        if x not in list1:
            result.append(x)
    return result

print(uncommon_elements([1,1,2], [2,3,4]))
print(uncommon_elements([1,2,3], [4,5,6]))
print(uncommon_elements([1,1,2,3,4,2], [1,3,4,5]))


# ==============================
# HOMEWORK 2: Squares less than n
# ==============================

n = 5
for i in range(1, n):
    print(i*i)


# ==============================
# HOMEWORK 3: Insert underscore rule
# ==============================

def insert_underscore(txt):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0

    for i in range(len(txt)):
        result += txt[i]
        count += 1

        if i == len(txt) - 1:
            break

        if count == 3:
            if txt[i] in vowels or result.endswith("_"):
                continue
            result += "_"
            count = 0

    return result

print(insert_underscore("hello"))
print(insert_underscore("assalom"))
print(insert_underscore("abcabcdabcdeabcdefabcdefg"))


# ==============================
# HOMEWORK 4: Number Guessing Game
# ==============================

import random

def number_guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10

        while attempts > 0:
            guess = int(input("Guess a number (1-100): "))

            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                return

            attempts -= 1
            print("Attempts left:", attempts)

        choice = input("You lost. Want to play again? ")
        if choice.lower() not in ['y','yes','ok']:
            break


# ==============================
# HOMEWORK 5: Password Checker
# ==============================

def password_checker():
    password = input("Enter password: ")

    if len(password) < 8:
        print("Password is too short.")
    elif not any(c.isupper() for c in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")


# ==============================
# HOMEWORK 6: Prime numbers 1-100
# ==============================

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# ==============================
# BONUS: Rock Paper Scissors Game
# ==============================

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        computer = random.choice(choices)
        player = input("Choose rock, paper, or scissors: ").lower()

        if player not in choices:
            print("Invalid choice")
            continue

        print("Computer:", computer)

        if player == computer:
            print("Draw")
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            print("Player wins round")
            player_score += 1
        else:
            print("Computer wins round")
            computer_score += 1

        print("Score -> Player:", player_score, "Computer:", computer_score)

    if player_score == 5:
        print("Player wins the match!")
    else:
        print("Computer wins the match!")


# To run games manually uncomment:
# number_guessing_game()
# password_checker()
# rock_paper_scissors()
