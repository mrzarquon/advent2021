import json
from pathlib import Path


data_file = Path("puzzle01.txt")

data = data_file.read_text()

data = data.split("\n")

end = len(data[0])
total = len(data)

gamma = [0 for x in range(0, end)]
epsilon = [0 for x in range(0, end)]


for x in range(0, end):
    z = 0
    for d in data:
        z += int(d[x])
    remainder = total - z
    gamma[x] = int(z > remainder)
    epsilon[x] = int(z < remainder)

gamma = "".join([str(g) for g in gamma])
epsilon = "".join([str(g) for g in epsilon])

print(int(f"0b{gamma}", 2) * int(f"0b{epsilon}", 2))
