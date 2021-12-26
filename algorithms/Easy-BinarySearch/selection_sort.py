def getSmallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest, smallest_idx

def selectionSort(array):
    result = []
    for i in range(len(array)):
        value, index = getSmallest(array)
        result.append(array.pop(index))
    return result

print(selectionSort([3,4,5,2,6,8,15,67,896,343,676,2343,7,45,3453,67,34,898,123,454,234]))
