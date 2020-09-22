import heapq
n = int(input())
boxes = sorted(list(map(int, input().split())))
piles = [1]

for b in boxes[1:]:
    if piles[0] <= b:
        heapq.heappush(piles, heapq.heappop(piles)+1)
    else:
        heapq.heappush(piles, 1)

print(len(piles))