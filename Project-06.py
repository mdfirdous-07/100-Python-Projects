# Basic math Quiz Game

import random

# step1: define the math question function
def generate_question():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operator=random.choice(["+","-","*"])
    
    if operator == "+":
        answer =num1 + num2
    elif operator=="-":
        answer =num1 - num2
    else:
        answer = num1*num2
        
    question= f"{num1} {operator} {num2}"
    return question, answer

# step2: Main Quizz game function


def math_quiz():
    print("\n---- Welcome to the math quiz game ----\n" )
    score=0
    round=5
    for i in range(round):
        question, correct_answer = generate_question()
        print(f"\n Question{i+1}:{question}")
        user_answer=int(input("your answer: "))
        
        if user_answer==correct_answer:
            print("correct!")
            score=score + 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            
    print("\n --- game over! ---\n")
    print(f"Your final score is: {score}/{round}")
    
    if score==round:
        print("Congratulations! you got all the questions correct")
    elif score>=round//2:
        print("good job ! you did well.")
    else:
        print("Keep practicing! you can do better next time")
    
#  step3 : run the game

math_quiz()
        
