m,n = map(int, input().split())

def fib_sum(n):
    a=0
    b=1
    sum=0
    for i in range(n):
        a,b = b**2%10, (a+b)**2%10
        sum = (sum+a)%10
    return sum

def fib(n):
    a=0
    b=1
    for i in range(n):
        a,b = a%10, a+b%10
    return a

def fib_partial(m,n):
    if m==n:
        return fib(n)
    else:
        m_fib = fib_sum(m-1)
        n_fib = fib_sum(n)
        return (n_fib - m_fib)%10

print(fib_partial(m,n))