from sys import stdin

def has_problem(line):
    if ord(line[0]) < ord('A') or ord(line[0]) > ord('Z'):
        # print(line, 'cap')
        return True
    if line.count('.') != 1 or line[-1] != '.':
        # print(line, 'per')
        return True
    for i in range(len(line)):
        if line[i] == ',' and (line[i + 1] != ' ' or line[i-1] == ' '):
            # print(line, 'com')
            return True
        if line[i] == ' ' and line[i+1] == ' ':
            # print(line, 'spa')
            return True
    return False

i = 1
res = []
for line in stdin:
    if has_problem(line.strip()):
        res.append(str(i))
    i += 1
print(' '.join(res) if res else 'No Problems')