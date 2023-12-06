def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

if __name__ == '__main__':
    lines = read_input('input.txt')

    times = [int(time) for time in lines[0][len('Time:'):].split()]
    distance = [int(dist) for dist in lines[1][len('Distance:'):].split()]
    
    n = len(times)
    possible_ways = 1

    for i in range(n):
        time = times[i]
        wins = 0
        for loading_time in range(time+1):
            result = loading_time * (time-loading_time)
            if result > distance[i]:
                wins += 1
        possible_ways *= wins
    
    print(possible_ways)
    

