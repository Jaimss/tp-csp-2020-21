from time import time


def timer(method):
    def timed(*args, **kwargs):
        ts = time()
        result = method(*args, **kwargs)
        te = time()

        return result, (te - ts)

    return timed


nums = [x for x in range(10000000)]


@timer
def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


@timer
def linear():
    for x in nums:
        if x == (10000000 - 1):
            return "returning linear"


x, y = linear()
print(x, y)

a, b = binary_search(nums, 0, len(nums) - 1, (10000000 - 1))
print(a, b)
