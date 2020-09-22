diffs = [1]
scores = [0, 1]
for _ in range(int(input())):
    n = int(input())
    while len(diffs) < n:
        for i in range(len(diffs)):
            diffs.append(diffs[i])
            scores.append(diffs[-1] + scores[-1])
        diffs[-1] += 1
        scores[-1] += 1
    print(scores[n])