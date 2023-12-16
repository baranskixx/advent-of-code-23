from queue import Queue

DIRS = ['RIGHT', 'LEFT', 'UP', 'DOWN']

DIR_TO_VECTOR = {
    'RIGHT': (0, 1),
    'LEFT': (0, -1),
    'UP': (-1, 0),
    'DOWN': (1, 0)
}

DIR_AND_MIRROR_TO_DIRS = {
    ('RIGHT', '/'): ['UP'],
    ('RIGHT', '\\'): ['DOWN'],
    ('RIGHT', '|'): ['UP', 'DOWN'],
    ('RIGHT', '-'): ['RIGHT'],
    ('LEFT', '/'): ['DOWN'],
    ('LEFT', '\\'): ['UP'],
    ('LEFT', '|'): ['UP', 'DOWN'],
    ('LEFT', '-'): ['LEFT'],
    ('UP', '/'): ['RIGHT'],
    ('UP', '\\'): ['LEFT'],
    ('UP', '-'): ['LEFT', 'RIGHT'],
    ('UP', '|'): ['UP'],
    ('DOWN', '-'): ['LEFT', 'RIGHT'],
    ('DOWN', '/'): ['LEFT'],
    ('DOWN', '\\'): ['RIGHT'],
    ('DOWN', '|'): ['DOWN'],
}

def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]    

def bfs(grid):
    H, W = len(grid), len(grid[0])
    Q = Queue()
    V = [[False] * W for _ in range(H)]
    V_dir = [[[False] * 4 for _ in range(W)] for _ in range(H)]
    Q.put((0, 0, 'RIGHT'))

    while not Q.empty():
        y, x, curr_dir = Q.get()
        print(y, x)
        if y < 0 or y >= H or x < 0 or x >= W or V_dir[y][x][DIRS.index(curr_dir)]:
            continue
        V[y][x] = True
        V_dir[y][x][DIRS.index(curr_dir)] = True
        if grid[y][x] == '.':
            vec_y, vec_x = DIR_TO_VECTOR[curr_dir]
            Q.put((y + vec_y, x + vec_x, curr_dir))
        else:
            next_dirs = DIR_AND_MIRROR_TO_DIRS[(curr_dir, grid[y][x])]
            for dir in next_dirs:
                vec_y, vec_x = DIR_TO_VECTOR[dir]
                Q.put((y + vec_y, x + vec_x, dir))
    for row in V:
        print(str(['#' if elem else '.' for elem in row]))
    return V



if __name__ == '__main__':
    grid = read_input('input.txt')
    V = bfs(grid)
    result = sum([list(row).count(True) for row in V])
    print(result)