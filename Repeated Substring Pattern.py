def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, n//2 + 1):    #n//2 to make it half
        if n % i == 0 and s[:i] * (n//i) == s:      #s[:i] -> substring
            return True                             # * (n//i) multiply with substring and compare it with s
    return False

print(repeatedSubstringPattern("abcabcabcabc"))

#best solution
'''
return s in (s+s)[1:-1]
'''