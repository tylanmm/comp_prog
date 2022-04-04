def solve(r, c):
    print('..+' + '-+'*(c-1))
    for i in range(r):
        print(('|' if i else '.') + '.|'*c)
        print('+' + '-+'*c)


for t in range(int(input())):
    r, c = map(int, input().split())
    print('Case #{}:'.format(t+1))
    solve(r, c)
