def compareVersion(version1, version2):
    lst1, lst2 = version1.split('.'), version2.split('.')

    l1, l2 = len(lst1), len(lst2)

    for i in range(max(l1, l2)):
        i1 = int(lst1[i]) if i < l1 else 0
        i2 = int(lst2[i]) if i < l2 else 0

        if i1 != i2:    #if i1 and i2 different then we compare
            return 1 if i1 > i2 else -1
    return 0

print(compareVersion("7.5.2.4", "7.5.3"))