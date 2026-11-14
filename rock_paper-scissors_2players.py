import random

user1=input("Enter your move Sir:")
comp=random.choice(["rock", "paper", "scissors"])

if user1==comp:
    print("computer move:",comp)
    print("Draw")
else:
    if user1=="rock":
        if comp=="paper":
            print("computer move:",comp)
            print("Computer wins")
        elif comp=="scissors":
            print("computer move:",comp)
            print("Sir wins")
    elif user1=="paper":
        if comp=="rock":
            print("computer move:",comp)
            print("Sir wins")
        elif comp=="scissors":
            print("computer move:",comp)
            print("Computer wins")
    elif user1=="scissors":
        if comp=="rock":
            print("computer move:",comp)
            print("Computer wins")
        elif comp=="paper":
            print("computer move:",comp)
            print("Sir wins")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
