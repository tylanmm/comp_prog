'''
We don't care about actual fixed years, just differences between them,
so here I arbitrarily decided that Bessie was born in year 0.
For each phrase, we are guaranteed to already know the year that the
second cow was born, so we just need to find out the difference in
time between that second cow's birth year and first cow's birth year.

The input is small enough that we can just look up the index of each
animal for every phrase, though to be more efficient we could make a
dictionary (e.g., {Ox: 0, Tiger: 1, ...}). Depending on whether the
phrase says "previous" or "next", we have to go backwards or forwards
the difference in time between the animal year of the second name
and the animal year of the first name.

At the end, we will have a dictionary of the years that each cow was
born relative to Bessie's birth year. The answer is just the absolute
difference between Bessie's birth year and Elsie's birth year.
'''

# Setup initial input
n = int(input())
animals = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
years = {'Bessie': 0}
animal = {'Bessie': 'Ox'}

# Process all of the phrases
for i in range(n):
    # Get information from the phrase
    line = input().split()
    n1 = line[0]
    n2 = line[-1]
    a = line[4]
    isPrev = line[3]

    # Get the difference in years between two animals
    # Have to be careful, since the animals are in a cycle
    if isPrev == 'previous':
        diff = -((animals.index(animal[n2]) - animals.index(a)) % 12)
    else:
        diff = (animals.index(a) - animals.index(animal[n2])) % 12
    
    # Edge case: they were born in the "same" year
    # Just add or subtract 12 (depending on situation)
    if diff == 0:
        if isPrev == 'previous':
            diff = -12
        else:
            diff = 12
    
    # Set year of name 1 to be the year of name 2 plus that difference
    years[n1] = years[n2] + diff
    animal[n1] = a

print(abs(years['Bessie'] - years['Elsie']))