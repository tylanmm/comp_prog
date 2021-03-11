'''
It turns out that the only thing that matters when determining
whether the fence was CW or CCW is how many times we turn left
and how many times we turn right. If we turn left more than we
turn right, then it was CCW. Otherwise, it was CW.

As you loop over a given fence, track how many times you turn
in either direction. Use that final count to determine what 
the answer is for a given fence.
'''

# Count the number of lefts and rights
# More rights than lefts = clockwise
# More lefts than rights = counter-clockwise
def solve(fence):
    dirs = 'NESW'
    balance = 0
    for i in range(1, len(fence)):
        # Check if the current direction comes before or after the previous
        # If it comes right after, then its a right turn
        # If it comes right before (or 3 steps after), then its a left turn
        # You could check this in several other ways I'm sure
        d = (dirs.index(fence[i]) - dirs.index(fence[i-1])) % 4
        if d == 1:      # Right turn, so add
            balance += 1
        elif d == 3:    # Left turn, so substract
            balance -= 1
    return 'CW' if balance > 0 else 'CCW'

# Read and process inputs
n = int(input())
for i in range(n):
    fence = input()
    print(solve(fence))