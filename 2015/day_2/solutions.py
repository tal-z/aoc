import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    data = [list(map(int, line.strip().split("x"))) for line in data]
    return data


def paper_needed(dimensions):
    l, w, h = sorted(dimensions)
    surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    overlap = l * w
    return surface_area + overlap


def solution_1(data):
    ans = sum(paper_needed(dimensions) for dimensions in data)
    print("Solution 1:", ans)


def ribbon_needed(dimensions):
    l, w, h = sorted(dimensions)
    perimeter = (l*2) + (w*2)
    bow = l * w * h
    return perimeter + bow

def solution_2(data):
    ans = sum(ribbon_needed(dimensions) for dimensions in data)
    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

