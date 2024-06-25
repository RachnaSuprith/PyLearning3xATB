numbers = [1, 2, 3]


def do_something(num):
    numbers.append(4)
    numbers[0] = 100
    return numbers

l = do_something(numbers)
print(l)
