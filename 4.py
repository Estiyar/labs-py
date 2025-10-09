Q1
def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

for square in generate_squares(5):
    print(square)

Q2
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:       
            yield i         

n = int(input("Введите n: "))

for number in even_numbers(n):   
    print(number, end=" ")
Q3
def divisible(n):
    for i in range(n,n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for num in divisible(n):
    print(num)

Q4
def square_num (a,b):
    for i in range(a,b+1):
        yield i ** 2 
a = int(input("напиши начало"))
b = int(input("напиши конец"))
for number in square_num (a,b):
    print (number,end=" " )



Q5
def dawn(n):
    for i in range (n, -1,-1):
        yield i 
n = int(input("пиши сюда"))
for numb in dawn(n):
   print(numb,end=" ")



Q6
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Date after 5 days:", new_date)


Q7
from datetime import date, timedelta

today = date.today()
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))


Q8
from datetime import datetime

now = datetime.now().replace(microsecond=0)
print(now)


Q9
from datetime import datetime

date1 = datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime(2025, 10, 9, 14, 30, 0)
difference = (date2 - date1).total_seconds()
print("Difference ", difference)


Q10
import math

degree = 15
radian = math.radians(degree)
print("Radian:", radian)



Q11
height = 5
base1 = 5
base2 = 6
area = ((base1 + base2) / 2) * height
print("Area:", area)


Q12
import math

n = 4  
s = 25  
area = (n * s**2) / (4 * math.tan(math.pi / n))
print("Area:", area)



Q13
base = 5
height = 6
area = base * height
print("Area of parallelogram:", area)



Q14
import json

with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN".ljust(50), "Description".ljust(20), "Speed".ljust(8), "MTU")
print("-" * 80)

for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    desc = item["l1PhysIf"]["attributes"]["descr"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:<50} {desc:<20} {speed:<8} {mtu}")

