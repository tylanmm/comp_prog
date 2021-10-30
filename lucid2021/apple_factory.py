from collections import Counter
freq = Counter(input())
s = 'ale'
lo = float('inf')
for c in 'ale':
    lo = min(lo, freq[c])
lo = min(lo, freq['p']//2)
print(lo)