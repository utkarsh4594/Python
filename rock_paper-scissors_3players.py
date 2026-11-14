import random

user1=input("Enter your move Sir:")
comp1=random.choice(["rock", "paper", "scissors"])
comp2=random.choice(["rock", "paper", "scissors"])
if user1==comp1 and comp1==comp2 and user1==comp2:
    print("computer1 move:",comp1)
    print("computer2 move:",comp2)
    print("Draw")
else:
    if user1=="rock":
        if comp1=="paper" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Computer wins")
        elif comp1=="scissors" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Sir wins")
        elif comp1=="paper" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Draw")
        elif comp1=="scissors" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Draw")
    elif user1=="paper":
        if comp1=="rock" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Sir wins")
        elif comp1=="scissors" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Computer wins")
        elif comp1=="rock" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Draw")
        elif comp1=="scissors" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Draw")
    elif user1=="scissors":
        if comp1=="rock" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Computer wins")
        elif comp1=="paper" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Sir wins")
        elif comp1=="rock" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Draw")
        elif comp1=="paper" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("Draw")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")


            


           
       
            

    
    
    





