def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and (arr[i] == 2 * arr[j]):
                return True
    return False

print(checkIfExist([7,1,14,11]))
'''
#best one
d={}
for i in range(len(arr)):
    if arr[i]*2 in d or (arr[i]%2==0 and arr[i]//2 in d):
        return True
    else:
        d[arr[i]]=1
return False
'''