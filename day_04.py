import re
from collections import defaultdict

if __name__ == '__main__':
    entries = [[re.match('\[.*\]',line).group(0),' '.join(line.strip().split(' ')[2:])] for line in open('input/input_04.txt').readlines()]
    entries.sort()
    guards = defaultdict(list)

    i = 0
    guard_num = -1
    asleep = -1
    while i < len(entries):
        if entries[i][1] == 'falls asleep':
            asleep = int(entries[i][0][-3:-1])
        elif entries[i][1] == 'wakes up':
            awake = int(entries[i][0][-3:-1])
            guards[guard_num].append([asleep,awake])
        else:
            guard_num = int(re.findall('\d+',entries[i][1])[0])
        i = i+1

    total_time_asleep = []
    for g in guards:
        total_time_asleep.append([g,sum([shift[1] - shift[0] for shift in guards[g]])])
    total_time_asleep.sort(key=lambda x: x[1])
    guard_slept_most = total_time_asleep[-1][0]

    minutes = [0] * 60
    for [asleep,awake] in guards[guard_slept_most]:
        for m in range(asleep,awake):
            minutes[m] += 1
    sleepy_minute = minutes.index(max(minutes))

    print(guard_slept_most,"guard slept most, most frequent minute was",sleepy_minute,end="")
    print("; answer is",guard_slept_most*sleepy_minute)


    # 2

    # id, minute, frequency
    guard_high_scores = []

    for g in guards:
        minutes = [0] * 60
        for [asleep,awake] in guards[g]:
            for m in range(asleep,awake):
                minutes[m] += 1
        most_minute = minutes.index(max(minutes))
        guard_high_scores.append([g,most_minute,max(minutes)])
    guard_high_scores.sort(key=lambda x: x[2])


    guard, minute, freq = guard_high_scores[-1]

    print("guard",guard,"was asleep during minute",minute,freq,"times",end="")
    print("; answer is",guard*minute)
