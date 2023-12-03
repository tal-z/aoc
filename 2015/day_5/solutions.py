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


def is_nice_1(string):
    vowel_counts = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }
    bad_substrings = {"ab", "cd", "pq", "xy"}
    two_in_a_row = False
    for i in range(len(string)-1):
        char, next_char = string[i:i+2]
        if char+next_char in bad_substrings:
            return 0
        if char in vowel_counts:
            vowel_counts[char] += 1
        if char == next_char:
            two_in_a_row = True
    if string[-1] in vowel_counts:
        vowel_counts[string[-1]] += 1
    has_three_vowels = sum(vowel_counts.values()) >= 3
    if two_in_a_row and has_three_vowels:
        return 1
    return 0




def solution_1(data):
    ans = sum(is_nice_1(string) for string in data)
    print("Solution 1:", ans)


def is_nice_2(string):
    # contains a pair of any two letters that appears at least twice in the string without overlapping
    # check pairs:
    has_dupe_pair = False
    seen_pairs = {}
    for i in range(0, len(string)-1):
        pair = string[i:i+2]
        if (pair in seen_pairs):
            if (i-seen_pairs[pair]) > 1:
                has_dupe_pair = True
                break
        else:
            seen_pairs[pair] = i

    # same ends of 3-substring
    # check triplets
    has_trip = False
    for i in range(len(string)-2):
        front, middle, back = string[i:i+3]
        if front == back:
            has_trip = True
            break

    return has_dupe_pair and has_trip

def solution_2(data):
    ans = sum(is_nice_2(string) for string in data)
    print("Solution 2:", ans)


if __name__ == "__main__":
    data = clean_input(read_input())
    #solution_1(data)
    solution_2(data)

