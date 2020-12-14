import re

def a(filename):
    max = 0;
    max_t = "";
    with open(filename) as f:
        for ticket in f:
            n = int(ticket[:-1].replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)
            if n > max:
                max = n
                max_t = ticket
    print(max)
    print(max_t)

def b(filename):
    l = []
    with open(filename) as f:
        for ticket in f:
            n = int(ticket[:-1].replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)
            l.append(n)
    l.sort()
    for i in range(len(l)-1):
        print(l[i])
        if l[i+1] != l[i]+1:
            print("XXX ", l[i+1], "  ", l[i]+1)
        print("\n")


b("input_05.txt")

