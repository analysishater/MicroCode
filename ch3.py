with open('input3.txt', 'r') as file:
    content = file.read()

lines = [int(item.strip()) for item in content.split(',') if item.strip().lstrip('-').isdigit()]
lines.append(468)

for i in range(len(lines)):
    lines[i] = [lines[i], 0]

rounds = 0
c = True

while c:
    i = 0
    c = False
    s = False
    indices = []  # reset every iteration
    while i < len(lines) and not s:
        if lines[i][0] != 0:
            c = True
            if lines[i][1] != 0:
                lines[i][1] -= 1
                i += 1
            else:
                s = True
                lines[i][1] = 13
        else:
            i += 1

    if s:
        indices.append(i)
        k = i + 2

        if i == 0:
            while k < len(lines) - 1:
                if lines[k][0] != 0:
                    if lines[k][1] == 0:
                        lines[k][1] = 13
                        indices.append(k)
                        k += 2
                    else:
                        lines[k][1] -= 1
                        k += 1
                else:
                    k += 1
        else:
            while k < len(lines):
                if lines[k][0] != 0:
                    if lines[k][1] == 0:
                        lines[k][1] = 13
                        indices.append(k)
                        k += 2
                    else:
                         
                        lines[k][1] -= 1
                        k += 1
                else:
                    k += 1

        if indices !=[]:
            done = False
            while not done:
                for j in indices:
                    print("hi")
                    lines[j][0] -= 1
                    if lines[j][0] == 0:
                        done = True
                rounds += 1

print(rounds)