"""
 Given a position of coins of player1 and player2 in a 3X3 Tic Tac Toc board, write a program to
determine if the board position is a solution and if so identify the winner of the game. In a Tic Tac Toc
problem, if the coins in a row or column or along a diagonal is of the same player then he has won the
game. Assume that player1 uses ‘1’ as his coin and player2 uses '2' as his coin. '0' in the board represent
empty cell.
"""


def getResult(board):
    game_result = 0
    # checking diagonal1
    for i in range(len(board)):
        if board[i][i] == 1:
            return 1
        elif board[i][i] == 2:
            return 2

    # checking diagonal2
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] == 1:
            return 1
        elif board[i][len(board) - 1 - i] == 2:
            return 2

    # checking row wise
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                return 1
            elif board[i][j] == 2:
                return 2

    # checking column wise
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == 1:
                return 1
            elif board[j][i] == 2:
                return 2

    return game_result


n = 3
board = list()
for i in range(n):
    row_list = list()
    for j in range(n):
        x = int(input("Enter the value: "))
        row_list.append(x)
    board.append(row_list)


result = getResult(board)
if result == 1:
    print("Player1 Wins!!!!")
elif result == 2:
    print("Player2 Wins!!!!")
else:
    print("Draw Match")
