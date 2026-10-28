# Merge sort, with a "key" function, a trace of the recursive calls, step counters, and timing.
# Run from the code/ folder:  python merge_sort.py

import random
import time

from insertion_sort import insertion_sort


def merge(a, b, key=lambda x: x):
    """a and b are sorted by key. Return a new sorted list with the items of both."""
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):   # <= : on equal keys take from a first (stable)
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])             # one of the lists is used up:
    result.extend(b[j:])             # copy the rest of the other one
    return result


def merge_sort(a, key=lambda x: x):
    """Return a new sorted list, like sorted(a, key=key)."""
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort(a[:mid], key)
    right = merge_sort(a[mid:], key)
    return merge(left, right, key)


def largest(a):
    """The largest item of a non-empty list: the larger of the largest items of the two halves."""
    if len(a) == 1:
        return a[0]
    mid = len(a) // 2
    return max(largest(a[:mid]), largest(a[mid:]))


def merge_sort_traced(a, depth=0):
    """merge_sort without key, printing each call and its result, indented by depth."""
    indent = "    " * depth
    print(f"{indent}merge_sort({a})")
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort_traced(a[:mid], depth + 1)
    right = merge_sort_traced(a[mid:], depth + 1)
    result = merge(left, right)
    print(f"{indent}-> merge({left}, {right}) = {result}")
    return result


def merge_sort_counted(a):
    """Return (sorted list, comparisons, items copied by merge)."""
    if len(a) <= 1:
        return a[:], 0, 0
    mid = len(a) // 2
    left, c1, m1 = merge_sort_counted(a[:mid])
    right, c2, m2 = merge_sort_counted(a[mid:])
    result = []
    comparisons = 0
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, c1 + c2 + comparisons, m1 + m2 + len(result)


def main():
    print(merge([1, 3, 5, 6], [2, 4, 7, 8]))
    print(largest([6, 5, 3, 1, 8, 7, 2, 4]))
    print()
    merge_sort_traced([6, 5, 3, 1, 8, 7, 2, 4])

    # Steps: items copied by merge (n log2 n when n is a power of 2) and comparisons
    print()
    print(f"{'n':>9} {'copied':>12} {'comparisons':>12} {'n(n-1)/4':>14}")
    for n in [8, 1024, 2**20]:
        data = random.sample(range(n), n)
        result, comparisons, copied = merge_sort_counted(data)
        assert result == sorted(data)
        print(f"{n:>9,} {copied:>12,} {comparisons:>12,} {n * (n - 1) // 4:>14,}")

    # Stable, and the same result as sorted()
    records = [(random.randrange(10), random.random()) for _ in range(1000)]
    assert merge_sort(records, key=lambda r: r[0]) == sorted(records, key=lambda r: r[0])
    print()
    print("same result as sorted(), including the order of equal keys")

    # Timing: doubling n
    print()
    print(f"{'n':>6} {'insertion sort':>16} {'merge sort':>12} {'sorted()':>10}")
    for n in [1000, 2000, 4000, 8000]:
        data = [random.random() for _ in range(n)]
        start = time.perf_counter()
        insertion_sort(data[:])
        t_insertion = time.perf_counter() - start
        start = time.perf_counter()
        merge_sort(data)
        t_merge = time.perf_counter() - start
        start = time.perf_counter()
        sorted(data)
        t_sorted = time.perf_counter() - start
        print(f"{n:>6} {t_insertion * 1000:>13.1f} ms {t_merge * 1000:>9.1f} ms {t_sorted * 1000:>7.2f} ms")


if __name__ == "__main__":
    main()
