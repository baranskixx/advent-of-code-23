from copy import copy

def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines() if line != '\n']

if __name__ == '__main__':
    lines = read_input('input.txt')
    seeds = [int(number) for number in lines[0][7:].split()]
    seeds_left = copy(seeds)
    next_gen_seeds = []
    for line in lines[2:]:
        if line.endswith(':') or line.endswith('-'):
            seeds = copy(next_gen_seeds) + copy(seeds_left)
            seeds_left = copy(seeds)
            next_gen_seeds = []
        else:
            dest_start, src_start, _range = [int(num) for num in line.split()]
            for seed in seeds:
                if seed >= src_start and seed < src_start + _range and seed in seeds_left:
                    next_gen_seeds.append(dest_start + seed - src_start)
                    seeds_left.remove(seed)
    
    print(min(seeds))
                    
