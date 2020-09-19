def wordPattern(pattern, str):
    str = str.split()
    #print(set(zip(pattern, str)))   #{('a', 'dog'), ('b', 'cat')}
    return  len(str) == len(pattern) and len(set(str)) == len(set(pattern)) == len(set(zip(pattern, str)))

print(wordPattern("abba", "dog cat cat dog"))