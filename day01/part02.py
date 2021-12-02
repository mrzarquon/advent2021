import json
from pathlib import Path


data_file = Path("puzzle01.txt")

data = data_file.read_text()

data = data.split("\n")

data = [int(d) for d in data]

i = 0
z = list()

for x in range(0, len(data) + 1):
    if x + 2 < len(data):
        amount = data[x] + data[x + 1] + data[x + 2]
        z.append(amount)

i = 0
for x, y in enumerate(z):
    if int(x) > 0:
        if int(y) > int(z[x - 1]):
            print(y, z[x - 1])
            i += 1


print(i)
print(len(z))
