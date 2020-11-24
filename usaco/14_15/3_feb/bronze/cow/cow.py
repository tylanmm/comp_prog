# Read in the data
with open("cow.in") as f:
    raw = f.read().split()
    n = int(raw[0])
    chars = raw[1]

seen = {"C": 0, "CO": 0, "COW": 0}      # Keep track of the subsequences we actually care about
for c in chars:
    if c == "C":                        # If we see a "C",
        seen["C"] += 1                  #   Add 1 to the amount of times we have potentially started a "COW" subsequence
    elif c == "O":                      # If we see an "O",
        seen["CO"] += seen["C"]         #   Add the amount of times we have seen a "C" up to that point to the "CO" count
    else:                               # If we see a "W",
        seen["COW"] += seen["CO"]       #   Add the amount of times we have seen a "CO" subsequence so far to the "COW" count

# The value of seen["COW"] is our answer
with open("cow.out", "w") as f:
    f.write(str(seen["COW"]))