def insertionSort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [12,11,13,5,6]
insertionSort(arr)
print("Sroted array is:")
for i in range(len(arr)):
    print('%d' %arr[i])
