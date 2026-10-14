# Insertion sort, with a "key" function, comparison and shift counters, and timing.
# Run from the code/ folder:  python insertion_sort.py

import random
import time

from random_tuples import create_random_tuples


def insertion_sort(a, key=lambda x: x):
    """Sort a in place by key. Stable: items with equal keys keep their order."""
    for i in range(1, len(a)):
        item = a[i]          # a[0:i] is sorted; insert a[i] into it
        j = i - 1
        while j >= 0 and key(a[j]) > key(item):
            a[j + 1] = a[j]  # shift a larger item one place to the right
            j -= 1
        a[j + 1] = item


def insertion_sort_counted(a, key=lambda x: x):
    """Same as insertion_sort, but return (comparisons, shifts)."""
    comparisons = 0
    shifts = 0
    for i in range(1, len(a)):
        item = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key(a[j]) <= key(item):
                break
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = item
    return comparisons, shifts


def main():
    # Trace: the list after each step of the outer loop
    a = [5, 2, 4, 6, 1, 3]
    print("start", a)
    for i in range(1, len(a)):
        item = a[i]
        j = i - 1
        while j >= 0 and a[j] > item:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = item
        print(f"i = {i}  ", a)

    # Comparisons and shifts: sorted, reversed and random input
    print()
    print(f"{'n':>6} {'input':>8} {'comparisons':>12} {'shifts':>10}")
    for n in [10, 100, 1000]:
        for name, data in [("sorted", list(range(n))),
                           ("reversed", list(range(n, 0, -1))),
                           ("random", random.sample(range(n), n))]:
            comparisons, shifts = insertion_sort_counted(data)
            print(f"{n:>6} {name:>8} {comparisons:>12,} {shifts:>10,}")

    # Sort tuples by key, and check against Python's sorted (also stable)
    a = create_random_tuples(1000, 2, [int, str])
    a = [(x % 10, s) for x, s in a]      # many equal keys
    expected = sorted(a, key=lambda x: x[0])
    insertion_sort(a, key=lambda x: x[0])
    assert a == expected
    print()
    print("same result as sorted(), including the order of equal keys")

    # Timing: doubling n
    print()
    print(f"{'n':>6} {'insertion sort':>16} {'sorted()':>12}")
    for n in [1000, 2000, 4000, 8000]:
        data = [random.random() for _ in range(n)]
        start = time.perf_counter()
        insertion_sort(data[:])
        t_insertion = time.perf_counter() - start
        start = time.perf_counter()
        sorted(data)
        t_sorted = time.perf_counter() - start
        print(f"{n:>6} {t_insertion * 1000:>13.1f} ms {t_sorted * 1000:>9.2f} ms")


if __name__ == "__main__":
    main()
