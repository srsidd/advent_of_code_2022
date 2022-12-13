#! /usr/bin/env python3

"""
python script to solve advent of code challenges

    @copyright:
        Copyright (c) Sidd Srivatsa, Inc. 2022 All Rights Reserved

        This file contains confidential and proprietary information. Any use of
        this code, including without limitation reproduction, modification,
        distribution or republication, without the prior written consent of
        Sidd Srivatsa, Inc., is strictly prohibited.
"""


def read_file(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines

f = 'day1.txt'

data = read_file(f)
sum = [0, 0, 0]
current_sum = 0
elf = 0
best_elf = [0, 0, 0]

for line in data:
    if line == '\n':
        if current_sum > min(sum):
            sum[sum.index(min(sum))] = current_sum
            best_elf[sum.index(min(sum))] = elf
        current_sum = 0
        elf = elf + 1
    else:
        current_sum = current_sum + int(line.rstrip())

if current_sum > min(sum):
    sum[sum.index(min(sum))] = current_sum
    best_elf[sum.index(min(sum))] = elf

print("Elf number {} has most calories: {}".format(best_elf[sum.index(max(sum))], max(sum)))
print("Top three Elves are {}, with most calories {}, which adds up to {}".format(best_elf, sum, sum[0]+sum[1]+sum[2]))
