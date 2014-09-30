"""
Approximate Pattern Matching Problem
"""

def main(pattern, text, d):
    inds = []
    for i, p in patterns_in_text(list(text), pattern):
        if approx_match(p, pattern, d):
            inds.append(i)
    print(' '.join(map(str,inds)))


def patterns_in_text(text, init_pattern):
    i = 0
    while len(text) >= len(init_pattern):
        yield i, ''.join(text[0:len(init_pattern)])
        text.pop(0)
        i += 1


def approx_match(text, pattern, d):
    d_counter = 0
    for i, char in enumerate(text):
        if char == pattern[i]:
            pass
        else:
            d_counter += 1
            if d_counter > d:
                return False
    return True


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
        d = int(f.readline().strip())
    main(pattern, text, d)
