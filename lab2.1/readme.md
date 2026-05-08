# Activity 2.1 – Recurrence Experimentation and Analysis

**Course:** CS 5329 – Algorithm Design and Analysis  
**Student Name:** Raja Brahmendra Veerepalli  
**Semester:** Spring 2026

---

## Overview
This assignment compares a naive recursive Fibonacci implementation with a dynamic
programming approach to observe differences in runtime behavior and algorithm efficiency.

---

## How to Run the Program
From the repository directory, run:

```bash
python assignment2_fibonacci.py



Sample Output
n=10: fib_recursive -> 55 (time 0.0001s), fib_dp -> 55 (time 0.0000s)
n=20: fib_recursive -> 6765 (time 0.0013s), fib_dp -> 6765 (time 0.0000s)
n=30: fib_recursive -> 832040 (time 0.1400s), fib_dp -> 832040 (time 0.0001s)
n=35: fib_recursive -> 9227465 (time 1.5000s), fib_dp -> 9227465 (time 0.0001s)
n=50: fib_dp time 0.0001s
n=100: fib_dp time 0.0001s
n=500: fib_dp time 0.0002s
n=1000: fib_dp time 0.0003s

## Analysis Questions

a. Why does `fib_recursive` slow down as n increases?

    The recursive approach repeatedly recomputes the same Fibonacci values. This causes the
    number of function calls to grow exponentially as n increases.

b. What is the Big-O time complexity of each approach?
    - `fib_recursive`: Exponential time, approximately O(φⁿ)  
    - `fib_dp`: Linear time, O(n)

c. Would `fib_recursive(50)` be feasible to run?
    No. The exponential growth in recursive calls would result in an extremely long runtime,
    making it impractical to execute.

d. How does dynamic programming change the recurrence behavior?
    Dynamic programming ensures that each Fibonacci value is computed only once and reused,
    which reduces the growth from exponential to linear.
