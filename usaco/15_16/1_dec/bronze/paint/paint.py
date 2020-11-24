with open('paint.in') as f:
    a, b, c, d = map(int, f.read().split())

# Create a set containing all of the fence intervals
fences = set()
for i in range(a, b):
    fences.add(i)
for i in range(c, d):
    fences.add(i)

with open('paint.out', 'w') as f:
    f.write(str(len(fences)) + '\n')