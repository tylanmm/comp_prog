with open('meetings.in') as f:
    n, l = map(int, f.readline().split())
    cows = [tuple(map(int, f.readline().split())) for _ in range(n)]
