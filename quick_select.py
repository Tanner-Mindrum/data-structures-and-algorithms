import random


def find_kth(part_a_or_b):
    # Input validation for positive integer
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n >= 0:
                break
        except ValueError:
            pass
        print("Not a valid input. Try again.")

    # Generate array of size n with random nums in range -100 to 100
    a = []
    for i in range(n):
        a.append(random.randrange(-100, 101))
    print(a)

    a = [-16, 33, 20, 59, 53, -17, 43]

    # Input validation for number in correct range
    while True:
        try:
            k = int(input("Enter a number between 1 to n: "))
            if k in range(1, n + 1):
                break
        except ValueError:
            pass
        print("Not a valid input. Try again.")

    # Call quick_select to find and print the kth least element
    quick_select(a, k, part_a_or_b)


def quick_select(a, k, part_a_or_b):
    # Call partition helper function to partition array a
    tail = partition(a, part_a_or_b)
    #print("array:", a)

    if part_a_or_b:
        if tail + 1 == k:  # Found the kth least element
            print(a[tail])
        elif tail + 1 < k:  # Select the lower bound array
            k -= len(a[: tail + 1])
            quick_select(a[tail + 1:], k, part_a_or_b)
        else:  # Select the upper bound array
            quick_select(a[:tail], k, part_a_or_b)

    else:
        print(tail, k)
        if len(a) != 1:
            if tail < k:
                print(a[tail-1:])
                k -= len(a[tail:]) + 1
                # print("kupdate",k)
                # print(a)
                quick_select(a[:tail - 1], k, part_a_or_b)
            elif tail > k:
                # print(a)
                # print(a[-k:])
                quick_select(a[tail+1:], k, part_a_or_b)
            elif tail == k:
                #print("in")
                if k > 0:
                    #print(a)
                    print(a[len(a) - k:])
        else:
            print(a)


def partition(a, part_a_or_b):
    # Pivot is the median of the first, middle, and last values in array a
    pivot = 0
    if len(a) != 0:
        if len(a) >= 3:
            pivot = [a[0], a[(0 + (len(a) - 1)) // 2], a[len(a) - 1]]
            pivot.sort()
            pivot = pivot[1]
        else:
            #print(a)
            a.sort()
            pivot = a[len(a) - 1]

        # Push pivot to end of array, swap with element at last position in array
        if len(a) > 1:
            a[a.index(pivot)] = a[len(a) - 1]
            a[len(a) - 1] = pivot

        tail = 0
        j = 0
        while j != len(a) - 1:  # Iterate until j reaches 2nd to last position
            if a[j] < pivot:  # Swap element if it's less than the pivot
                temp = a[j]
                a[j] = a[tail]
                a[tail] = temp
                tail += 1  # Move tail
            j += 1  # Iterate scanner

        # Final swap that swaps pivot and the tail
        temp = a[len(a) - 1]
        a[len(a) - 1] = a[tail]
        a[tail] = temp

        # Return index of pivot after being swapped back
        return tail


# print("-------------------")
# print("Find kth smallest:")
# print("-------------------")
# find_kth(True)
print("\n-------------------")
print("Find kth max")
print("-------------------")
find_kth(False)
