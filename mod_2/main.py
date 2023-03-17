
def fibonacci_r(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n - 1) + fibonacci_r(n - 2)


def fibonacci_i(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f1 = 0
        f2 = 1
        for _ in range(n):
            m = f1 + f2
            f1 = f2
            f2 = m
        return f1


def run_example():
    print(fibonacci_r(10))
    print(fibonacci_i(10))


if __name__ == "__main__":
    run_example()
