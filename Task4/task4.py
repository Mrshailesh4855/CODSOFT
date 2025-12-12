import random
print("Rock Paper Scissors Game")
print("Type rock, paper, or scissors")
user_score=0
computer_score=0
while True:
    user=input("Your choice: ").lower()
    if user not in ["rock","paper","scissors"]:
        print("Invalid choice! Try again.\n")
        continue
    computer=random.choice(["rock","paper","scissors"])
    print("You chose:",user)
    print("Computer chose:",computer)
    if user==computer:
        print("Result: It's a Tie!\n")
    elif user=="rock" and computer=="scissors":
        print("You Win!\n")
        user_score+=1
    elif user=="paper" and computer=="rock":
        print("You Win!\n")
        user_score+=1
    elif user=="scissors" and computer=="paper":
        print("You Win!\n")
        user_score+=1
    else:
        print("You Lose!\n")
        computer_score+=1
    print("Score -> You:",user_score,"| Computer:",computer_score)
    again=input("\nPlay again? (y/n): ").lower()
    if again!="y":
        print("Final Score -> You:",user_score,"| Computer:",computer_score)
        break
