# get input
nums = list(map(int, input().split()))

# because every number is positive, 
# the largest thing in nums is a+b+c
abc = max(nums)

# similarly, the smallest thing must be one of a, b, or c
# without loss of generality, let's decide it's a
a = min(nums)

# the next smallest thing could only be one of b or c
# again, W.L.O.G., let's decide it's b
nums.remove(a)
b = min(nums)

# with a, b, and a+b+c, we can now get c
# (a + b + c) - a - b = c
c = abc - a - b

print(a, b, c)