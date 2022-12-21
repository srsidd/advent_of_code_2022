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

f = '../data/day2.txt'

data = read_file(f)
sum = [0, 0, 0]

win = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
# loss = ['A ', 'B ', 'C ']
points = 0

for line in data:
    their_action = line.split(' ')[0].rstrip()
    my_action = line.split(' ')[1].rstrip()
    if my_action == 'X':
        points = points + 1
        print("I threw: rock, added 1 point")
    elif my_action == 'Y':
        points = points + 2
        print("I threw: paper, added 2 points")
    elif my_action == 'Z':
        points = points + 3
        print("I threw: scissors, added 3 points")

    if line.rstrip() in win:
        points = points + 6
        print("I threw: {}, and opponent threw: {}, so I won. Points: {}".format(my_action, their_action, points))
    elif line.rstrip() in draw:
        points = points + 3
        print("I threw: {}, and opponent threw: {}, so I drew. Points: {}".format(my_action, their_action, points))
    else:
        print("I threw: {}, and opponent threw: {}, so I lost. Points: {}".format(my_action, their_action, points))

# a = rock, b = paper, c = scissor
# 1         2          3

f = '../data/day2.txt'

data = read_file(f)

points = 0
for line in data:
    their_action = line.split(' ')[0].rstrip()
    result = line.split(' ')[1].rstrip()

    if result == 'X':
        print('Result is a loss')
        if their_action == 'A':
            print('Opponent threw threw rock, so I threw scissor to lose')
            points = points + 3
        elif their_action == 'B':
            print('Opponent threw threw paper, so I threw rock to lose')
            points = points + 1
        elif their_action == 'C':
            print('Opponent threw threw scissor, so I threw scissor to lose')
            points = points + 2
    elif result == 'Y':
        print('Result is a draw')
        points = points + 3
        if their_action == 'A':
            print('Opponent threw threw rock, so I threw rock to draw')
            points = points + 1
        elif their_action == 'B':
            print('Opponent threw threw paper, so I threw paper to draw')
            points = points + 2
        elif their_action == 'C':
            print('Opponent threw threw scissor, so I threw scissor to draw')
            points = points + 3
    elif result == 'Z':
        print('Result is a win')
        points = points + 6
        if their_action == 'A':
            print('Opponent threw threw rock, so I threw paper to win')
            points = points + 2
        elif their_action == 'B':
            print('Opponent threw threw paper, so I threw scissor to win')
            points = points + 3
        elif their_action == 'C':
            print('Opponent threw threw scissor, so I threw rock to win')
            points = points + 1

print("Total points: {}".format(points))
