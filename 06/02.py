def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

if __name__ == '__main__':
    lines = read_input('input.txt')

    times = [time for time in lines[0][len('Time:'):].split()]
    distance = [dist for dist in lines[1][len('Distance:'):].split()]

    total_time = ''
    for t in times:
        total_time += t
    total_time = int(total_time)

    total_dist = ''
    for d in distance:
        total_dist += d
    total_dist = int(total_dist)
    print(total_time)
    print(total_dist)

    possible_ways = 0
    for loading_time in range(total_time+1):
        result = loading_time * (total_time - loading_time)
        if result > total_dist:
            possible_ways += 1
    
    print(possible_ways)
                