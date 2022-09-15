import random

print("...rock...")
print("...paper...")
print("...scissors...")
p1_choice = input("enter Player1's choice: ").lower()
comp = ["rock", "paper", "scissors"]
comp_choice = random.choice(comp)
comp_input = print(f"The computer chose: {comp_choice}")
print("SHOOT!")
if p1_choice and comp_choice:
    if p1_choice == comp_choice:
        print("it's a tie!")
    elif p1_choice == "rock":
        if comp_choice == "scissors":
            print("Player1 Wins!")
        elif comp_choice == "paper":
            print("Player2 Wins!")
    elif p1_choice == "paper":
        if comp_choice == "rock":
            print("Player1 Wins!")
        elif comp_choice == "scissors":
            print("Player2 Wins!")
    elif p1_choice == "scissors":
        if comp_choice == "rock":
            print("Player1 Wins!")
        elif comp_choice == "paper":
            print("Player2 Wins!")
    else:
        print("Something went wrong")
else:
    print("You need to choose first!")