def boards(board):
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            l = 0
            d = 0
            if board[i][j] == 1:
                if i - 1 >= 0 and j - 1 >= 0 and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == 2):
                    l += 1
                if i - 1 >= 0 and (board[i - 1][j] == 1 or board[i - 1][j] == 2):
                    l += 1
                if i - 1 >= 0 and j + 1 < m and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == 2):
                    l += 1
                if j - 1 >= 0 and (board[i][j - 1] == 1 or board[i][j - 1] == 2):
                    l += 1
                if j + 1 < m and (board[i][j + 1] == 1 or board[i][j + 1] == 2):
                    l += 1
                if i + 1 < n and j - 1 >= 0 and (board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == 2):
                    l += 1
                if i + 1 < n and (board[i + 1][j] == 1 or board[i + 1][j] == 2):
                    l += 1
                if i + 1 < n and j + 1 < m and (board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == 2):
                    l += 1

                if l < 2 or l > 3:
                    board[i][j] = 2
            else:
                if i - 1 >= 0 and j - 1 >= 0 and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == 2):
                    d += 1
                if i - 1 >= 0 and (board[i - 1][j] == 1 or board[i - 1][j] == 2):
                    d += 1
                if i - 1 >= 0 and j + 1 < m and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == 2):
                    d += 1
                if j - 1 >= 0 and (board[i][j - 1] == 1 or board[i][j - 1] == 2):
                    d += 1
                if j + 1 < m and (board[i][j + 1] == 1 or board[i][j + 1] == 2):
                    d += 1
                if i + 1 < n and j - 1 >= 0 and (board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == 2):
                    d += 1
                if i + 1 < n and (board[i + 1][j] == 1 or board[i + 1][j] == 2):
                    d += 1
                if i + 1 < n and j + 1 < m and (board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == 2):
                    d += 1
                if d == 3:
                    board[i][j] = 3
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                board[i][j] = 0
            elif board[i][j] == 3:
                board[i][j] = 1
    return board
print(boards([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))