from sys import argv

user_range = int(argv[1])

def demo_range(num):
    for i in range(num):
        print i

def print_all_evens(num):
    """Print all even numbers between 0 and num."""
    for i in range(2, num, 2):
        print i

def count_down(num):
    """Count down from num to 0."""
    for i in range(num, -1, -1):
        print i


if __name__ == '__main__':
    demo_range(user_range)
    # print_all_evens(user_range)
    # count_down(user_range)
