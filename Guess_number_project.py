import random

n = random.randint(1, 100)

a = -1

count = 1

while(a != n ):
    
    a = int(input("Guess your number: "))
    if(a > 0 and a > n and a < 100):
        print("Lower Number:")
        count += 1
            
    elif(a > 0 and a < n and a < 100):
        print("Higher Number:") 
        count += 1  
        
    else:
        print("Please enter the number between 1 to 100. ") 
        
print(f"You guessed the correct number {n} in {count} guesses.")
        
