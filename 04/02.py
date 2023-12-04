def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_points_for_line(line):
    winning_str = line[line.find(':') + 2 : line.find('|') - 1]
    numbers_str = line[line.find('|') + 2 : ]
    winning_numbers = {int(number_str) for number_str in winning_str.split()}
    numbers = {int(num_str) for num_str in numbers_str.split()}

    return len(winning_numbers & numbers)

if __name__ == '__main__':
    lines = read_input('input.txt')
    copies = [1 for _ in range(len(lines))]

    for index, line in enumerate(lines):
        points = get_points_for_line(line)
        if points != 0:
            for x in range(index + 1, min(len(copies), index + points + 1)):
                copies[x] += copies[index]
    print(copies)
    print(sum(copies))