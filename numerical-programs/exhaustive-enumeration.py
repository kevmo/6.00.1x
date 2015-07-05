from sys import argv


def estimate_cube(n):

    try:
        n = int(n)
    except Exception as e:
        return "Error: {}".format(e)

    guess = 1

    while guess**3 < n:
        guess = guess + 1

    return guess

if __name__ == "__main__":
    print estimate_cube(argv[1])
