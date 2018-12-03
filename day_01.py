import sys
from itertools import cycle

def part_one(freqs):
    print(sum(freqs))

def part_two(freqs):
    total = 0
    seen = set()

    for freq in cycle(freqs):
        total += freq
        if total in seen:
            print(total)
            return
        seen.add(total)

if __name__ == '__main__':

    freqs = [(1 if line[0] == '+' else -1) * int(line[1:]) 
                for line in open('input/input_01.txt').readlines()]
    part_one(freqs)
    part_two(freqs)
