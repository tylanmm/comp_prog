def check(letters, i, s):
    if len(letters) == 0:
        return True
    if i + len(letters) > len(s) or (s[i] != letters[0] and s[i] != '?'):
        return False
    return check(letters[1:], i+1, s)

for _ in range(int(input())):
    n, s = int(input()), list(input())
    canWork = [i for i in range(len(s)-6) if check('abacaba', i, s)]
    
    for i in canWork:
        for j in canWork:
            if i == j:
                continue
            if abs(i-j) < 7:
                if j < i and '?' not in s[j:i]:
                    break
                elif j > i and '?' not in s[i+7:j+7]:
                    break
        else:
            print('Yes')
            s[i:i+7] = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
            for j in range(n):
                s[j] = 'z' if s[j] == '?' else s[j]
            print(''.join(s))
            break
    else:
        print('No')