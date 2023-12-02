
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def is_showdown_valid(showdown):
    for color_info in showdown.split(','):
        number, color = color_info.split()
        if max_cubes[color] < int(number):
            return False
    return True

def find_sum_of_games(lines):
    _sum = 0
    for index, line in enumerate(lines):
        colom_index = line.find(':')
        game_showdowns = line[colom_index+2:].split(';')
        for showdown in game_showdowns:
            if not is_showdown_valid(showdown):
                break
        else:
            game_id = index + 1
            _sum += game_id
    return _sum

if __name__ == '__main__':
    lines = read_input('input.txt')
    print(find_sum_of_games(lines))