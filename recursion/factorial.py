from sys import argv


input = int(argv[1])


def recursive_factorial(num):
    """Assumes num is a positive integer.

    Returns factorial result of that number.
    """
    if num > 1:
        return num * recursive_factorial(num - 1)

    return num


def iterative_factorial(num):
    """Assumes num is a positive integer.

    Returns factorial result of that number.
    """
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

if __name__ == '__main__':
    print recursive_factorial(input)
    print iterative_factorial(input)
