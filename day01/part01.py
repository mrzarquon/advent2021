import json
from pathlib import Path


data_file = Path("puzzle01.txt")

data = data_file.read_text()

data = data.split("\n")

i = 0
z = list()
for x, y in enumerate(data):
    if int(x) > 0:
        if int(y) > int(data[x - 1]):
            print(y, data[x - 1])
            z.append(y)
            i += 1

print(i)
print(len(z))
