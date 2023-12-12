import sys
from copy import copy
from functools import lru_cache
sys.setrecursionlimit(20000)

def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

transform = lambda t: (t[0]-1,) + t[1:]
@lru_cache(maxsize=None)
def count_possibilities(row, numbers, flag):
    if not numbers:
        return 0 if '#' in row else 1
    elif not row:
        return 0 if sum(numbers) else 1
    elif numbers[0] == 0:
        return count_possibilities(row[1:], numbers[1:], False) if row[0] != '#' else 0
    elif flag:
        return count_possibilities(row[1:], transform(numbers), True) if row[0] != '.' else 0
    elif row[0] == '#':
        return count_possibilities(row[1:], transform(numbers), True)
    elif row[0] == '.':
        return count_possibilities(row[1:], numbers, False)
    return count_possibilities(row[1:], numbers, False) + \
            count_possibilities(row[1:], transform(numbers), True)
    
def main():
    input_file = 'input.txt'
    lines = read_input(input_file)

    result = 0
    for line in lines:
        fields, numbers_str = line.split()
        numbers = [int(num) for num in numbers_str.split(',')] * 5
        org_fields = copy(fields)
        for _ in range(4):
            fields += '?' + org_fields
        result += count_possibilities(fields, tuple(numbers), False)
        print(result)
    print(result)

if __name__ == '__main__':
    main()