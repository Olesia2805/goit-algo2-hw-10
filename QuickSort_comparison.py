import random
import time
import timeit
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


if __name__ == "__main__":
    N_10 = 10_000
    N_50 = 50_000
    N_100 = 100_000
    N_500 = 500_000

    sizes = [N_10, N_50, N_100, N_500]
    random_times = []
    deterministic_times = []
    for size in sizes:
        random_array = [random.randint(1, 1000) for _ in range(size)]
        print(f"Sorting array of size {size}")

        time_random_array = timeit.timeit(
            "randomized_quick_sort(random_array)", globals=globals(), number=5
        )
        print(f"  Randomized Quick Sort Time: {time_random_array:.6f} seconds")
        random_times.append(time_random_array)

        time_deterministic_array = timeit.timeit(
            "deterministic_quick_sort(random_array)", globals=globals(), number=5
        )
        print(
            f"  Deterministic Quick Sort Time: {time_deterministic_array:.6f} seconds"
        )
        deterministic_times.append(time_deterministic_array)
        print("----------------------------------------")

    plt.plot(sizes, random_times, label="Randomized Quick Sort")
    plt.plot(sizes, deterministic_times, label="Deterministic Quick Sort")
    plt.legend()
    plt.xlabel("Array Size (N)")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Quick Sort Algorithms")
    plt.show()
