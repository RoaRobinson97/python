#RECURSIVE
def binary_search_recursive(arr, low, high, x):

    if high >= low:
        mid = (high + low)

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)

        else:
            return binary_search_recursive(arr, mid + 1, high, x)

    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search_recursive(arr, 0, len(arr)-1, x)

if result !=-1:
    print('Element is present at index', str(result))
else:
    print("Element is not present in the array")

#ITERATIVE
def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low)

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

arr2 =[2,3,4,4,10]
x = 10
result2 = binary_search_iterative(arr2,x)

if result2 != -1:
    print("Element is present at index:", str(result2))
else:
    print("Element is not present in array")