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

f = '../data/day7_test.txt'
f = '../data/day7.txt'
data = read_file(f)

folder_size = 0
folder_map = {}
current_folder = ''
first_run = True

for line in data:
    cmds = line.rstrip().split(" ")

    if cmds[0] == '$':
        if cmds[1] == 'cd':
            if cmds[2] == '..':
                # Drop current folder
                folders = current_folder.split('/')[1:-1]
                current_folder_size = folder_map[current_folder]['size']
                current_folder = ''
                for folder in folders:
                    current_folder = current_folder + '/' + folder
                folder_map[current_folder]['size'] = folder_map[current_folder]['size'] + current_folder_size
                folder_size = 0
            else:
                if first_run:
                    first_run = False
                else:
                    current_folder = current_folder + '/' + cmds[2]
                    if current_folder not in folder_map:
                        folder_map.setdefault(current_folder, {'size': 0})
    elif cmds[0].isdigit():
        file_size = int(cmds[0])
        folder_size = folder_size + file_size
        folder_map[current_folder]['size'] = folder_map[current_folder]['size'] + file_size
    elif cmds[0] == 'dir':
        if current_folder not in folder_map:
            folder_map.setdefault(current_folder, {'size': 0})
    print('cmds: {}'.format(cmds))

points = 0
for folder in folder_map:
    current_size = folder_map[folder]['size']
    print('current_folder: {} with size {}'.format(folder, current_size))
    if current_size < 100000:
        points = points + current_size

print("Total size of folders: {}".format(points))
