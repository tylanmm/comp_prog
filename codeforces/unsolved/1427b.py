for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    
    # get the in-between
    for i in range(1, n-1):
        if k:
            if s[i] == 'L' and s[i-1] == 'W' and s[i+1] == 'W':
                s[i] = 'W'
                k -= 1
        else:
            break
    
    # get the pre
    for i in range(n-2, -1, -1):
        if k:
            if s[i] == 'L' and s[i+1] == 'W':
                s[i] = 'W'
                k -= 1
        else:
            break
    
    # get the post
    for i in range(1, n):
        if k:
            if s[i] == 'L' and s[i-1] == 'W':
                s[i] = 'W'
                k -= 1
        else:
            break

    # calculate score
    score = 0
    for i in range(n):
        if k and s[i] == 'L':
            s[i] = 'W'
            k -= 1
        if s[i] == 'W':
            score += 1 + ((s[i-1] == 'W') if i else 0)
    
    print(score)

'''

        if s[i] == 'W':
            curr += 1 + (s[i-1] == 'W')
'''