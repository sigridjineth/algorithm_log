def gcd(a,b):
    assert 0<=a<=2*10**9 and 0<=b<=2*10**9

    if b == 0:
        return a
    else:
        aprime = a % b
        return gcd(b, aprime)

def lcm(a,b):
    assert 0<=a<=2*10**9 and 0<=b<=2*10**9
    return a*b / gcd(a,b)

input_a, input_b = map(int, input().split())
print(lcm(input_a, input_b))