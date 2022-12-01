elfs = [0]
counter = 0

f = open("./input.txt", "r")
line = f.readline()

while line:
    if line == "\n":
        counter += 1
        elfs.append(0)
    else:
        elfs[counter] += int(line)
        
    line = f.readline()

# Part 1 - Answer: finds calories of highest elf
print("Calories of the highest elf")
print(max(elfs))

top = [0, 0, 0]
for e in elfs:
    mini = min(top)
    if (e > mini):
        top.remove(mini)
        top.append(e)

# Part 2 - Answer: find calories of top 3 elves
print("Calories sum of top 3 elves")
print(sum(top))

f.close()