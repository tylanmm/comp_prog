n, s, r = map(int, input().split())
amt = [1]*n
for t in map(int, input().split()):
    amt[t-1] -= 1
for t in map(int, input().split()):
    amt[t-1] += 1

def dfs(state, i, amt):
    if i == len(state):
        return amt
    if state[i] != 2:
        return dfs(state, i+1, amt)
    
    left = right = amt
    if i != 0 and state[i-1] == 0:
        left = dfs(state, i+1, amt-1)
    if i < len(state) - 1 and state[i+1] == 0:
        state[i+1] = 1
        right = dfs(state, i+1, amt-1)
        state[i+1] = 0
    return min(left, right)

print(dfs(amt, 0, amt.count(0)))