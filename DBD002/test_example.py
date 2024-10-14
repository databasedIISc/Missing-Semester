def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def test_fibo():
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(10) == 55)
    assert(fibonacci(20) == 6765)

def test_gcd():
    assert(gcd(0, 1) == 1)
    assert(gcd(1, 0) == 1)
    assert(gcd(1, 1) == 1)
    assert(gcd(10, 5) == 5)
    assert(gcd(10, 3) == 1)
    assert(gcd(10, 0) == 10)
    assert(gcd(-10, -4) == 2)
    assert(gcd(10, 10) == 10)
    assert(gcd(-1, 1) == 1)
    assert(gcd(-1, -1) == 1)

