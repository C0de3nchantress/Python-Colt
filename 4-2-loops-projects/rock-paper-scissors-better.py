import random
print("...rock...")
print("...paper...")
print("...scissors...")
computer_count = 0
player_count = 0
while computer_count<=3 or player_count<=3:
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
                print("Player1 wins this round")
                player_count+=1
                if player_count ==3:
                    print("Player1 Wins it all!")
                    break
            elif comp_choice == "paper":
                print("Computer wins this round")
                computer_count +=1
                if computer_count == 3:
                    print("Computer Wins it all!")
                    break
        elif p1_choice == "paper":
            if comp_choice == "rock":
                print("Player1 wins this round")
                player_count+=1
                if player_count ==3:
                    print("Player1 Wins it all!")
                    break
            elif comp_choice == "scissors":
                print("Computer wins this round")
                computer_count +=1
                if computer_count == 3:
                    print("Computer Wins it all!")
                    break
        elif p1_choice == "scissors":
            if comp_choice == "rock":
                print("Player1 wins this round")
                player_count+=1
                if player_count ==3:
                    print("Player1 Wins it all!")
                    break
            elif comp_choice == "paper":
                print("Computer wins this round")
                computer_count +=1
                if computer_count == 3:
                    print("Computer Wins it all!")
                    break
        else:
            print("Something went wrong")
    else:
        print("You need to choose first!")