# Linear search and binary search, with a "key" function and a step counter.
# Run from the code/ folder:  python search.py

import random


def linear_search(a, target, key=lambda x: x):
    """Return (index, steps) of the first item whose key equals target; index is None if not found."""
    steps = 0
    for i in range(len(a)):
        steps += 1
        if key(a[i]) == target:
            return i, steps
    return None, steps


def binary_search(a, target, key=lambda x: x):
    """a must be sorted by key. Return (index, steps); index is None if not found."""
    lo = 0           # first index that may still hold target
    hi = len(a)      # one past the last index that may still hold target
    steps = 0
    while lo < hi:
        steps += 1
        mid = (lo + hi) // 2
        k = key(a[mid])
        if k == target:
            return mid, steps
        if target < k:
            hi = mid         # target can only be left of mid
        else:
            lo = mid + 1     # target can only be right of mid
    return None, steps


def main():
    a = [3, 8, 12, 17, 21, 25, 30, 34, 41, 47, 52, 58, 63, 70, 77]
    for target in [41, 3, 77, 20]:
        print(f"target={target}  linear: {linear_search(a, target)}  binary: {binary_search(a, target)}")

    # Worst case number of steps as n grows
    print()
    print(f"{'n':>12} {'linear':>12} {'binary':>8}")
    for n in [10, 100, 1000, 10**6]:
        a = list(range(n))
        missing = -1           # smaller than all: the worst case for both searches
        print(f"{n:>12,} {linear_search(a, missing)[1]:>12,} {binary_search(a, missing)[1]:>8}")

    # Search by key: tuples (last name, first name, year), sorted by last name
    scientists = sorted([
        ("Curie", "Marie", 1898),
        ("Darwin", "Charles", 1859),
        ("Einstein", "Albert", 1905),
        ("Franklin", "Rosalind", 1952),
        ("Lovelace", "Ada", 1843),
        ("Newton", "Isaac", 1687),
    ], key=lambda s: s[0])
    i, steps = binary_search(scientists, "Lovelace", key=lambda s: s[0])
    print()
    print(f"Lovelace: {scientists[i]}, found in {steps} steps")

    # Check binary_search against linear_search on random data
    for _ in range(1000):
        a = sorted(random.randint(0, 50) for _ in range(random.randint(0, 30)))
        target = random.randint(-5, 55)
        i, _ = binary_search(a, target)
        assert (i is None) == (target not in a)
        assert i is None or a[i] == target
    print("random tests passed")


if __name__ == "__main__":
    main()
