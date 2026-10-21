# How many times does each loop body run? Compare with the formulas.
# Run from the code/ folder:  python count_steps.py

import math


def num_divisions_to_1(n, k):
    """How many times must n be divided by k (integer division) until it reaches 1?"""
    if k <= 1:
        raise ValueError("k must be greater than 1")
    count = 0
    while n > 1:
        n = n // k
        count += 1
    return count


def nested(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count


print(f"{'n':>15} {'k':>3} {'divisions':>9} {'log_k(n)':>9}")
for n in [8, 10, 100, 1000, 1024, 10**6, 10**9]:
    print(f"{n:>15,} {2:>3} {num_divisions_to_1(n, 2):>9} {math.log2(n):>9.2f}")
for n in [1000, 10**6]:
    print(f"{n:>15,} {10:>3} {num_divisions_to_1(n, 10):>9} {math.log10(n):>9.2f}")

print()
print(f"{'n':>6} {'nested':>10} {'n(n-1)/2':>10}")
for n in [1, 2, 10, 100, 1000]:
    print(f"{n:>6} {nested(n):>10,} {n * (n - 1) // 2:>10,}")

print()
print(f"{'k':>3} {'1+2+...+2^k':>14} {'2^(k+1)-1':>12}")
for k in [0, 1, 2, 3, 10, 20]:
    print(f"{k:>3} {sum(2**i for i in range(k + 1)):>14,} {2**(k + 1) - 1:>12,}")
