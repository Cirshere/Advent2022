f = open("./input.txt", "r")
line = f.readline()

values = {'A': 1, 'B': 2, 'C': 3}
options = ['A', 'B', 'C']
score = 0

while line:
    text = line.split(' ')
    oppo = options.index(text[0])
    cond = text[1].strip()
    yours = -1

    if (cond == 'X'):
        yours = (oppo - 1) % 3
    elif (cond == 'Y'):
        yours = oppo
        score += 3
    elif (cond == 'Z'):
        yours = (oppo + 1) % 3
        score += 6

    score += values[options[yours]]
    line = f.readline()

print(score)
f.close()