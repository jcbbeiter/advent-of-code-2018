import sys

def part_one():

    result = 0

    with open('input/input_01.txt') as f:
        for line in f.readlines():
            sign = 1 if line[0] == '+' else -1
            result += sign*int(line[1:])

    print(result)

def part_two():
    total = 0
    seen = set()

    lines = open('input/input_01.txt').readlines()
    while True:
        for line in lines:
            sign = 1 if line[0] == '+' else -1
            total += sign*int(line[1:])
            if total in seen:
                print(total)
                return
            seen.add(total)

if __name__ == '__main__':
    part_one()
    part_two()
