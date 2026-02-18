
#  Student Grade Manager

# Step1:- Get Student scores 
student_scores=input("Enter student scores separated by commas: ")
scores=[int(score) for score in student_scores.split(",")] 

# step2:- Assign grade using list comprehension

grades=[
    "A" if score >=90 else
    "B" if score >=80 else
    "C" if score >=70 else
    "D" if score >=60 else
    "F"
    for score in scores
]

# step3:- Filter passing and failing students

passing_students = [ score for score in scores if score>=60]
failing_students = [score for score in scores if score < 60]

# step4:- print Result
print("\n-- Studets Grades --- ")
for i,(score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Students {i}: score = {score}, Grade={grade}")
    
print("\n--- Passing and Falling Students ----")
print("Passing Students:",passing_students)
print("Failing Students:", failing_students)
