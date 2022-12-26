#! /usr/bin/env python3

"""
python script to solve challenge 6 of Advent of Code challenges

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

f = '../data/day6.txt'

data = read_file(f)

for i in range(0, len(data[0])):
    sequence = data[0][i:i+4]
    if len(set(sequence)) == 4:
        print("Found first unique first 4 characters: {} at idx: {}".format(sequence, i+4))
        break
    if i > len(data[0]) - 4:
        break

# Challenge 2
