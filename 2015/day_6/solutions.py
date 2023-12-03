import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    # [("instruction", (x_1, y_1), (x_2, y_2)), ...]
    cleaned_data = []
    for line in data:
        start, coord_2 = line.split(" through ")
        *instruction, coord_1 = start.split()
        coord_1 = tuple(map(int, coord_1.strip().split(",")))
        coord_2 = tuple(map(int, coord_2.strip().split(",")))
        cleaned_data.append(("_".join(instruction), coord_1, coord_2))

    return cleaned_data


def solution_1(data):
    # simulate lights in the off position
    all_lights = {
        (x, y): False
        for x in range(1000)
        for y in range(1000)
    }

    def modify_range(instructions):
        action, top_left, bottom_right = instructions

        start_row = top_left[0]
        start_column = top_left[1]
        end_row = bottom_right[0]
        end_column = bottom_right[1]

        coords_to_modify = [
            (x, y)
            for x in range(start_row, end_row+1)
            for y in range(start_column, end_column+1)
        ]

        if action == "turn_on":
            for coord in coords_to_modify:
                all_lights[coord] = True
        elif action == "turn_off":
            for coord in coords_to_modify:
                all_lights[coord] = False
        elif action == "toggle":
            for coord in coords_to_modify:
                all_lights[coord] = not all_lights[coord]

    for instructions in data:
        modify_range(instructions)

    ans = sum(all_lights.values())
    print("Solution 1:", ans)


def solution_2(data):
    # simulate lights in the off position
    all_lights = {
        (x, y): 0
        for x in range(1000)
        for y in range(1000)
    }

    def modify_range(instructions):
        action, top_left, bottom_right = instructions

        start_row = top_left[0]
        start_column = top_left[1]
        end_row = bottom_right[0]
        end_column = bottom_right[1]

        coords_to_modify = [
            (x, y)
            for x in range(start_row, end_row+1)
            for y in range(start_column, end_column+1)
        ]

        if action == "turn_on":
            for coord in coords_to_modify:
                all_lights[coord] += 1
        elif action == "turn_off":
            for coord in coords_to_modify:
                all_lights[coord] = max(all_lights[coord]-1, 0)
        elif action == "toggle":
            for coord in coords_to_modify:
                all_lights[coord] += 2

    for instructions in data:
        modify_range(instructions)

    ans = sum(all_lights.values())
    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

