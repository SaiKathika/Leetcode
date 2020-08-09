#This is classical bit manipulation problem for n & (n-1) trick, which removes the last non-zero bit from our number
#n = 100000, then n - 1 = 011111 and n & (n-1) = 000000, so if it is power of two, result is zero
#n = 101110, then n - 1 = 101101 and n & (n-1) = 101100, number is not power of two and result is not zero.
#Answer:  return n>0 and not (n & n-1)

#Another examle
'''
Example: n = 8
n is  even then divide by 2, n = n / 2 = 4
n is  even then divide by 2, n = n / 2 = 2
n is  even then divide by 2, n = n / 2 = 1
'''
def isPowerOfTwo(n):
    while n>0 and n%2 == 0: n /= 2
    return n==1
print(isPowerOfTwo(218))
