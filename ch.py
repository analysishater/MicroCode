with open('input2.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

stack = []

for i in lines:
    if "push" in i:
        n = int(i[5:])
        stack.append(n)
    elif "pop" in i:
        if stack:
            stack.pop()
    elif "dup" in i:
        if stack:
            if "dup3" in i:
                if len(stack) >= 3:
                    stack += [stack[-3]] * 3
            elif "dup2" in i:
                if len(stack) >= 2:
                    stack += [stack[-2]] * 2
            else:
                stack.append(stack[-1])
    elif "rol" in i:
        n = int(i[4:].strip())
        if len(stack) >= n:
            top = stack.pop()
            stack.insert(len(stack) - (n - 1), top)
    elif "xor" in i:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j ^ k)
    elif "or" in i:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j | k)   # bitwise OR
    elif "and" in i:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j & k)   # bitwise AND
    elif "sub" in i:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j - k)
    elif "sum" in i:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j + k)
    elif "inc" in i:
        if stack:
            stack[-1] += 1
    elif "dec" in i:
        if stack:
            stack[-1] -= 1
    elif "not" in i:
        if stack:
            stack[-1] = ~stack[-1]
    elif "shl" in i:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j << k)
    else:
        if len(stack) >= 2:
            k, j = stack.pop(), stack.pop()
            stack.append(j >> abs(k))

if stack:
    if len(stack) == 1:
        print(stack[0])  # fixed: was print(stack)
    else:
        result = stack[0]
        for j in range(1, len(stack)):
            result ^= stack[j]
        print(result)
else:
    print("Stack is empty")