import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n\n')

nums = map(int, data[0].split(','))
boards = [[list(map(int, line.split())) for line in b.split('\n')] for b in data[1:]]

def place_num(num, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                board[i][j] = -1
                return

def check_win(board):
    # check rows
    for i in range(len(board)):
        if all([board[i][j] < 0 for j in range(len(board[i]))]):
            return True
    
    # check cols
    for j in range(len(board[0])):
        if all([board[i][j] < 0 for i in range(len(board))]):
            return True
    
    return False

def score(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                total += board[i][j]
    return total

left = len(boards)
done = [False]*len(boards)
for n in nums:
    for i, b in enumerate(boards):
        if done[i]: continue
        place_num(n, b)
        if check_win(b):
            left -= 1
            done[i] = True
        if left == 0:
            print(score(b) * n)
            quit()