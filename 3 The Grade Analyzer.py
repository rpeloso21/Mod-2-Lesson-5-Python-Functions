
import random

grades = []

for x in range(15):
    grade = random.randint(1, 100)
    grades.append(grade)

# Task 1
def average():
    average = sum(grades)/len(grades)
    print(f"the average grade is {average}.")

# Task 2
def high_and_low():
    highest = max(grades)
    lowest = min(grades)
    print(f"The highest grade is {highest} and the lowest grade is {lowest}.")

# Task 3
def sort_grades():

    a = 0
    b = 0
    c = 0
    d = 0
    f = 0

    for grade in grades:
        if grade > 89:
            a += 1
        elif grade > 79:
            b += 1
        elif grade > 69: 
            c += 1
        elif grade > 59: 
            d += 1
        else:
            f += 1
    print(f"For this list of grades there are {a} A's, {b} B's, {c} C's, {d} D's, and {f} F's.")

        

print(f"The list of grades is: {grades}")
average()
high_and_low()
sort_grades()