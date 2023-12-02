
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_solution(lines):
    _sum = 0
    for index, line in enumerate(lines):
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        colom_index = line.find(':')
        game_showdowns = line[colom_index+2:].split(';')
        for showdown in game_showdowns:
            for color_info in showdown.split(','):
                number, color = color_info.split()
                min_cubes[color] = max(min_cubes[color], int(number))
        _sum += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
    return _sum

if __name__ == '__main__':
    lines = read_input('input.txt')
    print(find_solution(lines))