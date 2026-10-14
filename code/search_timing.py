# Timing: "in" on a list (linear) vs binary search (bisect) vs "in" on a set.
# Run from the code/ folder:  python search_timing.py

import bisect
import random
import time

n = 1_000_000
numbers = sorted(random.sample(range(10 * n), n))
as_set = set(numbers)
targets = [random.randrange(10 * n) for _ in range(100)]


def time_it(name, search):
    start = time.perf_counter()
    found = sum(1 for t in targets if search(t))
    elapsed = time.perf_counter() - start
    print(f"{name:<22} {elapsed / len(targets) * 1e6:12.2f} microseconds per search  (found {found})")


def binary_in(t):
    i = bisect.bisect_left(numbers, t)
    return i < len(numbers) and numbers[i] == t


print(f"n = {n:,}, {len(targets)} searches")
time_it("t in list", lambda t: t in numbers)
time_it("binary search (bisect)", binary_in)
time_it("t in set", lambda t: t in as_set)
