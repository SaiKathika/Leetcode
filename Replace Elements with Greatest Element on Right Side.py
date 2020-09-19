def replaceElements(arr):
    i = 0
    while i + 1 < len(arr):
        arr[i] = max(arr[i+1:])
        i += 1
    arr[-1] = -1
    return arr

print(replaceElements([17,18,5,4,6,1]))