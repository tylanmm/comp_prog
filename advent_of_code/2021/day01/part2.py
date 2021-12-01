import sys

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split('\n')))

ans = 0
for i in range(3, len(data)):
    ans += data[i] > data[i-3]
print(ans)