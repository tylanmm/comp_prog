alphabet = 'abcdefghijklmnopqrstuvwxyz'
def convert(num):
    i, n = 1, 26
    while n < num:
        num -= n
        n *= 26
        i += 1
    num -= 1
    
    res = ''
    while num >= 26:
        res = alphabet[num % 26] + res
        num //= 26
    return '{:{fill}{align}{width}}'.format(alphabet[num % 26] + res, fill='a', align='>', width=i)

print(convert(int(input())))