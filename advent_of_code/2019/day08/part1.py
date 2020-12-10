from sys import argv

w, h = 25, 6

with open(argv[1]) as f:
    data = f.read().strip()

layer = None
amt = len(data)
for i in range(0, len(data), h*w):
    lay = data[i:i+h*w]
    num0 = lay.count('0')
    if num0 < amt:
        amt = num0
        layer = lay

print(layer.count('1') * layer.count('2'))