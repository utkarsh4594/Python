import random

user=input("Enter your move Sir:")
comp=random.choice(["rock", "paper", "scissors"])

if user==comp:
    print("computer move:",comp)
    print("Draw")
else:
    if user=="rock":
        if comp=="paper":
            print("computer move:",comp)
            print("Computer wins")
        elif comp=="scissors":
            print("computer move:",comp)
            print("Sir wins")
    elif user=="paper":
        if comp=="rock":
            print("computer move:",comp)
            print("Sir wins")
        elif comp=="scissors":
            print("computer move:",comp)
            print("Computer wins")
    elif user=="scissors":
        if comp=="rock":
            print("computer move:",comp)
            print("Computer wins")
        elif comp=="paper":
            print("computer move:",comp)
            print("Sir wins")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
