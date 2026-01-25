import sys
import platform

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print("Hello, Algorithms!")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    fib_10 = fibonacci(10)
    print(f"The 10th Fibonacci number is: {fib_10}")
