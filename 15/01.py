def read_input(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def hash(str):
    val = 0
    for char in str:
        val = ((val + ord(char)) * 17) % 256
    return val

if __name__ == '__main__':
    data = read_input('input.txt')
    sequence = data[0].split(',')
    result = sum([hash(str) for str in sequence])
    print(result)
    
    

