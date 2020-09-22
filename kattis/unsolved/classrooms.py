import heapq

n, k = map(int, input().split())
rooms = []
activities = sorted(sorted([tuple(map(int, input().split())) for _ in range(n)]), key=lambda x:x[1])

count = 0
for start, end in activities:
    if len(rooms) == 0:
        heapq.heappush(rooms, end)
        count += 1
    elif rooms[0] < start:
        heapq.heapreplace(rooms, end)
        count += 1
    elif len(rooms) < k:
        heapq.heappush(rooms, end)
        count += 1

print(count)