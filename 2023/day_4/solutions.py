import os
from collections import defaultdict

BASE_DIR = str(os.path.dirname(__file__))


def read_input():
    filepath = BASE_DIR + f"/input.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data


def clean_input(data):
    cleaned_data = []
    for line in data:
        line = line.strip()
        card_id, numbers = line.split(": ")
        winners, my_numbers = numbers.split("|")
        winners = set(map(int, winners.split()))
        my_numbers = set(map(int, my_numbers.split()))
        cleaned_data.append((int(card_id[5:].strip()), winners, my_numbers))
    return cleaned_data


def solution_1(data):
    to_add = []
    for game in data:
        card_id, winners, my_numbers = game
        my_winners = my_numbers.intersection(winners)
        game_value = 2**(len(my_winners)-1) if my_winners else 0
        to_add.append(game_value)

    ans = sum(to_add)

    print("Solution 1:", ans)


def solution_2(data):
    card_counts = defaultdict(lambda: 0)
    #card_values = defaultdict(lambda: (set(), set()))

    # build data structures for keping track of the number of cards I've won as I go, and for the number of cards I win
    for game in data:
        card_id, winners, my_numbers = game
        card_counts[card_id] += 1
        #card_values[card_id][0].update(winners)
        #card_values[card_id][1].update(my_numbers)

    for game in data:
        card_id, winners, my_numbers = game
        my_winners = my_numbers.intersection(winners)
        winners_count = len(my_winners)

        for _ in range(card_counts[card_id]):
            for i in range(1, winners_count+1):
                add_to = card_id + i
                card_counts[add_to] += 1

    ans = sum(card_counts.values())

    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    solution_1(data)
    solution_2(data)

