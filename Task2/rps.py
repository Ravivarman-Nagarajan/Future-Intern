import random

def get_computer_choice ():
    choices = ['rock' , 'paper' , 'scissor']
    return random.choice(choices)

def get_user_choice ():
    player_choice = input("Enter your choice (rock , paper , scissor):") .lower()
    while player_choice not in ['rock' , 'paper' , 'scissor']:
        print("Invalid Input , Please Enter a valid Input in [rock,paper,scissor]")
    return player_choice

def choose_winner(player , computer) : 
    if player == computer :
        return "It is a tie!"
    
    elif(player == 'rock'and computer == 'scissor') or \
        (player == 'scissor' and computer == 'paper') or \
        (player == 'paper'  and computer == 'rock'):
        return "You Won!"
    
    else :
        return "You Lost!"
    
def play_game():
    while True :
        player_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer chose : ",computer_choice)
        result = choose_winner(player_choice , computer_choice)
        print(result)

        play_again = input("Do you want to play again(yes/no):").lower()
        if play_again == 'no':
            print("Thank you for Playing")
            break
play_game()