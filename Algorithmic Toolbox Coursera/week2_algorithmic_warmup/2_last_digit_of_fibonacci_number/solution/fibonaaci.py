def fib(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n
    else:
        fib_list = [0] * (n+1)
        fib_list[0] = 0
        fib_list[1] = 1
        for i in range(2, n+1):
            fib_list[i] = (fib_list[i-2] + fib_list[i-1]) % 10
        return fib_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fib(input_n))