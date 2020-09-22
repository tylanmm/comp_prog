_data = []

"""
The following three functions perform the basic 3 operations on the data:
 -  Complement (toggle each of the bits)
 -  Reverse (do a complete flip of the bits)
 -  Complement AND reverse (call both of the other functions)
"""
def complement(data):
    newData = [''] * len(data)
    for i in range(len(data)):
        if data[i] != '':
            newData[i] = int(not data[i])
        else:
            newData[i] = ''
    return newData

def reverse(data):
    return data[::-1]

def both(data):
    return complement(reverse(data))

"""
The following two functions find the first empty bit starting from
the left and the right, respectively. They return -1 if there is
no such empty bit, meaning that all bits are known
 -  Note: returns the bit index plus one, since the judge's bits
    are 1-indexed rather than 0-indexed
"""
def lfind(data):
    for i in range(len(data)):
        if data[i] == '':
            return i + 1
    return -1

def rfind(data):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == '':
            return i + 1
    return -1

"""
This function is called when there are no more empty bits, so it's
time to make a guess of the data
"""
def guess(data):
    print(''.join(map(str, data)))
    if input() == 'N':
        quit()

"""
Determine the bit that when coupled with the first bit, uniquely
determines the transformation that was applied
"""
def findSecond(data, prev):
    poss1 = []
    poss2 = []
    poss1Name = ''
    poss2Name = ''
    if data[0] == prev:
        poss1 = data
        poss1Name = 'data'
    else:
        poss1 = complement(data)
        poss1Name = 'complemented'
    
    reversed = reverse(data)
    if reversed[0] == prev:
        poss2 = reversed
        poss2Name = 'reversed'
    else:
        poss2 = both(data)
        poss2Name = 'both'
    
    for i in range(1, len(poss1)):
        if poss1[i] != poss2[i]:
            return i + 1
    
    if poss1Name == 'complemented':
        global _data
        _data = poss1
    return rfind(_data)

def determineOperation(bit1Val, bit2Val, bit2Index):
    global _data
    if _data[0] == bit1Val:
        if _data[bit2Index] == bit2Val:
            return
        reversed = reverse(_data)
        if reversed[0] == bit1Val and reversed[bit2Index] == bit2Val:
            _data = reversed
        else:
            _data = both(_data)
    else:
        complemented = complement(_data)
        if complemented[bit2Index] == bit2Val:
            _data = complemented
            return
        reversed = reverse(_data)
        if reversed[0] == bit1Val and reversed[bit2Index] == bit2Val:
            _data = reversed
        else:
            _data = both(_data)

"""
Based on current state of data and query number, make query
1.  If Num % 10 == 1, query bit one
2.  Else if queryNum % 10 == 2 but does not equal 2, then determine
    the bit that, when paired with the first, uniquely determines
    which operation took place
3.  Else if queryNum is odd, then query the first empty bit
4.  Else (queryNum is even), then query the last empty bit
"""
def query(data, numQ, prev):
    if numQ % 10 == 1:
        return 1

    elif numQ % 10 == 2 and numQ != 2:
        i = findSecond(data, prev)
        if i > -1:
            return i
        else:
            guess(_data)
            return 'done'

    elif numQ % 2 == 1:
        i = lfind(data)
        if i > -1:
            return i
        else:
            guess(data)
            return 'done'

    else:
        i = rfind(data)
        if i > -1:
            return i
        else:
            guess(data)
            return 'done'

def getResponse():
    return int(input())

def test(bits):
    global _data
    _data = [''] * bits
    numQ = 0
    bestQ = 0
    first = 0
    response = 0
    while numQ < 150:
        numQ += 1
        bestQ = query(_data, numQ, first)
        if bestQ == 'done':
            return
        print(bestQ)
        response = getResponse()
        if numQ % 10 > 2 or numQ <= 2 or numQ % 10 == 0:
            _data[bestQ - 1] = response
        elif numQ % 10 == 2 and numQ != 2:
            determineOperation(first, response, bestQ - 1)
        first = response

t, b = map(int, input().split())
for _ in range(t):
    test(b)