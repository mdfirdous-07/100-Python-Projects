# Number Comparison Tool

# step1: get the user input for two numbers
n1=int(input("Enter the first number:- "))
n2=int(input("Enter the second number:- "))

# step2: compare the number
print("\n  comparision result  \n")

if n1==n2:
    print(f"print both number are equal : {n1}")
elif n1>n2:
    print(f"{n1} is greater than {n2}")
else:
    print(f"{n2} is greater than {n1}")
    
# check if any numnber is zero 
if n1==0 or n2==0:
    print("atleast one number is zero")
else:
    print("both number are non-zero")
