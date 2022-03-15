b, c, d, l = map(int, input().split())
no_solution = True
for x in range(0, l//b+1):
    for y in range(0, l//c+1):
        for z in range(0, l//d+1):
            if x*b + y*c + z*d == l:
                no_solution = False
                print(x, y, z)
if no_solution:
    print('impossible')