import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    cleaned_data = [line.strip().split(" -> ") for line in data]
    return cleaned_data


def solution_1(data):
    replacements = {
        "AND": "&",
        "OR": "|",
        "LSHIFT": "<<",
        "RSHIFT": ">>",
        "NOT": "~",
        "is": "_is",
        "as": "_as",
        "if": "_if",
        "in": "_in",
    }
    ready_to_execute = []

    for instruction in data:
        signal, connect_to = instruction

        for find, replace in replacements.items():
            connect_to = connect_to.replace(find, replace)
            signal = signal.replace(find, replace)

        ready_to_execute.append((signal, connect_to))

    for instruction in ready_to_execute:
        operation, variable = instruction
        try:
            exec(f"{variable} = {operation}")
        except NameError:
            ready_to_execute.append(instruction)

    exec("print('Solution 1:', a)")



def solution_2(data):
    replacements = {
        "AND": "&",
        "OR": "|",
        "LSHIFT": "<<",
        "RSHIFT": ">>",
        "NOT": "~",
        "is": "_is",
        "as": "_as",
        "if": "_if",
        "in": "_in",
    }
    ready_to_execute = []

    for instruction in data:
        signal, connect_to = instruction

        for find, replace in replacements.items():
            connect_to = connect_to.replace(find, replace)
            signal = signal.replace(find, replace)
        if connect_to == "b":
            signal = 956
        ready_to_execute.append((signal, connect_to))

    for instruction in ready_to_execute:
        operation, variable = instruction
        try:
            exec(f"{variable} = {operation}")
        except NameError:
            ready_to_execute.append(instruction)

    exec("print('Solution 2:', a)")

if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

