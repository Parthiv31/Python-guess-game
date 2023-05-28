import random
print("Welcome to guess game")
while(True):
    print("Guess a number between 1 to 100")
    r=random.randint(1,101)
    i=int(input())
    if i==r:
        print("You guessed right")
    else:
        print(f"No, the correct number is {r}")
    print("Do you want to continue (yes/no)")
    s=input().lower()
    if s=="no":
        print("Exiting...\n")
        break
