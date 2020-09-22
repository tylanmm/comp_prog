# Read in the data
with open("censor.in") as f:
    s, t = f.read().split()

out = s[:len(t)]                    # Make a string containing the first len(t) letters of s
for i in range(len(t), len(s)):     # For every character in s,
    out += s[i]                     #   Put it in our string of seen characters
    if out[-len(t):] == t:          #   If the last len(t) letters == t,
        out = out[:-len(t)]         #       Cut off that portion of the string

# Answer is what remains after that process
with open("censor.out", "w") as f:
    f.write(out)