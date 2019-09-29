def gcd(a,b):
    assert 0<=a<=2*10**9 and 0<=b<=2*10**9

    if b == 0:
        return a
    else:
        aprime = a % b
        return gcd(b, aprime)

if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))