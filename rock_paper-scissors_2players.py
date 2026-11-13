import random

user1=input("Enter your move Sir:")
user2=random.choice(["rock", "paper", "scissors"])

if user1==user2:
    print("computer move:",user2)
    print("Draw")
else:
    if user1=="rock":
        if user2=="paper":
            print("computer move:",user2)
            print("Computer wins")
        elif user2=="scissors":
            print("computer move:",user2)
            print("Sir wins")
    elif user1=="paper":
        if user2=="rock":
            print("computer move:",user2)
            print("Sir wins")
        elif user2=="scissors":
            print("computer move:",user2)
            print("Computer wins")
    elif user1=="scissors":
        if user2=="rock":
            print("computer move:",user2)
            print("Computer wins")
        elif user2=="paper":
            print("computer move:",user2)
            print("Sir wins")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
