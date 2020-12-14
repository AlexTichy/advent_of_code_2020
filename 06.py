import re


def a(filename):
    sum = 0;
    group_questions = []
    with open(filename) as f:
        for line in f:
            if line is "\n":
                sum += len(set(group_questions))
                print(len(set(group_questions)), "\n")
                group_questions = []
                continue;

            print(line[:-1])
            for i in range(len(line) - 1):
                group_questions.append(line[i])

        sum += len(set(group_questions))

    print(sum)


def b(filename):
    s = 0
    group_questions = []
    first = True
    with open(filename) as f:
        for line in f:
            if line is "\n":
                s += len(group_questions)
                print(group_questions)
                print(len(group_questions))
                print(s, "\n")
                group_questions = []
                first = True
                continue

            print(line[:-1])

            new = []
            for i in range(len(line) - 1):
                new.append(line[i])

            if first:
                group_questions = set(new)
                first = False
            else:
                group_questions = set.intersection(set(group_questions), set(new))

    s += len(group_questions)
    print(len(group_questions), "\n")

    print(s)


b("input_06.txt")
