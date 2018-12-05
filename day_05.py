def react_step(p):
    reacted = []

    last = '-'

    for ch in p:
        if last.upper() == ch.upper() and ch != last:
            last = '-'
        else:
            if last != '-':
                reacted.append(last)
            last = ch
    if p[-1] == p[-2]:
        reacted.pop()
    else:
        reacted.append(p[-1])
    return ''.join(reacted)

def react(p):
    p = list(p)
    last_len = -1
    while len(p) != last_len:
        last_len = len(p)
        p = react_step(p)
    return ''.join(p)

def trimmed_polymers(p):
    for t in set(p.lower()):
        yield ''.join(ch for ch in p if ch.lower() != t)


if __name__ == '__main__':
    polymer = open('input/input_05.txt').read().strip()


    #1
    print(len(react(polymer)))

    #2
    print(min(len(react(p)) for p in trimmed_polymers(polymer)))


