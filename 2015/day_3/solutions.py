import os
from collections import defaultdict

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    return data[0]


def solution_1(data):

    x, y = 0, 0
    visited = defaultdict(lambda: 0)
    visited[x,y] += 1

    for direction in data:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        visited[x,y] += 1

    ans = len(visited)

    print("Solution 1:", ans)


def solution_2(data):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0

    visited = defaultdict(lambda: 0)
    visited[santa_x, santa_y] += 1

    for idx, direction in enumerate(data):
        if not idx % 2:
            x, y = santa_x, santa_y
        else:
            x, y = robo_x, robo_y

        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        elif direction == "v":
            y -= 1

        visited[x,y] += 1

        if not idx % 2:
            santa_x, santa_y = x, y
        else:
            robo_x, robo_y = x, y

    ans = len(visited)

    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

