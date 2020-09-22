stack = []

def swap():
    if len(stack) > 1:
        t = stack.pop()
        n = stack.pop()
        stack.append(t)
        stack.append(n)
    else:
        print("Invalid swap operation")

def discard():
    if len(stack) > 0:
        stack.pop()
    else:
        print("Invalid remove operation")


instructions = {'SS': lambda n : stack.append(n),
                'SNS': lambda : stack.append(stack[-1]),
                'SNT': swap,
                'SNN': discard
                }