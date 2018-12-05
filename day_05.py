def react(p):
    reacted = []

    does_react = lambda a,b: (a.upper() == b.upper() and a != b)

    i = 0
    while i < len(p):
        if i != len(p)-1 and does_react(p[i],p[i+1]):
            i += 2
        else:
            if len(reacted) > 0 and does_react(p[i],reacted[-1]):
                reacted.pop()
            else:
                reacted.append(p[i])
            i += 1

    return ''.join(reacted)

def trimmed_polymers(p):
    for t in set(p.lower()):
        yield ''.join(ch for ch in p if ch.lower() != t)


if __name__ == '__main__':
    polymer = open('input/input_05.txt').read().strip()


    #1
    print(len(react(polymer)))

    #2
    print(min(len(react(p)) for p in trimmed_polymers(polymer)))
