for t in range(int(input())):
    n, height = int(input()), list(map(int, input().split()))
    peaks = 0
    for i in range(1, n-1):
        peaks += height[i-1] < height[i] and height[i] > height[i+1]
    print('Case #%d: %d' % (t+1, peaks))