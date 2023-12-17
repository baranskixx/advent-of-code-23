from queue import PriorityQueue

INF = 1e9

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def read_input(path):
    data = []
    with open(path, 'r') as file:
        for line in file:
            data.append([int(digit) for digit in list(line.strip())])
    return data

def min_path(grid):
    H, W = len(grid), len(grid[0])

    def is_valid_height(height):
        return height >= 0 and height < H
    def is_valid_width(width):
        return width >= 0 and width < W 

    D = [[[[INF] * 3 for _ in range(4)] for _ in range(W)] for _ in range(H)]

    Q = PriorityQueue()
    Q.put((grid[0][1], (0, 1, 1, 0)))
    Q.put((grid[1][0], (1, 0, 2, 0)))

    while not Q.empty():
        dist, data = Q.get()
        y, x, dir_index, line_steps = data

        if D[y][x][dir_index][line_steps] <= dist:
            continue
        D[y][x][dir_index][line_steps] = dist

        # move straight
        if line_steps < 2:
            move_y, move_x = DIRS[dir_index]
            new_y, new_x = y + move_y, x + move_x
            if is_valid_height(new_y) and is_valid_width(new_x):
                new_dist = dist + grid[new_y][new_x]
                Q.put((new_dist, (new_y, new_x, dir_index, line_steps + 1)))
        
        # move left
        move_y, move_x = DIRS[dir_index-1]
        new_y, new_x = y + move_y, x + move_x
        if is_valid_height(new_y) and is_valid_width(new_x):
            new_dist = dist + grid[new_y][new_x]
            Q.put((new_dist, (new_y, new_x, (dir_index-1)%4, 0)))
        
        # move right
        move_y, move_x = DIRS[(dir_index+1) % 4]
        new_y, new_x = y + move_y, x + move_x
        if is_valid_height(new_y) and is_valid_width(new_x):
            new_dist = dist + grid[new_y][new_x]
            Q.put((new_dist, (new_y, new_x, (dir_index+1)%4, 0)))

    result = INF
    for dir_index in range(4):
        for line_index in range(3):
            result = min(result, D[H-1][W-1][dir_index][line_index])

    print(result)



if __name__ == '__main__':
    grid = read_input('input.txt')
    print(min_path(grid))
