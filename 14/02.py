import itertools

def read_input(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def makegrid(data):
    return [list(row) for row in data.splitlines()]

def tilt_n(grid):
    for x in range(W):
        dy = 0
        for y in range(H):
            c = grid[y][x]
            if c == '.':
                dy += 1
            elif c == '#':
                dy = 0
            elif c == 'O':
                grid[y][x] = '.'
                grid[y-dy][x] = 'O'

def tilt_s(grid):
    for x in range(W):
        dy = 0
        for y in range(H-1,-1,-1):
            c = grid[y][x]
            if c == '.':
                dy += 1
            elif c == '#':
                dy = 0
            elif c == 'O':
                grid[y][x] = '.'
                grid[y+dy][x] = 'O'

def tilt_w(grid):
    for y in range(H):
        dx = 0
        for x in range(W):
            c = grid[y][x]
            if c == '.':
                dx += 1
            elif c == '#':
                dx = 0
            elif c == 'O':
                grid[y][x] = '.'
                grid[y][x-dx] = 'O'

def tilt_e(grid):
    for y in range(H):
        dx = 0
        for x in range(W-1,-1,-1):
            c = grid[y][x]
            if c == '.':
                dx += 1
            elif c == '#':
                dx = 0
            elif c == 'O':
                grid[y][x] = '.'
                grid[y][x+dx] = 'O'

def weight(grid):
    return sum((H-y)*row.count('O') for y,row in enumerate(grid))

def get_hash(grid):
    return hash(tuple([''.join(row) for row in grid]))

if __name__ == '__main__':
    grid = read_input('input.txt')
    H = len(grid)
    W = len(grid[0])
    seen = [0]
    scores = [0]
    want = -1
    for i in itertools.count():
        tilt_n(grid)
        tilt_w(grid)
        tilt_s(grid)
        tilt_e(grid)
        cur = get_hash(grid)
        scores.append(weight(grid))
        if cur in seen:
            break
        seen.append(cur)
    pat0 = seen.index(cur)
    cycle = len(seen) - pat0
    want =  (1000000000 - pat0) % cycle + pat0
    print(scores[want])
