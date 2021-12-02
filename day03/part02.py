import json
from pathlib import Path


data_file = Path("puzzle01.txt")

data = data_file.read_text()

data = data.split("\n")

data = [(str(d.split()[0]), int(d.split()[1])) for d in data]

# [0] = x, [1] = z
pos = list((0, 0, 0))

for coor in data:
    direction = coor[0]
    amount = coor[1]
    if direction == "forward":
        pos[0] = pos[0] + amount
        pos[1] += pos[2] * amount
    elif direction == "down":
        pos[2] = pos[2] + amount
    else:
        pos[2] = pos[2] - amount

    print(pos[0], pos[1])

print(pos[0], pos[1])
print(pos[0] * pos[1])
