import re

pattern = re.compile('(\d+)-(\d+) (\w): (\w+)')
f = open("input_02.txt", "r")

def a(f):
    count = 0
    for line in f.readlines():
        match = pattern.match(line)
        num = match.group(4).count(match.group(3))
        if num >= int(match.group(1)) and num <= int(match.group(2)):
            print(line, " num:", num)
            count += 1
    print(count)

def b(f):
    count = 0
    for line in f.readlines():
        match = pattern.match(line)
        pw = match.group(4)
        letter = match.group(3)
        one = int(match.group(1))-1
        two = int(match.group(2))-1

        if pw[one] is letter and pw[two] is not letter:
            print(line)
            count += 1
        elif pw[one] is not letter and pw[two] is letter:
            print(line)
            count += 1

    print(count)

b(f)

