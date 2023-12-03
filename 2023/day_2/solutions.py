import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    cleaned_data = {}
    for line in data:
        game_id, rounds = line.split(":")
        game_id = int(game_id[5:])
        cleaned_data[game_id] = []
        for round in rounds.split(";"):
            selection_dict = {}
            selections = round.split(",")
            for selection in selections:
                count, key = selection.split()
                selection_dict[key] = int(count)
            cleaned_data[game_id].append(selection_dict)

    return cleaned_data


def solution_1(data):
    max_allowed = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    valid_game_ids = []

    for game_id, rounds in data.items():
        game_is_valid = True
        for round in rounds:
            for color, count in round.items():
                if count > max_allowed[color]:
                    game_is_valid = False
                    break
        if game_is_valid:
            valid_game_ids.append(game_id)

    ans = sum(valid_game_ids)
    print("Solution 1:", ans)


def solution_2(data):
    game_powers = []
    for game_id, rounds in data.items():
        min_required_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for round in rounds:
            for color, count in round.items():
                min_required = max(count, min_required_cubes[color])
                min_required_cubes[color] = min_required

        min_required_cubes = list(min_required_cubes.values())
        game_power = min_required_cubes.pop()
        while min_required_cubes:
            game_power *= min_required_cubes.pop()

        game_powers.append(game_power)

    ans = sum(game_powers)

    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

