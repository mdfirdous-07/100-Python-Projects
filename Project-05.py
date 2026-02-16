# Countdown Timer

import time
#  step1: get user input for countdown start
start=int(input("Enter the number to start the countdown from: "))

# step2 : Countdown using a while loop
print("\n--  Countdown Begins -- \n")
while start>0:
    print(start)
    time.sleep(1)
    start-=1
    
# step3: 
print("\n--- Happy New Year! ---")
print("\n--- Happy birthday! ---")
