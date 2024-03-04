import random


def quick_select(array, k):
    # Handle base cases
    if len(array) == 1:
        return array[0]
    elif k < 1 or k > len(array):
        raise ValueError("Invalid value for k")

    # Randomly select a pivot element
    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]

    # Partition the array around the pivot
    left, right = partition(array, pivot)

    # Determine the position of the k-th smallest element relative to the pivot
    left_len = len(left)
    if k <= left_len:
        return quick_select(left, k)
    elif k == left_len + 1:
        return pivot
    else:
        return quick_select(right, k - left_len - 1)


def partition(array, pivot):
    left, right = [], []
    for num in array:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
    return left, right
