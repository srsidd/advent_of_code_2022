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

f = '../data/day3.txt'

data = read_file(f)
points = 0

for line in data:
    first_compartment = line[0:int(len(line)/2)].rstrip()
    second_compartment = line[int(len(line)/2):].rstrip()
    print('data input: {}, with len: {}, and midpt: {}'.format(line.rstrip(), len(line), len(line)/2-1))
    print('first_component: {}'.format(first_compartment))
    print('second_component: {}'.format(second_compartment))

    common_letters = ''.join(set(first_compartment).intersection(second_compartment))
    print('common_letters: {}'.format(common_letters))

    for common_letter in common_letters:
        if common_letter.isupper():
            pts_to_add = ord(common_letter) - 38
        elif common_letter.lower():
            pts_to_add = ord(common_letter) - 96

        print('pts_to_add: {}\n'.format(pts_to_add))
        points = points + pts_to_add

print("Total points: {}".format(points))
