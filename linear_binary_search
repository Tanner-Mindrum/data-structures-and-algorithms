import random
import timeit
import math


# Function gets user input to set length of array and creates list of sorted random integers
def create_list():
    a = []

    n = int(input("Enter a positive integer: "))
    while n <= 0:
        n = int(input("Enter a positive integer: "))

    # Add n amount of random integers to list
    for i in range(n):
        a.append(random.randrange(-1000, 1000))

    # Return sorted array using built-in sorting method
    a.sort()
    return a


# Search for a given value, key, using linear search
def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return a.index(a[i])
    return -1


# Search for a given value, key, using binary search
def binary_search(a, key):
    start = 0
    end = len(a) - 1
    while True:
        midpoint = (start + end) // 2
        if a[midpoint] == key:
            return a.index(a[midpoint])
        elif key > a[midpoint]:
            start = midpoint + 1
        elif key < a[midpoint]:
            end = midpoint - 1
        if start > end:
            return -1


def main():
    # Part A
    a = create_list()
    linear_time = 0
    binary_time = 0
    num_reps = 100
    for i in range(num_reps):
        # Pick a random number in a
        key = random.choice(a)

        # Perform linear search and time execution time
        linear_start_time = timeit.default_timer()
        linear_search(a, key)
        linear_time += timeit.default_timer() - linear_start_time

        # Perform binary search and time execution time
        binary_start_time = timeit.default_timer()
        binary_search(a, key)
        binary_time += timeit.default_timer() - binary_start_time

    print("Average linear search runtime: ", linear_time / num_reps)
    print("Average binary search runtime: ", binary_time / num_reps, "\n")

    # Part B
    a = create_list()
    key = 5000

    # Perform one linear search and time execution time
    linear_start_time = timeit.default_timer()
    linear_search(a, key)
    linear_time = timeit.default_timer() - linear_start_time
    print("Worst-case linear search runtime: ", linear_time)

    # Perform one binary search and time execution time
    binary_start_time = timeit.default_timer()
    binary_search(a, key)
    binary_time = timeit.default_timer() - binary_start_time
    print("Worst-case binary search runtime: ", binary_time, "\n")

    # Calculation of how long it takes to one run line of binary search where n = 10**5
    one_line = timeit.default_timer() / (10 * math.log(100000, 2) + 2)
    print("Time to run one single line using binary search (n = 10^5): ", one_line)

    # Calculation of how approximately long it will take to run binary and linear search when n = 10**9
    estimation_binary = one_line * (10 * math.log(1000000000, 2) + 2)
    print("Estimated time to run binary search (n = 10^9): ", estimation_binary)

    estimation_linear = one_line * (4 * math.log(1000000000, 2))
    print("Estimated time to run linear search (n = 10^9): ", estimation_linear)


main()
