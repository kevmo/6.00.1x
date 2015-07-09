from sys import argv


input = int(argv[1])


def fibo(n):
    """Returns the nth Fibonacci number"""
    if n == 2:
        print "HEY"

    if n == 1 or n == 2:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    print fibo(input)

