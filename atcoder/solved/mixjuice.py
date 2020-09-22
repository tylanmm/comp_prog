import heapq
n, k = map(int, input().split())
fruits = list(map(int, input().split()))
heapq.heapify(fruits)
print(sum(heapq.nsmallest(k, fruits)))