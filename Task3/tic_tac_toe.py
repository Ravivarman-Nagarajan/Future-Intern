board = ['-' for _ in range(10)]

def display_board():
    print("|", board[1], "|", board[2], "|", board[3], "|")
    print("|", board[4], "|", board[5], "|", board[6], "|")
    print("|", board[7], "|", board[8], "|", board[9], "|")

player1 = "X"
player2 = "O"

def check_conditions(player):
    conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 4, 7], [2, 5, 8], [3, 6, 9], 
        [1, 5, 9], [3, 5, 7]
    ]
    for check in conditions:
        if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
            return True
    return False

def startgame():
    display_board()
    while True:
        while True:
            player1_option = input(f"{player1}, Enter Your Position: ")

            if player1_option not in [str(i) for i in range(1, 10)]:
                print("Please Enter Valid Number[1-9]")
                continue

            if board[int(player1_option)] == "-":
                board[int(player1_option)] = player1
                display_board()
                if check_conditions(player1):
                    print(f'Winner of the game is {player1}')
                    return
                break
            else:
                print("Position is already taken, try another box!")

        if "-" not in board[1:]:
            print("The game is a tie!")
            return

        while True:
            player2_option = input(f"{player2}, Enter Your Position: ")

            if player2_option not in [str(i) for i in range(1, 10)]:
                print("Please Enter Valid Number[1-9]")
                continue

            if board[int(player2_option)] == "-":
                board[int(player2_option)] = player2
                display_board()
                if check_conditions(player2):
                    print(f'Winner of the game is {player2}')
                    return
                break
            else:
                print("Position is already taken, try another box!")

        if "-" not in board[1:]:
            print("The game is a tie!")
            return

startgame()
