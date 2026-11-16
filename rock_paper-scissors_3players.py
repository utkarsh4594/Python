import random
user=input("Enter your move Sir:")
comp1=random.choice(["rock", "paper", "scissors"])
comp2=random.choice(["rock", "paper", "scissors"])
if user==comp1 and comp1==comp2:
    print("computer1 move:",comp1)
    print("computer2 move:",comp2)
    print("Draw")
else:
    if user=="rock":
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
        elif comp1=="rock" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("computer2 wins")
        elif comp1=="rock" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("sir and computer1 win")
        elif comp1=="paper" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("computer1 wins")
        elif comp1=="scissors" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("sir and computer2 win")
    elif user=="paper":
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
        elif comp1=="paper" and comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("sir and computer1 win")
        elif comp1=="paper" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("computer2 wins")
        elif comp1=="rock" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("sir and computer2 win")
        elif comp1=="scissors" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("computer1 wins")
    elif user=="scissors":
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
        elif comp1=="scissors" and  comp2=="rock":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("computer2 wins")
        elif comp1=="scissors" and comp2=="paper":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("sir and comuter1 win")
        elif comp1=="paper" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("sir and computer2 win")
        elif comp1=="rock" and comp2=="scissors":
            print("computer1 move:",comp1)
            print("computer2 move:",comp2)
            print("computer1 wins")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")


            


           
       
            

    
    
    





