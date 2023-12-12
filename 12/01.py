import sys
from copy import copy
sys.setrecursionlimit(20000)


def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']


def matches_sequence(fields, fragment, start_index):
    if start_index + fragment - 1 < len(fields):
        if '.' in fields[start_index : start_index + fragment]:
            return False
        return start_index + fragment >= len(fields) or \
        fields[start_index + fragment] != '#'
    return False


def possible_combinations(fields, fragments):
    def rek(field_index, frag_index):
        if frag_index == len(fragments):
            if '#' in fields[field_index:]:
                return 0
            return 1
        if field_index >= len(fields):
            return 0
        fragment = fragments[frag_index]
        result_positive = rek(field_index + fragment + 1, frag_index + 1) if matches_sequence(fields, fragment, field_index) else 0
        result_negative = rek(field_index + 1, frag_index) if fields[field_index] != '#' else 0
        return result_positive + result_negative

    return rek(0, 0)

def main():
    input_file = 'input.txt'
    lines = read_input(input_file)

    result = 0

    for line in lines:
        fields, numbers_str = line.split()
        numbers = [int(num) for num in numbers_str.split(',')]
        result += possible_combinations(fields, numbers)
    
    print(result)

if __name__ == '__main__':
    main()