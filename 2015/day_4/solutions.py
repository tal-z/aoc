from hashlib import md5
import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    return data[0]


def hex_digest(data):
    return md5(data.encode()).hexdigest()


def solution_1(data):

    prefix = data
    suffix = 0
    ans = None

    while not ans:
        result = hex_digest(prefix + str(suffix))
        if result.startswith("00000"):
            ans = prefix + str(suffix)
        suffix += 1

    print("Solution 1:", ans)


def solution_2(data):
    prefix = data
    suffix = 0
    ans = None

    while not ans:
        result = hex_digest(prefix + str(suffix))
        if result.startswith("000000"):
            ans = prefix + str(suffix)
        suffix += 1

    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

