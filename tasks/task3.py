import time
import timeit

from tasks.task1 import QuickFind
from tasks.task2 import WeightedCompressedQuickUnion


def task3():
    test_task1()
    test_task2()


def test_task1():
    print("================")
    print("Task 1 - Quick Find")
    print("================")

    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"\nTesting with {size} elements:")

        init_time = timeit.timeit(lambda: QuickFind(size), number=1000)
        print(f"  Init time: {init_time:.6f}s (1000 iterations)")

        def union_test():
            qf = QuickFind(size)
            for i in range(0, (size - 1) // 2, 2):
                qf.union(i, i + 1)
            return qf

        union_time = timeit.timeit(union_test, number=100)
        print(f"  Union time: {union_time:.6f}s (100 iterations)")

        qf = QuickFind(size)
        for i in range(0, (size - 1) // 2, 2):
            qf.union(i, i + 1)

        def find_test():
            for i in range(0, (size - 1) // 2, 2):
                qf.find(i, i + 1)

        find_time = timeit.timeit(find_test, number=100)
        print(f"  Find time: {find_time:.6f}s (100 iterations)")

    print("================")


def test_task2():
    print("================")
    print("Task 2 - Quick Union with Path Compression")
    print("================")

    sizes = [100, 1_000, 10_000, 100_000, 1_000_000]

    for size in sizes:
        print(f"\nTesting with {size} elements:")

        init_time = timeit.timeit(
            lambda: WeightedCompressedQuickUnion(size), number=1000
        )
        print(f"  Init time: {init_time:.6f}s (1000 iterations)")

        def union_test():
            qu = WeightedCompressedQuickUnion(size)
            for i in range(0, (size - 1) // 2, 2):
                qu.union(i, i + 1)
            return qu

        union_time = timeit.timeit(union_test, number=100)
        print(f"  Union time: {union_time:.6f}s (100 iterations)")

        qu = WeightedCompressedQuickUnion(size)
        for i in range(0, (size - 1) // 2, 2):
            qu.union(i, i + 1)

        def find_test():
            for i in range(0, (size - 1) // 2, 2):
                qu.connected(i, i + 1)

        find_time = timeit.timeit(find_test, number=100)
        print(f"  Find time: {find_time:.6f}s (100 iterations)")

        qu = WeightedCompressedQuickUnion(size)
        for i in range(0, (size - 1) // 2, 2):
            qu.union(i, i + 1)

        start_time = time.time()
        for i in range(0, (size - 1) // 2, 2):
            qu.connected(i, i + 1)
        end_time = time.time()

        print(f"  Connected check time: {(end_time - start_time) * 1000:.3f}ms")
        print(f"  Number of components: {qu.count()}")

    print("================")
