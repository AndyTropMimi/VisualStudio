


def addNumbers(numbers):
    total = 0

    for n in numbers:
        total += n
        print(n, total)
    return total

print(addNumbers([1, 2, 3]))