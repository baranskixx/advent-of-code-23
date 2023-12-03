def load_input(path):
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_all_stars(lines): 
    stars = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '*':
                stars.append((y, x))
    return stars

def find_number_end(line, num_start):
    num_end = num_start + 1
    while num_end < len(line) and line[num_end].isdigit():
        num_end += 1
    
    return num_end

def star_adjacent_to_number(star_y, star_x, number_y, number_from, number_to):
    return abs(star_y - number_y) <= 1 and star_x in range(number_from-1, number_to+1)

def add_to_stars_neighbours(stars_neighbours, number, num_y, num_from, num_to):
    for coords, numbers_list in stars_neighbours:
        star_y, star_x = coords
        if star_adjacent_to_number(star_y, star_x, num_y, num_from, num_to):
            numbers_list.append(number)
    return stars_neighbours

if __name__ == '__main__':
    lines = load_input('input.txt')
    stars = find_all_stars(lines)
    
    stars_neigh = []
    for coord in stars:
        stars_neigh.append([coord, list()])

    for y, line in enumerate(lines):
        x = 0 
        while x < len(line):
            if line[x].isdigit():
                _end = find_number_end(line, x)
                number = int(line[x : _end])
                stars_neigh = add_to_stars_neighbours(stars_neigh, number, y, x, _end)
                x = _end
            else:
                x += 1
    
    _sum = 0
    for coords, nums in stars_neigh:
        if len(nums) == 2:
            _sum += nums[0] * nums[1]
    
    print(_sum)


