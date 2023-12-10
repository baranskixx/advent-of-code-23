import sys
from copy import copy
sys.setrecursionlimit(1000000)

NORTH_NEW_DIRECTION = {'|':'north', '7':'west', 'F': 'east'}
SOUTH_NEW_DIRECTION = {'|':'south', 'L': 'east', 'J':'west'}
WEST_NEW_DIRECTION  = {'-':'west', 'L':'north', 'F':'south'}
EAST_NEW_DIRECTION  = {'-':'east', 'J':'north', '7':'south'}
DIRECTIONS = {
            'north' : NORTH_NEW_DIRECTION,
            'south': SOUTH_NEW_DIRECTION,
            'east': EAST_NEW_DIRECTION,
            'west': WEST_NEW_DIRECTION
}
DIR_MOVE = {'north': (-1, 0), 'south': (1, 0), 'west': (0, -1), 'east': (0, 1)}
ON_LEFT_FROM = {'north': (0, -1), 'south': (0, 1), 'west': (1, 0), 'east': (-1, 0)}
ON_RIGHT_FROM = {'north': (0, 1), 'south': (0, -1), 'west': (-1, 0), 'east': (1, 0)}


def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']


def dfs(lines, path, V, y, x):
    if y not in range(0, len(lines)) or x not in range(0, len(lines[0])) or (y,x) in path or V[y][x]:
        return 0, V
    V[y][x] = True
    a, V = dfs(lines, path, copy(V), y-1, x)
    b, V = dfs(lines, path, copy(V), y, x-1)
    c, V = dfs(lines, path, copy(V), y+1, x)
    d, V = dfs(lines, path, copy(V), y, x+1)
    return sum([a,b,c,d]) + 1, V


if __name__ == '__main__':
    lines = read_input('input.txt')
    y = 0
    x = 0
    V = [[False] * len(lines[0]) for _ in range(len(lines))]
    for row_index, row in enumerate(lines):
        if 'S' in row:
            y = row_index
            x = row.index('S')
            break
    
    direction = 'south'
    path = []
    pos_y, pos_x = y, x
    while True:
        path.append((pos_y,pos_x, direction))
        V[pos_y][pos_x] = True
        move_y, move_x = DIR_MOVE[direction]
        pos_y, pos_x = pos_y + move_y, pos_x + move_x
        if pos_y == y and pos_x == x:
            break
        next_direction = DIRECTIONS[direction][lines[pos_y][pos_x]]
        direction = next_direction
    
    tiles = 0
    for index, path_elem in enumerate(path):
        pos_y, pos_x, direction = path_elem
        transfer_coords = ON_RIGHT_FROM[direction]
        transfer_y, transfer_x = transfer_coords
        right_x, right_y = pos_x + transfer_x, pos_y + transfer_y
        result, V = dfs(lines, [path_elem[0:2] for path_elem in path], V, right_y, right_x)
        tiles += result
        
        _, _, direction = path[index-1]
        transfer_coords = ON_RIGHT_FROM[direction]
        transfer_y, transfer_x = transfer_coords
        right_x, right_y = pos_x + transfer_x, pos_y + transfer_y
        result, V = dfs(lines, [path_elem[0:2] for path_elem in path], V, right_y, right_x)
        tiles += result
    
    print(tiles)

    
    


    

