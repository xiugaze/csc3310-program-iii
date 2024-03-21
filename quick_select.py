import random

def quick_select(array, k):
    # Handle base cases
    if len(array) == 1:
        return array[0]
    elif k < 1 or k > len(array):
        raise ValueError("Invalid value for k")

    # Randomly select a pivot element
    pivot_index = random.randint(0, len(array) - 1)
    # pivot_index = 0
    pivot = array[pivot_index]

    # Partition the array around the pivot
    left, same, right = partition(array, pivot)

    # Determine the position of the k-th smallest element relative to the pivot
    if k <= len(left):
        return quick_select(left, k)
    elif k == len(left) + 1:
        return pivot
    else:
        return quick_select(right, k - len(left) - len(same))


def partition(array, pivot):
    left, same, right = [], [], []
    for num in array:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            same.append(num)
    return left, same, right
