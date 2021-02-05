with open('socdist1.in') as f:
    n = int(f.readline())
    stalls = f.readline()

all_gaps = [len(gap) for gap in stalls.split('1')]
ends = [all_gaps[0], all_gaps[-1]]
gaps = sorted(all_gaps[1:-1], reverse=True)

hi = 0

if len(all_gaps) == 1:
    # there are no other cows
    hi = all_gaps[0] - 1

if len(gaps) > 0:
    if len(gaps) >= 2:
        # it's the two largest non-end gaps
        hi = max(hi, (gaps[1]+1)//2)
    
    # it's a shared non-end gap
    hi = max(hi, (gaps[0]+1)//3)
    # it's the left end and the largest gap
    hi = max(hi, min(ends[0], (gaps[0]+1)//2))
    # it's the right end and the largest gap
    hi = max(hi, min(ends[1], (gaps[0]+1)//2))

if len(all_gaps) >= 2:
    # it's the left end and the right end
    hi = max(hi, min(ends))
    # it's the shared left end
    hi = max(hi, ends[0]//2)
    # it's the shared right end
    hi = max(hi, ends[1]//2)

if len(gaps) > 0:
    # the smallest distance between already-placed cows
    hi = min(hi, gaps[-1] + 1)

with open('socdist1.out', 'w') as f:
    f.write(str(hi) + '\n')