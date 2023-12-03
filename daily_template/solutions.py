import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    return data


def solution_1(data):
    print("Solution 1:", "SOLUTION_GOES_HERE")


def solution_2(data):
    print("Solution 2:", "SOLUTION_GOES_HERE")


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

