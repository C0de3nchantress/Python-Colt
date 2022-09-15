print("...rock...")
print("...paper...")
print("...scissors...")
p1_choice = input("enter Player1's choice: ")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
print("** NO CHEATING **")
p2_choice = input("enter Player2's choice: ")
print("SHOOT!")
if p1_choice and p2_choice:
    if p1_choice == p2_choice:
        print("it's a tie!")
    elif p1_choice == "rock":
        if p2_choice == "scissors":
            print("Player1 Wins!")
        elif p2_choice == "paper":
            print("Player2 Wins!")
    elif p1_choice == "paper":
        if p2_choice == "rock":
            print("Player1 Wins!")
        elif p2_choice == "scissors":
            print("Player2 Wins!")
    elif p1_choice == "scissors":
        if p2_choice == "rock":
            print("Player1 Wins!")
        elif p2_choice == "paper":
            print("Player2 Wins!")
    else:
        print("Something went wrong")
else:
    print("You need to choose first!")