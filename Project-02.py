  # Greeting message generator 
  
# step1 : ask for user details
name=input("what is your name? ")
color=input("what's your favourite color? ")
age=int(input("What is your age? "))

# step2: generalized a personalized greeting message
print("\n  WELCOME MESSAGE  \n")
print(f"Hello, {name}.")
print(f"You are {age} years old and {color} is a beatiful color.")
print(f"You are now ready to start your python adventure.")
