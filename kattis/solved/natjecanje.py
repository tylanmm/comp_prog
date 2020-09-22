n, s, r = map(int, input().split())
kayaks = [1]*11
for t in map(int, input().split()):
    kayaks[t] -= 1
for t in map(int, input().split()):
    kayaks[t] += 1

def share(i):
    if i == n+1:
        return kayaks.count(0)
    
    best = n
    if kayaks[i] > 1:
        if i > 1 and kayaks[i-1] == 0:
            kayaks[i] -= 1
            kayaks[i-1] += 1
            best = min(best, share(i+1))
            kayaks[i] += 1
            kayaks[i-1] -= 1
        if i < n and kayaks[i+1] == 0:
            kayaks[i] -= 1
            kayaks[i+1] += 1
            best = min(best, share(i+1))
            kayaks[i] += 1
            kayaks[i+1] -= 1
    best = min(best, share(i+1))
    return best

print(share(1))