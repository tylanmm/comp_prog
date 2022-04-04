from sys import setrecursionlimit
setrecursionlimit(100002)


def solve(mod):
    children = [solve(child) for child in tree[mod]]
    # lo = lowest scoring child so far
    # res = total score in subtree
    lo, res = float('inf') if tree[mod] else 0, 0
    for hi_c, res_c in children:
        res += hi_c + res_c     # all children (except lowest) end here
        lo = min(lo, hi_c)      # find the lowest scoring child
    # score so far is res, minus the lowest scoring child (which doesn't end yet)
    return max(lo, f[mod]), res - lo


for t in range(int(input())):
    n = int(input())
    f = [0] + list(map(int, input().split()))
    p = [0] + list(map(int, input().split()))
    tree = [set() for _ in range(len(p)+1)]
    for i in range(1, len(p)):
        tree[p[i]].add(i)
    lo, res = solve(0)
    print('Case #{}: {}'.format(t+1, lo + res))
