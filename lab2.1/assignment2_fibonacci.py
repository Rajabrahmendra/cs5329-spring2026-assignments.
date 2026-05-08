import time

def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_dp(n):
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    test_values = [10, 20, 30, 35]

    for n in test_values:
        start = time.time()
        r1 = fib_recursive(n)
        t1 = time.time() - start

        start = time.time()
        r2 = fib_dp(n)
        t2 = time.time() - start

        print(
            f"n={n}: fib_recursive -> {r1} (time {t1:.4f}s), "
            f"fib_dp -> {r2} (time {t2:.6f}s)"
        )

    # Large values (DP only)
    for n in [50, 100, 500, 1000]:
        start = time.time()
        fib_dp(n)
        t = time.time() - start
        print(f"n={n}: fib_dp time {t:.6f}s")
