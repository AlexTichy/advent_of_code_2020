import re


def a(filename):

    lines = []
    with open(filename) as f:
        lines = f.readlines()

    acc = 0
    pos = 0

    while True:
        cl = lines[pos]
        print("acc: ", acc)
        print("cl: ", cl)
        print()

        if cl == "read":
            break

        lines[pos] = "read"
        if cl.startswith("nop"):
            pos += 1
        elif cl.startswith("jmp"):
            pos += int(cl.split()[1])
        elif cl.startswith("acc"):
            acc += int(cl.split()[1])
            pos += 1

    print(acc)


def bx(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()

    print("len lines ", len(lines))
    goes_to = []

    for i in range(len(lines)):
        cl = lines[i]
        if cl.startswith("jmp"):
            jmp = int(cl.split()[1])
            if jmp < 0:
                goes_to.append(i+jmp)
            else:
                goes_to.append(None)
        else:
            goes_to.append(None)

        print("i: ", i, " goes to ", goes_to[i])

    goes_to.append(len(lines))

    for i in range(len(lines)-1, -1, -1):
        cl = lines[i]
        if cl.startswith("nop") or cl.startswith("acc"):
            goes_to[i] = goes_to[i+1]
        elif cl.startswith("jmp"):
            jmp = int(cl.split()[1])
            if jmp > 0:
                goes_to[i] = goes_to[i+jmp]

        print("i: ", i, " goes to ", goes_to[i])

    print(goes_to)

    acc = 0
    pos = 0

    while True:
        if pos == len(lines):
            break
        cl = lines[pos]
        print("cl: ", cl)
        print("goes to: ", goes_to[pos])
        print()

        if cl.startswith("nop"):
            jmp = int(cl.split()[1])
            if goes_to[pos+jmp] == len(lines):
                print("changed line ", pos, ": ", cl)
                pos += jmp
            else:
                pos += 1
        elif cl.startswith("jmp"):
            if goes_to[pos + 1] == len(lines):
                print("changed line ", pos, ": ", cl)
                pos += 1
            else:
                pos += int(cl.split()[1])
        elif cl.startswith("acc"):
            acc += int(cl.split()[1])
            pos += 1

    print(acc)

def loop(lines, pos, acc):

    print("changed line ", pos, ": >>>", lines[pos])
    while True:
        cl = lines[pos]
        # print("acc: ", acc)
        # print("cl: ", cl)
        # print()

        if(cl.startswith("read")):
            return None

        lines[pos] = "read"
        if cl.startswith("nop"):
            pos += 1
        elif cl.startswith("jmp"):
            pos += int(cl.split()[1])
        elif cl.startswith("acc"):
            acc += int(cl.split()[1])
            pos += 1

        if pos < 0 or pos > len(lines):
            return None

        if pos == len(lines):
            return acc

def b(filename):

    with open(filename) as f:
        lines = f.readlines()

    acc = 0
    pos = 0

    while True:

        cl = lines[pos]
        # print("acc: ", acc)
        # print("cl: ", cl)
        # print()

        if cl.startswith("nop"):
            lines_x = lines.copy()
            lines_x[pos] = lines_x[pos].replace("nop", "jmp")
            acc_x = loop(lines_x, pos, acc)
            if acc_x:
                acc = acc_x
                break

            lines[pos] = "read"
            pos += 1

        elif cl.startswith("jmp"):
            lines_x = lines.copy()
            lines_x[pos] = lines_x[pos].replace("jmp", "nop")
            acc_x = loop(lines_x, pos, acc)
            if acc_x:
                acc = acc_x
                break

            lines[pos] = "read"
            pos += int(cl.split()[1])

        elif cl.startswith("acc"):
            acc += int(cl.split()[1])
            lines[pos] = "read"
            pos += 1

        if pos == len(lines):
            break;

    print(acc)


b("input_08.txt")
