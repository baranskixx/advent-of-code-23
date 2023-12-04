def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_points_for_line(line):
    winning_str = line[line.find(':') + 2 : line.find('|') - 1]
    numbers_str = line[line.find('|') + 2 : ]
    winning_numbers = {int(number_str) for number_str in winning_str.split()}
    numbers = {int(num_str) for num_str in numbers_str.split()}

    wins = len(winning_numbers & numbers)
    return 0 if wins == 0 else 2 ** (wins - 1)

if __name__ == '__main__':
    lines = read_input('input.txt')
    total_points = sum([get_points_for_line(line) for line in lines])
    print(total_points)
