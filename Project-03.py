 # simple calculator
 
# step1 :- Get user input for two numbers
n1=int(input("Enter the first number:- "))
n2=int(input("Enter the second number:- "))

# step2:- perform arithematic operation 

addition=n1+n2
substraction=n1-n2
multiply=n1*n2
divide=n1/n2
remainder=n1%n2

# step3:- Display the results

print(f"Addition:{n1}+{n2} = {addition}")
print(f"Substraction:{n1}-{n2} = {substraction}")
print(f"multiplication: {n1}*{n2} = {multiply}")
print(f"divide: {n1}/{n2} = {divide}")
print(f"Remainder: {n1}%{n2} = {remainder}")
