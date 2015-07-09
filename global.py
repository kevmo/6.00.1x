def test_global():
    global num_calls
    num_calls = 0
    test()


def test():
    global num_calls
    for i in range(10):
        num_calls += 1

    print num_calls


if __name__ == '__main__':
    test_global()
