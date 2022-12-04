f = open("./input.txt", "r")
line = f.readline()

values = {'A': 1, 'B': 2, 'C': 3}
rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']

options = ['A', 'B', 'C']

score = 0

while line:
    text = line.split(' ')
    oppo = ord(text[0]) + 23
    yours = ord(text[1].strip())

    # You: Scissors; Oppo: Rock
    if (oppo == 88 and yours == 90):
        score += 0
    # You: Rock; Oppo: Scissors
    elif(oppo == 90 and yours == 88):
        score += 6
    elif (oppo > yours):
        score += 0
    elif (oppo == yours):
        score += 3
    elif (oppo < yours):
        score += 6

    score += values[text[1].strip()]
    line = f.readline()

print(score)
f.close()