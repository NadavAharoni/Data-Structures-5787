# Quicksort, with the Lomuto and Hoare partitions, a "key" function, a trace of the recursive calls,
# step counters, the worst case, and timing.
# Run from the code/ folder:  python quick_sort.py
#
# Half-open ranges, as in binary search: a function that gets (a, lo, hi) works on a[lo:hi].

import random
import sys
import time

from merge_sort import merge_sort


def partition_lomuto(a, lo, hi, key=lambda x: x):
    """Partition a[lo:hi] around the pivot a[hi - 1] (the last item).
    Afterwards: a[lo:p] <= pivot, a[p] is the pivot, a[p + 1:hi] > pivot. Return p."""
    pivot = key(a[hi - 1])
    i = lo                                   # a[lo:i] holds the items <= pivot found so far
    for j in range(lo, hi - 1):
        if key(a[j]) <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi - 1] = a[hi - 1], a[i]        # the pivot goes between the two parts
    return i


def partition_hoare(a, lo, hi, key=lambda x: x):
    """Partition a[lo:hi] around the pivot a[lo] (the first item), with two indexes that move towards each other.
    Afterwards: every item of a[lo:p + 1] <= pivot <= every item of a[p + 1:hi]. Return p.
    The pivot is not necessarily at a[p]."""
    pivot = key(a[lo])
    i = lo - 1
    j = hi
    while True:
        i += 1
        while key(a[i]) < pivot:             # from the left: find an item >= pivot
            i += 1
        j -= 1
        while key(a[j]) > pivot:             # from the right: find an item <= pivot
            j -= 1
        if i >= j:                           # the indexes met
            return j
        a[i], a[j] = a[j], a[i]


def quick_sort(a, lo=0, hi=None, key=lambda x: x):
    """Sort a[lo:hi] in place (Lomuto partition)."""
    if hi is None:
        hi = len(a)
    if hi - lo <= 1:                         # 0 or 1 items: already sorted
        return
    p = partition_lomuto(a, lo, hi, key)     # the pivot is now in its final place, a[p]
    quick_sort(a, lo, p, key)                # the items before it
    quick_sort(a, p + 1, hi, key)            # the items after it


def quick_sort_hoare(a, lo=0, hi=None, key=lambda x: x):
    """Sort a[lo:hi] in place (Hoare partition)."""
    if hi is None:
        hi = len(a)
    if hi - lo <= 1:
        return
    p = partition_hoare(a, lo, hi, key)
    quick_sort_hoare(a, lo, p + 1, key)      # a[lo:p + 1]: may contain the pivot
    quick_sort_hoare(a, p + 1, hi, key)


def quick_sort_random(a, lo=0, hi=None, key=lambda x: x):
    """Like quick_sort, with a random pivot: swap a random item to the end, then partition."""
    if hi is None:
        hi = len(a)
    if hi - lo <= 1:
        return
    r = random.randrange(lo, hi)
    a[r], a[hi - 1] = a[hi - 1], a[r]
    p = partition_lomuto(a, lo, hi, key)
    quick_sort_random(a, lo, p, key)
    quick_sort_random(a, p + 1, hi, key)


def quick_sort_traced(a, lo=0, hi=None, depth=0):
    """quick_sort without key, printing each call, the pivot, and the list after the partition."""
    if hi is None:
        hi = len(a)
    indent = "    " * depth
    if hi - lo <= 1:
        print(f"{indent}quick_sort({a[lo:hi]})")
        return
    print(f"{indent}quick_sort({a[lo:hi]}), pivot {a[hi - 1]}")
    p = partition_lomuto(a, lo, hi)
    print(f"{indent}-> {a[lo:p]} {a[p]} {a[p + 1:hi]}")
    quick_sort_traced(a, lo, p, depth + 1)
    quick_sort_traced(a, p + 1, hi, depth + 1)


def quick_sort_counted(a, lo=0, hi=None, depth=1):
    """quick_sort (Lomuto) that returns (comparisons, swaps, maximum recursion depth)."""
    if hi is None:
        hi = len(a)
    if hi - lo <= 1:
        return 0, 0, depth
    pivot = a[hi - 1]
    i = lo
    comparisons = swaps = 0
    for j in range(lo, hi - 1):
        comparisons += 1
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            swaps += 1
            i += 1
    a[i], a[hi - 1] = a[hi - 1], a[i]
    swaps += 1
    c1, s1, d1 = quick_sort_counted(a, lo, i, depth + 1)
    c2, s2, d2 = quick_sort_counted(a, i + 1, hi, depth + 1)
    return comparisons + c1 + c2, swaps + s1 + s2, max(d1, d2)


def main():
    a = [5, 6, 1, 8, 3, 7, 2, 4]
    p = partition_lomuto(a, 0, len(a))
    print(f"Lomuto: {a}, pivot at index {p}")
    a = [5, 6, 1, 8, 3, 7, 2, 4]
    p = partition_hoare(a, 0, len(a))
    print(f"Hoare:  {a}, parts {a[:p + 1]} and {a[p + 1:]}")
    print()
    quick_sort_traced([5, 6, 1, 8, 3, 7, 2, 4])

    # Steps: random input vs sorted input
    sys.setrecursionlimit(10_000)
    print()
    print(f"{'n':>6} {'input':>8} {'comparisons':>12} {'swaps':>10} {'depth':>6} {'n(n-1)/2':>10}")
    for n in [1000, 2000, 4000]:
        for name, data in [("random", random.sample(range(n), n)), ("sorted", list(range(n)))]:
            comparisons, swaps, depth = quick_sort_counted(data)
            assert data == sorted(data)
            print(f"{n:>6,} {name:>8} {comparisons:>12,} {swaps:>10,} {depth:>6,} {n * (n - 1) // 2:>10,}")

    # Not stable: equal keys may change their order
    records = [(random.randrange(10), k) for k in range(1000)]
    expected = sorted(records, key=lambda r: r[0])       # stable: equal keys keep their order
    quick_sort(records, key=lambda r: r[0])
    print()
    print("same order as sorted() for equal keys:", records == expected)
    small = [(1, "a"), (1, "b"), (0, "c")]
    quick_sort(small, key=lambda r: r[0])
    print("quick_sort([(1, 'a'), (1, 'b'), (0, 'c')], key=...) ->", small)

    # Timing
    print()
    print(f"{'n':>7} {'quick sort':>11} {'random pivot':>13} {'Hoare':>9} {'merge sort':>11} {'sorted()':>9}")
    for n in [10_000, 20_000, 40_000, 80_000]:
        data = [random.random() for _ in range(n)]
        times = []
        for sort in [quick_sort, quick_sort_random, quick_sort_hoare]:
            b = data[:]
            start = time.perf_counter()
            sort(b)
            times.append(time.perf_counter() - start)
            assert b == sorted(data)
        for sort in [merge_sort, sorted]:
            start = time.perf_counter()
            sort(data)
            times.append(time.perf_counter() - start)
        print(f"{n:>7,}" + "".join(f" {t * 1000:>{w}.1f} ms" for t, w in zip(times, [8, 10, 6, 8, 6])))


if __name__ == "__main__":
    main()
