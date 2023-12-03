import os
from collections import defaultdict


BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    cleaned_data = [list(line.strip()) for line in data]
    return cleaned_data


def check_perimeter_1(line_idx, start_idx, end_idx, matrix):
    """
    Given a line index, a start index, and an end index,
    checks a within the matrix around the defined range
    to see if there are any non-period, non-numeric characters.
    """
    top_line = {(line_idx - 1, x) for x in range(start_idx, end_idx+1)}
    bottom_line = {(line_idx + 1, x) for x in range(start_idx, end_idx+1)}
    left_side = {(y, start_idx-1) for y in range(line_idx-1, line_idx+2)}
    right_side = {(y, end_idx) for y in range(line_idx-1, line_idx+2)}

    perimeter_coords = set()
    if line_idx > 0:
        perimeter_coords.update(top_line)
    if line_idx < len(matrix)-1:
        perimeter_coords.update(bottom_line)
    if start_idx > 0:
        perimeter_coords.update(left_side)
    if end_idx < len(matrix[0])-1:
        perimeter_coords.update(right_side)

    perimeter_coords = [
        coord
        for coord in perimeter_coords
        # y coord
        if coord[0] >= 0
        if coord[0] <= len(matrix)-1
        # x coord
        if coord[1] >= 0
        if coord[1] <= len(matrix[0])-1
    ]

    for coord in perimeter_coords:
        y, x = coord
        char = matrix[y][x]
        if char == ".":
            continue
        elif char.isdigit():
            continue
        else:
            return True
    return False


def solution_1(data):
    part_numbers = []

    for line_idx, line in enumerate(data):
        # Parse number(s) from line, one by one
        number = ""
        end_of_number = False
        for idx, char in enumerate(line):
            if char.isdigit():
                if not number:
                    start_idx = idx
                number += char
                # end of line
                if idx == len(data[0]) - 1:
                    end_of_number = True
                    end_idx = idx
            elif number:
                end_of_number = True
                end_idx = idx

            # Process parsed number
            if end_of_number:
                should_count = check_perimeter_1(line_idx, start_idx, end_idx, data)
                if should_count:
                    part_numbers.append(int(number))
                number = ""
                end_of_number = False

    ans = sum(part_numbers)
    print("Solution 1:", ans)


def check_perimeter_2(line_idx, start_idx, end_idx, matrix):
    """
    Given a line index, a start index, and an end index,
    checks a within the matrix around the defined range
    to see if there are any non-period, non-numeric characters.
    """
    top_line = {(line_idx - 1, x) for x in range(start_idx, end_idx+1)}
    bottom_line = {(line_idx + 1, x) for x in range(start_idx, end_idx+1)}
    left_side = {(y, start_idx-1) for y in range(line_idx-1, line_idx+2)}
    right_side = {(y, end_idx) for y in range(line_idx-1, line_idx+2)}

    perimeter_coords = set()
    if line_idx > 0:
        perimeter_coords.update(top_line)
    if line_idx < len(matrix)-1:
        perimeter_coords.update(bottom_line)
    if start_idx > 0:
        perimeter_coords.update(left_side)
    if end_idx < len(matrix[0])-1:
        perimeter_coords.update(right_side)

    perimeter_coords = [
        coord
        for coord in perimeter_coords
        # y coord
        if coord[0] >= 0
        if coord[0] <= len(matrix)-1
        # x coord
        if coord[1] >= 0
        if coord[1] <= len(matrix[0])-1
    ]

    for coord in perimeter_coords:
        y, x = coord
        char = matrix[y][x]
        if char == "*":
            return True, coord
    return False, coord


def solution_2(data):
    potential_gears = defaultdict(list)

    for line_idx, line in enumerate(data):
        # Parse number(s) from line, one by one
        number = ""
        end_of_number = False
        for idx, char in enumerate(line):
            if char.isdigit():
                if not number:
                    start_idx = idx
                number += char
                # end of line
                if idx == len(data[0]) - 1:
                    end_idx = idx
                    end_of_number = True
            elif number:
                end_idx = idx
                end_of_number = True

            # Process parsed number
            if end_of_number:
                should_count, coord = check_perimeter_2(line_idx, start_idx, end_idx, data)
                if should_count:
                    potential_gears[coord].append(int(number))
                number = ""
                end_of_number = False

    gear_ratios = [
        gear[0] * gear[1]
        for gear in potential_gears.values()
        if len(gear) == 2
    ]
    ans = sum(gear_ratios)
    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

