# user 
#computet 
#logic 
# main
import random 
def get_user_choice():
    user_choice = input("enter your choice (rock, paper or scissors):").capitalize() #rock=> Rock
    while user_choice not in ["Rock","Paper", "Scissors"]:
        print("invalid choice. choose rock, paper or scissors ")
        user_choice = input("enter your choice:").capitalize()

    return user_choice
    
def get_computer_choice():
    return random.choice(["Rock","Paper", "Scissors"])
    
def determine_winners(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "it's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice =="Scissors") or 
            (user_choice == "Paper" and computer_choice =="Rock") or 
            (user_choice == "Scissors" and computer_choice =="Paper") 
            
    ):
        return "you win!" 
    else:
        return "computer wins!"
        
        
def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winners(user_choice, computer_choice)
    print(result)

while True:
    play_game()
    exit_conditon  = input("want to continue or exit!").lower()
    if exit_conditon == 'exit':
        break
    
    
             
        
        