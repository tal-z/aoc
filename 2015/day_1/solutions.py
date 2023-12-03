import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    return data[0]


def solution_1(data):
    from collections import Counter

    counts = Counter(data)
    ans = counts["("] - counts[")"]
    print("Solution 1:", ans)


def solution_2(data):
    floor = 0
    ans = None
    for idx, char in enumerate(data):
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            ans = idx + 1
            break


    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

