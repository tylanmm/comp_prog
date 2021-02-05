import sys

with open(sys.argv[1]) as f:
    data = f.read()

print(data.count('(') - data.count(')'))