import re

from collections import defaultdict

def part_one(grid):
    count = 0
    for row in grid:
        for num in grid[row]:
            if grid[row][num] > 1:
                count += 1
    print(count)

def part_two(claims,grid):

    for [id, start_x, start_y, width, height] in claims:
        overlap = False
        for x in range(start_x,start_x+width):
            for y in range(start_y,start_y+height):
                if grid[x][y] != 1:
                    overlap = True
                    continue
        if not overlap:
            print(id,'does not overlap!')
            return

# claims are of the form: [id, x, y, width, height]
if __name__ == '__main__':
    claims = [list(map(int,re.findall('\d+',line))) for line in open('input/input_03.txt').readlines()]

    grid = defaultdict(lambda: defaultdict(int))

    for [id, start_x, start_y, width, height] in claims:
        for x in range(start_x,start_x+width):
            for y in range(start_y,start_y+height):
                grid[x][y] += 1

    part_one(grid)
    part_two(claims,grid)
