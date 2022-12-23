#! /usr/bin/env python3

"""
python script to solve challenge 4 of Advent of Code challenges

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

f = '../data/day4.txt'

data = read_file(f)
points = 0

for line in data:
    sections = line.rstrip().split(",")

    elf1 = sections[0].split("-")
    elf2 = sections[1].split("-")

    elf1_1 = int(elf1[0])
    elf1_2 = int(elf1[1])

    elf2_1 = int(elf2[0])
    elf2_2 = int(elf2[1])

    if elf1_1 >= elf2_1 and elf1_2 <= elf2_2:
        print("Pair overlap, elf1: {}, elf2: {}".format(elf1, elf2))
        points = points + 1
    elif elf2_1 >= elf1_1 and elf2_2 <= elf1_2:
        print("Pair overlap, elf2: {}, elf1: {}".format(elf2, elf1))
        points = points + 1

print("Total number of overlaps: {}".format(points))
