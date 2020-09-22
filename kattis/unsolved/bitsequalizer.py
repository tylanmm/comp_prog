for _ in range(int(input())):
    s, t = input(), input()
    count, sOnes, tOnes = 0, 0, 0
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] == '1':
                count += 1
                sOnes += 1
            elif s[i] == '?':
                if t[i] == '1' and sOnes > 0:
                    sOnes -= 1
                count += 1
            else:
                tOnes += 1
    
    if sOnes > tOnes:
        print(f'Case {_+1}: -1')
    elif sOnes == tOnes:
        print(f'Case {_+1}: {count}')
    else:
        print(f'Case {_+1}: {count + tOnes - sOnes}')