from collections import Counter
from itertools import combinations

def part_one(ids):
    twice_count = 0
    thrice_count = 0

    for id in ids:
        counts = Counter(id)
        if any(counts[c] == 2 for c in counts):
            twice_count += 1
        if any(counts[c] == 3 for c in counts):
            thrice_count += 1
    print(twice_count * thrice_count)

def part_two(ids):
    for (a, b) in combinations(ids,2):
        diffs = sum([1 if a[i] != b[i] else 0 for i in range(len(a))])
        if diffs == 1:
            print(''.join([a[i] if a[i] == b[i] else '' for i in range(len(a))]))
            return



if __name__ == '__main__':
    ids = [line.strip() for line in open('input/input_02.txt').readlines()]
    part_one(ids)
    part_two(ids)
