import timeit
import matplotlib.pyplot as plt

from tasks.task1 import QuickFind
from tasks.task2 import WeightedCompressedQuickUnion


def task3():
    sizes = [100, 500, 1000, 5000, 10000]
    print("================")
    print("Task 3 - Union-Find timing comparison")
    print("================")
    print(f"Sizes: {sizes}")
    qf_init, qf_union, qf_find = measure_quickfind(sizes)
    wcu_init, wcu_union, wcu_find = measure_quickunion(sizes)

    fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

    axes[0].plot(sizes, qf_init, marker="o", label="QuickFind (1000 it)")
    axes[0].plot(sizes, wcu_init, marker="o", label="WCU (1000 it)")
    axes[0].set_ylabel("init time (s)")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    axes[1].plot(sizes, qf_union, marker="o", label="QuickFind (100 it)")
    axes[1].plot(sizes, wcu_union, marker="o", label="WCU (100 it)")
    axes[1].set_ylabel("union time (s)")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(sizes, qf_find, marker="o", label="QuickFind (100 it)")
    axes[2].plot(sizes, wcu_find, marker="o", label="WCU (100 it)")
    axes[2].set_xlabel("n (elements)")
    axes[2].set_ylabel("find/connected time (s)")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle("Union-Find Timings: QuickFind vs Weighted Compressed Quick Union")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig("images/task3_comparison.png")
    print("Saved plot to images/task3_comparison.png")
    plt.close(fig)


def measure_quickfind(sizes: list[int]) -> tuple[list[float], list[float], list[float]]:
    init_times: list[float] = []
    union_times: list[float] = []
    find_times: list[float] = []

    for size in sizes:
        init_time = timeit.timeit(lambda: QuickFind(size), number=1000)
        init_times.append(init_time)

        def union_test():
            qf = QuickFind(size)
            for i in range(0, (size - 1) // 2, 2):
                qf.union(i, i + 1)
            return qf

        union_time = timeit.timeit(union_test, number=100)
        union_times.append(union_time)

        qf = QuickFind(size)
        for i in range(0, (size - 1) // 2, 2):
            qf.union(i, i + 1)

        def find_test():
            for i in range(0, (size - 1) // 2, 2):
                qf.find(i, i + 1)

        find_time = timeit.timeit(find_test, number=100)
        find_times.append(find_time)

    return init_times, union_times, find_times


def measure_quickunion(
    sizes: list[int],
) -> tuple[list[float], list[float], list[float]]:
    init_times: list[float] = []
    union_times: list[float] = []
    find_times: list[float] = []

    for size in sizes:
        init_time = timeit.timeit(
            lambda: WeightedCompressedQuickUnion(size), number=1000
        )
        init_times.append(init_time)

        def union_test():
            qu = WeightedCompressedQuickUnion(size)
            for i in range(0, (size - 1) // 2, 2):
                qu.union(i, i + 1)
            return qu

        union_time = timeit.timeit(union_test, number=100)
        union_times.append(union_time)

        qu = WeightedCompressedQuickUnion(size)
        for i in range(0, (size - 1) // 2, 2):
            qu.union(i, i + 1)

        def find_test():
            for i in range(0, (size - 1) // 2, 2):
                qu.connected(i, i + 1)

        find_time = timeit.timeit(find_test, number=100)
        find_times.append(find_time)

    return init_times, union_times, find_times
