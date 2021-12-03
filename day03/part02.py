import json
from os import O_EXCL
from pathlib import Path


data_file = Path("puzzle01.txt")

data = data_file.read_text()

data = data.split("\n")

end = len(data[0])
total = len(data)

gamma = [0 for x in range(0, end)]
epsilon = [0 for x in range(0, end)]

oxy = [0 for x in range(0, end)]
car = [0 for x in range(0, end)]


def get_col(data, pos):
    foo = [int(d[pos]) for d in data]
    # print(foo)
    return foo


def get_sig(col):
    ones = sum(col)
    total = len(col) - ones
    foo = int(ones >= total)
    # print(foo)
    return foo


def get_insig(col):
    ones = sum(col)
    total = len(col) - ones
    foo = int(ones < total)
    # print(foo)
    return foo


def get_sig_row(data, pos, sig):
    rows = [i for i in data if int(i[pos]) == int(sig)]
    # print(rows)
    return rows


oxy_data = data.copy()
for x in range(0, end):
    if len(oxy_data) > 1:
        col = get_col(oxy_data, x)
        sig = get_sig(col)
        oxy_data = get_sig_row(oxy_data, x, sig)
        # print(oxy_data)

car_data = data.copy()
for x in range(0, end):
    if len(car_data) > 1:
        col = get_col(car_data, x)
        sig = get_insig(col)
        car_data = get_sig_row(car_data, x, sig)
        # print(car_data)

print(oxy_data)
print(car_data)

print(int(f"0b{oxy_data[0]}", 2) * int(f"0b{car_data[0]}", 2))
