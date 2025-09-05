import random
import timeit
from typing import List

from tasks.task4 import BruteForce3Sum
from tasks.task5 import ThreeSum
import matplotlib.pyplot as plt


def task6():
    sizes4, times4 = test_task4()
    sizes5, times5 = test_task5()

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot(sizes4, times4, marker="o", label="Brute Force 3Sum (O(n^3))")
    plt.plot(sizes5, times5, marker="o", label="Optimized 3Sum (O(n^2))")
    plt.xlabel("n (array size)")
    plt.ylabel("total time (s) over iterations")
    plt.title("3Sum Timing Comparison")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/3sum_timings.png")
    print("Saved plot to images/3sum_timings.png")


def test_task4() -> tuple[List[int], List[float]]:
    print("================")
    print("Task 4 - Brute Force 3 Sum")
    print("================")

    # Timing harness (O(n^3), keep small)
    sizes = [100, 200, 500, 800, 1000]
    iterations = 3
    rng = random.Random(42)

    results: List[float] = []
    for size in sizes:
        arr = [rng.randint(-1000, 1000) for _ in range(size)]
        t = timeit.timeit(
            lambda arr=arr: BruteForce3Sum(arr).find_triplets(),
            number=iterations,
        )
        print(f"n={size}: {t:.6f}s ({iterations} iterations)")
        results.append(t)

    return sizes, results


def test_task5() -> tuple[List[int], List[float]]:
    print("================")
    print("Task 5 - Three Sum")
    print("================")

    # Timing harness (O(n^2) typical)
    sizes = [100, 200, 500, 800, 1000]
    iterations = 3
    rng = random.Random(42)

    results: List[float] = []
    for size in sizes:
        arr = [rng.randint(-1000, 1000) for _ in range(size)]
        t = timeit.timeit(
            lambda arr=arr: ThreeSum(arr).find_triplets(),
            number=iterations,
        )
        print(f"n={size}: {t:.6f}s ({iterations} iterations)")
        results.append(t)

    return sizes, results
