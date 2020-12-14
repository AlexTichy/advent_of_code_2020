import re


def a(filename):
    bagmap = {}
    reg_line = re.compile(" bags? contain | bags?, | bags?.\n")
    reg_inner = re.compile("(\d) (.+)")

    with open(filename) as f:
        for line in f:
            parts = re.split(reg_line, line)[:-1]
            if "no other" in parts[1]:
                continue
            for p in parts[1:]:
                m = reg_inner.match(p)
                inner = m.group(2)
                if not inner in bagmap:
                    bagmap[inner] = []
                bagmap[inner].append(parts[0])
    print(bagmap)

    s = ["shiny gold"]
    while True:
        print(s)
        new_s = []
        if(len(s) > 1):
            new_s.extend(s)

        for colour in s:
            print(colour)
            if colour in bagmap:
                new_s.extend(bagmap[colour])

        new_s = set(new_s)
        if len(new_s) == len(s):
            break
        s = new_s

    print(s)
    print(len(s))



def b(filename):
    bagmap = {}
    reg_line = re.compile(" bags? contain | bags?, | bags?.\n")
    reg_inner = re.compile("(\d) (.+)")

    with open(filename) as f:
        for line in f:
            parts = re.split(reg_line, line)[:-1]
            outer = parts[0]
            if "no other" in parts[1]:
                continue
            if not outer in bagmap:
                bagmap[outer] = []
            for p in parts[1:]:
                m = reg_inner.match(p)
                number = m.group(1)
                inner = m.group(2)
                bagmap[outer].append((inner, int(number)))
    print(bagmap)

    bags = ["shiny gold"]
    total = 0
    while bags:
        next_level = []
        for b in bags:
            if not b in bagmap:
                continue
            inner = bagmap[b]
            for colour in inner:
                total += colour[1]
                for i in range(colour[1]):
                    next_level.append(colour[0])
        bags = next_level
        print(bags)
        print(total)



b("input_07.txt")
