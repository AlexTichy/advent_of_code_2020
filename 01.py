f = open("input.txt", "r")
numbers = [int(x) for x in f.readlines()]
print(numbers)

def first_task():
    for n in numbers:
        if (2020-n) in numbers:
            print(n, " * ", 20-n, " = ", n*(2000-n))
            break

def second_task():
    for i in range(len(numbers)):
        first = numbers[i]
        for second in numbers[i+1:]:
            if (2020 - first - second) in numbers[i+2:]:
                third = (2020 - first - second)
                print(first, " * ", second, " * ", third, " = ", first*second*third)
                break

second_task()

