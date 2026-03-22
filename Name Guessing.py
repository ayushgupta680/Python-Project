import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Enter the numbers:"))
    
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too Hight")
    else:
        print("Correct")
        
1
        


