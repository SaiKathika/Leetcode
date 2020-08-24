def duplicateZeros(arr):
    lst = []
    for i in arr:
        if i == 0:
            lst.extend((i, i))
        else:
            lst.append(i)
    del lst[len(arr):]
    for i in range(len(lst)):
        arr[i] = lst[i]
    return arr

print(duplicateZeros([1,0,2,3,0,4,5,0]))
'''
#best answer
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == 0:
        arr.pop()
        arr.insert(i, 0)
'''