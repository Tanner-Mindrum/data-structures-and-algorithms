# A function that implements square root
def square_root():

    n = abs(float(input("Enter an integer: ")))

    i = 1
    while True:
        if i * i >= int(n): # Returns largest possible value as square root
            return i
        i += 1


def smallest_num(sorted_array):

    m = int(input("Enter number greater than or equal to 0: "))
    while m < 0:
        m = int(input("Enter number greater than or equal to 0: "))

    # Returns the first number that does not match i
    for i in range(len(sorted_array)):
        if sorted_array[i] != i:
            return i
    return sorted_array[len(sorted_array) - 1] + 1


print(square_root())
print(smallest_num([0, 1, 2, 3, 4]))
