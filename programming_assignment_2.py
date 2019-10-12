import math


# A function that implements square root by modifying binary search
def square_root():
    N = abs(float(input("Enter an integer: ")))

    start = 0
    end = int(N)
    mid = 0

    while start <= end:
        mid = math.ceil((start + end) / 2)
        if mid * mid == int(N):
            return mid
        elif mid * mid > N:
            end = mid - 1
        else:
            start = mid + 1
    return mid


# Finds the smallest missing number in a given sorted array
def smallest_num(a):

    m = int(input("Enter number greater than or equal to 0: "))
    while m < 0:
        m = int(input("Enter number greater than or equal to 0: "))

    start = 0
    end = len(a) - 1
    mid = 0

    while start <= end:
        mid = (start + end) // 2
        if mid != a[mid] and start == a[start]:
            return mid
        elif mid != a[mid] and start != a[start]:
            end = mid - 1
        else:
            start = mid + 1

    if mid == a[len(a) - 1]:
        return mid + 1

    return 0


print(square_root())
print(smallest_num([0,1,3,6,8,9]))
