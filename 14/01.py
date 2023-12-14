def read_input(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def move_rocks(grid):
    for y in range(1, len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                after_move_y = y - 1
                while after_move_y >= 0 and grid[after_move_y][x] == '.':
                    after_move_y -= 1
                after_move_y += 1
                if after_move_y != y:
                    grid[after_move_y][x] = 'O'
                    grid[y][x] = '.'
    return grid

def count_points(grid):
    points = 0

    for index, line in enumerate(grid):
        multiplier = len(grid) - index
        points += multiplier * line.count('O')

    return points


if __name__ == '__main__':
    grid = read_input('input.txt')
    grid = move_rocks(grid)
    print(count_points(grid))
