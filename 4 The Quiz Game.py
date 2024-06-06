import random

# Task 1
q1 = "What is the first letter of the English alphabet?"
q2 = "What does CPU stand for?"
q3 = "What color is the sky?"
q4 = "What year is it?"

a1 = "a"
a2 = "central processing unit"
a3 = "blue"
a4 = "2024"


questions = [q1, q2, q3, q4]
answers = [a1, a2, a3, a4]

# Task 2
def quiz_game():

    correct_answers = 0

    while True:
        
        answer = input(random.choice(questions))
        if answer.lower() in answers:
            correct_answers += 1
            
            # Task 3
            print(f"That is correct.  You have answered {correct_answers} questions correctly!")
        else:
            print(f"Incorrect.  You have answered {correct_answers} questions correctly.")
        
        keep_going = input("Would you like to keep playing?")
        if keep_going.lower() == "yes":
            continue
        else:
            break
            

intro = input("Are you ready to play the quiz game?")

if intro.lower() == "yes":
    quiz_game()
else:
    print("Why not??")