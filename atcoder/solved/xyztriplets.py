N = int(input())
f = [0]*(N+1)

def solve(amt):
    for x in range(1, amt):
        for y in range(1, amt):
            for z in range(1, amt):
                n = x*x + y*y + z*z + x*y + y*z + x*z
                if n <= N:
                    f[n] += 1
                else:
                    break

if N > 2:
    solve(int((N-2)**0.5)+1)

for n in range(1, N+1):
    print(f[n])