# read input from stdin
n = int(input())
petals = list(map(int, input().split()))

numPhotosWithAverage = 0

# un-optimized O(n^3) approach: loop over every possible range
for i in range(n):
    for j in range(i, n):
        # count total petals in the range
        total = 0
        for k in range(i, j+1):
            total += petals[k]
        
        # see if there's a flower in the range with the average amount of petals
        hasAverage = False
        averagePetals = total / (j - i + 1)
        for k in range(i, j+1):
            # this is just in case of floating point errors
            # (might not even be necessary)
            if abs(petals[k] - averagePetals) < 0.00001:
                hasAverage = True
                break
        if hasAverage:
            numPhotosWithAverage += 1

print(numPhotosWithAverage)