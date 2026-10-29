import random
import time
import matplotlib.pyplot as plt


def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons, shifts


sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

sorted_times = []
reverse_times = []
random_times = []


for n in sizes:

    sorted_data = list(range(n))

    reverse_data = list(range(n, 0, -1))

    random_data = random.sample(range(n * 2), n)


    start = time.perf_counter()

    comparisons, shifts = insertion_sort(sorted_data)

    end = time.perf_counter()

    sorted_time = end - start
    sorted_times.append(sorted_time)

    print("\nN =", n)
    print("Sorted")
    print("Time:", round(sorted_time, 6))
    print("Comparisons:", comparisons)
    print("Shifts:", shifts)


    start = time.perf_counter()

    comparisons, shifts = insertion_sort(reverse_data)

    end = time.perf_counter()

    reverse_time = end - start
    reverse_times.append(reverse_time)

    print("Reverse")
    print("Time:", round(reverse_time, 6))
    print("Comparisons:", comparisons)
    print("Shifts:", shifts)


    start = time.perf_counter()

    comparisons, shifts = insertion_sort(random_data)

    end = time.perf_counter()

    random_time = end - start
    random_times.append(random_time)

    print("Random")
    print("Time:", round(random_time, 6))
    print("Comparisons:", comparisons)
    print("Shifts:", shifts)



plt.plot(sizes, sorted_times, marker="o", label="Sorted")
plt.plot(sizes, reverse_times, marker="o", label="Reverse")
plt.plot(sizes, random_times, marker="o", label="Random")

plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (seconds)")

plt.title("Insertion Sort - Empirical Analysis")

plt.legend()
plt.grid()

plt.show()