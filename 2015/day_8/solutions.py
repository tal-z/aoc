import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    cleaned_data = [line.strip() for line in data]
    return cleaned_data


def solution_1(data):
    code_character_count = sum(len(s) for s in data)

    evaluated = [eval(s) for s in data]
    string_literal_character_count = sum(len(s) for s in evaluated)

    ans = code_character_count - string_literal_character_count

    print("Solution 1:", ans)


def solution_2(data):
    code_character_count = sum(len(s) for s in data)

    encoded_counts = []
    doubled = {'"', '\\'}
    for s in data:
        char_count = 2  # simulate code quotes
        for char in s:
            if char in doubled:
                char_count += 2  # count double for non-escaped characters that should be escaped
            else:
                char_count += 1  # count everything else as one
        encoded_counts.append(char_count)

    re_encoded_string_character_count = sum(encoded_counts)
    ans = re_encoded_string_character_count - code_character_count
    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

