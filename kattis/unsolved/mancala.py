boards = [[], [1]]
def genBoards(n):
    for i in range(len(boards)-1, n):
        board = [0] * (i+1)
        for j in range(i-1):
            board[j] = boards[i][j] - 1
        board[i] = i
        boards.append(board)

for p in range(int(input())):
    k, n = map(int, input().split())
    if len(boards) <= n:
        genBoards(n)
    
    print(f'{k} {len(boards[n])}')
    i = 0
    while i < len(boards[n]):
        print(' '.join(map(str, boards[n][i:min(i+10, len(boards[n]))])))
        i += 10