from collections import Counter

s = input()
n = len(s)
costs = [0] + list(map(int, input().split()))


def search(i, subs):
    if i == n:
        return sum([costs[len(sub)] for sub in subs if subs[sub]])

    cost = float('inf')
    for j in range(i, n):
        curr = s[i:j+1]
        subs[curr] += 1
        cost = min(cost, search(j+1, subs))
        subs[curr] -= 1

    return cost


print(search(0, Counter()))
