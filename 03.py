import re



def a(filename, down, right):
    f = open(filename, "r")
    lines = f.readlines()
    width = len(lines[0]) -1
    tree_count = 0
    horizontal_pos = 0
    vertical_pos = 0
    for l in lines:
        if(vertical_pos % down) is not 0:
            vertical_pos += 1
            continue
        if l[horizontal_pos % width] is '#':
            tree_count += 1
        horizontal_pos += right
        vertical_pos += 1
    print(tree_count)
    return tree_count

def b(filename):
    _a = a(filename, 1, 1)
    _b = a(filename, 1, 3)
    _c = a(filename, 1, 5)
    _d = a(filename, 1, 7)
    _e = a(filename, 2, 1)
    res = _a * _b * _c * _d * _e
    print(res)

b("input_03.txt")

