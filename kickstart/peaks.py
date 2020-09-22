for i in range(int(input())):
    n = int(input())
    peaks = list(map(int, input().split()))
    count = 0
    for j in range(1, n-1):
        if peaks[j] > peaks[j-1] and peaks[j] > peaks[j+1]:
            count += 1
    print('Case #%d: %d' % (i+1, count))