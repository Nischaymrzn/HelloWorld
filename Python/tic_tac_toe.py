def tic_tac_toe(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return f"{row[0]} wins!"
    return "No winner!"
