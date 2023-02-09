import Logic, Interface

def movement(where, who):
    if where.lower() in Logic.board:
        if who.lower() == "player 1":
            Logic.board[where] = Logic.player1
        elif who.lower() == "player 2":
            Logic.board[where] = Logic.player2
        else:
            print("Invalid Player")
    else:
        print("ERROR")