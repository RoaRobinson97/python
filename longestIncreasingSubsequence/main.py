global maximum

def _lis(arr, n):
    global maximum

    if n == 1:
        return 1

    maxEndingHere = 1

    for i in range(1,n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere

def lis(arr):

    global maximum

    n = len(arr)

    maximum = 1

    _lis(arr, n)

    return maximum

arr = [2.,33,9,33,21,50,41,60]
n = len(arr)
print("Lenght of Longest Increasing Subsequence is ", lis(arr))