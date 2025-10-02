import math
import random
from itertools import permutations

# 1. Class to get and print string
class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())


# 2. Shape and Square
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# 3. Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# 4. Point class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# 5. Bank Account
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")


# 6. Filter primes using filter + lambda
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(lst):
    return list(filter(lambda x: is_prime(x), lst))


# 7. Grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams


# 8. Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)


# 9. Chickens and Rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None


# 10. Permutations of string
def print_permutations(s):
    for p in permutations(s):
        print("".join(p))


# 11. Reverse words in sentence
def reverse_sentence(s):
    return " ".join(s.split()[::-1])


# 12. has_33
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False


# 13. spy_game
def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == 3:
                return True
    return False


# 14. Volume of sphere
def sphere_volume(r):
    return (4/3) * math.pi * (r**3)


# 15. Unique elements
def unique_list(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res


# 16. Palindrome check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 17. Histogram
def histogram(lst):
    for n in lst:
        print("*" * n)


# 18. Guess the number game
def guess_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


# 19. Movies tasks
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_movie_good(movie):
    return movie["imdb"] > 5.5

def good_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

def average_imdb(movies):
    return sum(m["imdb"] for m in movies) / len(movies)

def average_imdb_by_category(movies, category):
    cat_movies = [m for m in movies if m["category"] == category]
    return sum(m["imdb"] for m in cat_movies) / len(cat_movies)
