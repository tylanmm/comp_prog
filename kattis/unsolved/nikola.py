n = int(input())
squares = [int(input()) for _ in range(n)]
costs = [[float('inf')]*n for _ in range(n)]
costs[0][0] = 0

for jump in range(n-1):
    for square in range(n):
        if square + jump < n:       # if we can get to current square by jumping back from somewhere
            costs[square][jump] = min(costs[square][jump], squares[square] + costs[square+jump][jump])
        if square + jump + 1 < n:   # if we can get to somewhere with the current jump distance
            costs[square+jump+1][jump+1] = min(costs[square+jump+1][jump+1], costs[square][jump] + squares[square+jump+1])

print(min(costs[n-1]))