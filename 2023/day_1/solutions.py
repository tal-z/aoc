import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    data = [line.strip() for line in data]
    return data


def solution_1(data):
    to_add = []
    for entry in data:
        numbers = [char for char in entry if char.isdigit()]
        int_str = numbers[0] + numbers[-1]
        to_add.append(int(int_str))

    print("Solution 1:", sum(to_add))


def word_to_num(word):
    substitutions = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    word = list(word)
    new_word = []
    while word:
        found = False
        if word[0].isdigit():
            char = word.pop(0)
            new_word.append(char)
        else:
            for k, v in substitutions.items():
                if "".join(word).startswith(k):
                    word.pop(0)
                    new_word.append(v)
                    found = True
                    break
            if not found:
                word.pop(0)

    return "".join(new_word)


def solution_2(data):
    to_add = []

    for entry in data:
        entry = word_to_num(entry)
        numbers = [char for char in entry if char.isdigit()]
        int_str = numbers[0] + numbers[-1]
        to_add.append(int(int_str))

    print("Solution 2:", sum(to_add))


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)
