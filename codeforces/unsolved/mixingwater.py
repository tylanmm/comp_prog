for t in range(int(input())):
    h, c, t = map(int, input().split())
    if t <= (h+c)/2:
        print(2)
        continue

    cups = int((t - h)/(h + c - 2*t) * 2) + 1
    if abs((h*(cups + 1)//2 + c * cups//2)/cups - t) < abs((h*(cups + 3)//2 + c * (cups + 2)//2)/(cups + 2) - t):
        print(cups)
    else:
        print(cups + 2)