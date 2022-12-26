#! /usr/bin/env python3

"""
python script to solve challenge 5 of Advent of Code challenges

    @copyright:
        Copyright (c) Sidd Srivatsa, Inc. 2022 All Rights Reserved

        This file contains confidential and proprietary information. Any use of
        this code, including without limitation reproduction, modification,
        distribution or republication, without the prior written consent of
        Sidd Srivatsa, Inc., is strictly prohibited.
"""


f = '../data/day5.txt'

data = open(f).read()
points = 0
lines = [x for x in data.split('\n')]

crate_stack_map = {}
data_populate_idx = 0

for line in lines:
    data_populate_idx = data_populate_idx + 1
    if not any(c.isalpha() for c in line):
        print("Done populating crate stack map, ready for re-arranging\n")
        break

    crate_idx = 0
    for crate in line:
        crate_idx = crate_idx + 1
        if crate == ' ' or crate == '[' or crate == ']':
            continue
        else:
            # print("crate: {}, at idx: {}".format(crate, int(crate_idx / 4)+1))
            crate_stack_map.setdefault(int(crate_idx / 4)+1,[]).append(crate)
    print(line)
del lines[0:data_populate_idx+1]
print(crate_stack_map)

for line in lines:
    if line == '':
        # print("Done moving crates")
        break
    mv_cmd = line.split(" ")
    num_crates = int(mv_cmd[1])
    from_crate = int(mv_cmd[3])
    to_crate = int(mv_cmd[5])
    print("Move {} from {} to {}".format(num_crates, from_crate, to_crate))
    print("{}: {}\n{}: {}\nAfter".format(from_crate, crate_stack_map[from_crate], to_crate, crate_stack_map[to_crate]))
    for i in range (0, num_crates):
        crate_stack_map[to_crate].insert(0, crate_stack_map[from_crate].pop(0))
    print("{}: {}\n{}: {}\n\n".format(from_crate, crate_stack_map[from_crate], to_crate, crate_stack_map[to_crate]))

top_stack = ''
for i in range(1, len(crate_stack_map)+1):
    top_stack = top_stack + crate_stack_map[i][0]
print("Top stack: {}".format(top_stack))

# Challenge 2
f = '../data/day5.txt'

data = open(f).read()
points = 0
lines = [x for x in data.split('\n')]

crate_stack_map = {}
data_populate_idx = 0

for line in lines:
    data_populate_idx = data_populate_idx + 1
    if not any(c.isalpha() for c in line):
        print("Done populating crate stack map, ready for re-arranging\n")
        break

    crate_idx = 0
    for crate in line:
        crate_idx = crate_idx + 1
        if crate == ' ' or crate == '[' or crate == ']':
            continue
        else:
            # print("crate: {}, at idx: {}".format(crate, int(crate_idx / 4)+1))
            crate_stack_map.setdefault(int(crate_idx / 4)+1,[]).append(crate)
    print(line)
del lines[0:data_populate_idx+1]
print(crate_stack_map)

for line in lines:
    if line == '':
        # print("Done moving crates")
        break
    mv_cmd = line.split(" ")
    num_crates = int(mv_cmd[1])
    from_crate = int(mv_cmd[3])
    to_crate = int(mv_cmd[5])
    print("Move {} from {} to {}".format(num_crates, from_crate, to_crate))
    print("{}: {}\n{}: {}\nAfter".format(from_crate, crate_stack_map[from_crate], to_crate, crate_stack_map[to_crate]))
    for i in range (num_crates-1, -1, -1):
        crate_stack_map[to_crate].insert(0, crate_stack_map[from_crate].pop(i))
    print("{}: {}\n{}: {}\n\n".format(from_crate, crate_stack_map[from_crate], to_crate, crate_stack_map[to_crate]))

top_stack = ''
for i in range(1, len(crate_stack_map)+1):
    top_stack = top_stack + crate_stack_map[i][0]
print("Top stack: {}".format(top_stack))
