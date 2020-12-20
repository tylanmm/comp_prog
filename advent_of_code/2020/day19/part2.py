import sys

with open(sys.argv[1]) as f:
    rules, messages = f.read().split('\n\n')
    rules = rules.split('\n')
    messages = messages.split('\n')

g = {}
for r in rules:
    rule_num, rels = r.split(': ')
    if '|' in rels:
        rel1, rel2 = rels.split(' | ')
        g[rule_num] = [rel1.split(), rel2.split()]
    elif 'a' in rels or 'b' in rels:
        g[rule_num] = [rels[1:-1]]
    else:
        g[rule_num] = [rels.split()]

def concat(set1, set2):
    if len(set1) == 0:
        return set2
    
    res = set()
    for s1 in set1:
        for s2 in set2:
            res.add(s1 + s2)
    return res

dp = {}
def dfs(rule):
    if rule == '8':
        if '8' in dp:
            return dp['8']
        dp['8'] = dfs('42')
        dp['8'] = dp['42'].union(concat(dp['42'], '8*'))
        return dp['8']
    if rule == '11':
        if '11' in dp:
            return dp['11']
        temp = concat(dfs('42'), dfs('31'))
        dp['11'] = temp.union(concat(concat(dp['42'], '8*'), dp['31']))
        return dp['11']
    if rule in dp:
        return dp[rule]

    final = set()
    for rel in g[rule]:
        res = set()
        for child in rel:
            if child == 'a' or child == 'b':
                res.add(child)
            else:
                res = concat(res, dfs(child))
        final.update(res)
    dp[rule] = final
    return final

dfs('0')
print(dp['8'])
print(dp['11'])
total = 0
for s in messages:
    total += s in dp['0']
print(total)        