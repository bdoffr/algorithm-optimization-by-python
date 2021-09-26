import time


def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 缓存
cache = {0: 0, 1: 1}
def fibonacci2(n):
    if n in cache:
        return cache[n]
    return fibonacci2(n - 1) + fibonacci2(n - 2)


# 递归
class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


# 迭代
def fibonacci3(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


if __name__ == "__main__":
    start_time = time.time()
    fibonacci_list = [fibonacci(_) for _ in range(11)]

    # TODO fibonacci_list = [fibonacci3(_) for _ in range(11)]

    # TODO fibonacci_list = [Fibonacci()(_) for _ in range(51)]

    # FIXME fibonacci_list = [fibonacci3(_) for _ in range(51)]

    end_time = time.time()
    time_delta = end_time - start_time
    print(f"运行时间:{time_delta}, 结果:{fibonacci_list}")
